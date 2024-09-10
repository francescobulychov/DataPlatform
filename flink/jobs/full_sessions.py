import json
import datetime
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types

from pyflink.datastream.functions import KeyedProcessFunction, RuntimeContext
from pyflink.datastream.state import ValueStateDescriptor


class FullSessions(KeyedProcessFunction):

    def __init__(self):
        self.state = None

    def open(self, runtime_context: RuntimeContext):
        self.state = runtime_context.get_state(ValueStateDescriptor(
            "state", Types.PICKLED_BYTE_ARRAY()))

    def process_element(self, value, ctx: 'KeyedProcessFunction.Context'):

        previous_state = self.state.value()
        if previous_state is None:
            previous_state = dict(
                charger_id = None,
                start_parking = None,
                plate = None,

                start_session = None,
                user_id = None,
                price = None, 

                start_recharging = None,
                energy_delivered = None,

                end_recharging = None,
                end_session = None,
                end_parking = None
            )
        
        data = json.loads(value)

        if data.get('vehicle_detected') is not None:
            if data['vehicle_detected'] == True:
                previous_state['charger_id'] = data['charger_id']
                previous_state['start_parking'] = data['timestamp']
                previous_state['plate'] = data['plate']

        if data.get('user_connection') is not None:
            if data['user_connection'] == True:
                previous_state['user_id'] = data['user_id']
                previous_state['start_session'] = data['timestamp']
                previous_state['price'] = data['price']

        if data.get('recharging') is not None:
            if data['recharging'] == True:  
                previous_state['start_recharging'] = data['timestamp']
                previous_state['energy_delivered'] = data['energy_delivered']

        if data.get('recharging') is not None:
            if data['recharging'] == False:
                previous_state['end_recharging'] = data['timestamp'] 

        if data.get('user_connection') is not None:
            if data['user_connection'] == False:
                previous_state['end_session'] = data['timestamp'] 

        self.state.update(previous_state)

        if data.get('vehicle_detected') is not None:
            if data['vehicle_detected'] == False:
                previous_state['end_parking'] = data['timestamp']

                return_data = dict(
                    charger_id = previous_state['charger_id'],
                    start_parking = previous_state['start_parking'],
                    plate = previous_state['plate'],
                    start_session = previous_state['start_session'],
                    user_id = previous_state['user_id'],
                    price = previous_state['price'],
                    start_recharging = previous_state['start_recharging'],
                    energy_delivered = previous_state['energy_delivered'],
                    end_recharging = previous_state['end_recharging'],
                    end_session = previous_state['end_session'],
                    end_parking = previous_state['end_parking']
                )

                self.state.clear()
                yield json.dumps(return_data)

                
if __name__ == '__main__':

    env = StreamExecutionEnvironment.get_execution_environment()
    # https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.1.0-1.18/flink-sql-connector-kafka-3.1.0-1.18.jar
    env.add_jars("file:///opt/flink/usrlib/flink-sql-connector-kafka-3.2.0-1.19.jar")

    kafka_consumer = FlinkKafkaConsumer(
        topics='charger-station-signals',
        deserialization_schema=SimpleStringSchema(),
        properties={'bootstrap.servers': 'broker:19092', 'group.id': 'flink_group_full_sessions'}
    )

    kafka_consumer.set_start_from_earliest()
    stream = env.add_source(kafka_consumer)


    stream = stream.key_by(lambda x: json.loads(x)['charger_id'])
    stream = stream.process(FullSessions(), output_type=Types.STRING())

    kafka_producer = FlinkKafkaProducer(
        topic='full-sessions',
        serialization_schema=SimpleStringSchema(),
        producer_config={'bootstrap.servers': 'broker:19092'}
    )

    stream.add_sink(kafka_producer)

    env.execute()
