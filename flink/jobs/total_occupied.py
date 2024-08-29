import json
import datetime
from collections import defaultdict
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types

from pyflink.datastream.functions import KeyedProcessFunction, RuntimeContext
from pyflink.datastream.state import ValueStateDescriptor


def only_parking_sensor(data):
    data = json.loads(data)
    if data.get('vehicle_detected') is not None:
        return True
    return False

class TotalOccupied(KeyedProcessFunction):

    def __init__(self):
        self.state = None
        self.timer_state = None

    def open(self, runtime_context: RuntimeContext):
        self.state = runtime_context.get_state(ValueStateDescriptor(
            "state", Types.PICKLED_BYTE_ARRAY()))
        self.timer_state = runtime_context.get_state(ValueStateDescriptor(
            "timer_state", Types.LONG()))

    def process_element(self, value, ctx: 'KeyedProcessFunction.Context'):

        occupancy_map = self.state.value()
        if occupancy_map is None:
            occupancy_map = defaultdict(bool)
        
        data = json.loads(value)
        occupancy_map[data['charger_id']] = data['vehicle_detected']

        self.state.update(occupancy_map)

        if self.timer_state.value() is None:
            timer = ctx.timestamp() + 1000
            ctx.timer_service().register_processing_time_timer(timer)
            self.timer_state.update(timer)

    def on_timer(self, timestamp: int, ctx: 'KeyedProcessFunction.OnTimerContext'):

        result = self.state.value()

        return_data = dict(
            timestamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
            occupied = sum(1 for occupied in result.values() if occupied)
        )

        yield json.dumps(return_data)

        timer = ctx.timestamp() + 1000
        ctx.timer_service().register_processing_time_timer(timer)
        self.timer_state.update(timer)



if __name__ == '__main__':

    env = StreamExecutionEnvironment.get_execution_environment()
    # https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.1.0-1.18/flink-sql-connector-kafka-3.1.0-1.18.jar
    env.add_jars("file:///opt/flink/usrlib/flink-sql-connector-kafka-3.2.0-1.19.jar")

    kafka_consumer = FlinkKafkaConsumer(
        topics='charger-station-signals',
        deserialization_schema=SimpleStringSchema(),
        properties={'bootstrap.servers': 'broker:19092', 'group.id': 'flink_group_occupied_counter'}
    )

    kafka_consumer.set_start_from_earliest()
    stream = env.add_source(kafka_consumer)

    stream = stream.filter(only_parking_sensor)

    stream = stream.key_by(lambda x: 'global')

    stream = stream.process(TotalOccupied(), output_type=Types.STRING())

    kafka_producer = FlinkKafkaProducer(
        topic='total-occupied',
        serialization_schema=SimpleStringSchema(),
        producer_config={'bootstrap.servers': 'broker:19092'}
    )

    stream.add_sink(kafka_producer)

    env.execute()

