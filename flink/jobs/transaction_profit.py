import json
import datetime
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types

from pyflink.datastream.functions import KeyedProcessFunction, RuntimeContext
from pyflink.datastream.state import ValueStateDescriptor


def calculate_total_energy_delivered(previous_state):
    end_recharging = datetime.datetime.strptime(previous_state['end_recharging'], '%Y-%m-%d %H:%M:%S')
    start_recharging = datetime.datetime.strptime(previous_state['start_recharging'], '%Y-%m-%d %H:%M:%S')

    # seconds as minutes to simulate realistic profit
    time_recharging = (end_recharging - start_recharging).total_seconds() 
    time_recharging = time_recharging / 60

    return previous_state['energy_delivered'] * time_recharging


class TransactionProfit(KeyedProcessFunction):

    def __init__(self):
        self.state = None

    def open(self, runtime_context: RuntimeContext):
        self.state = runtime_context.get_state(ValueStateDescriptor(
            "state", Types.PICKLED_BYTE_ARRAY()))

    def process_element(self, value, ctx: 'KeyedProcessFunction.Context'):

        previous_state = self.state.value()
        if previous_state is None:
            previous_state = dict(
                connection_state = False,
                charger_id = None,
                user_id = None,
                price = None,
                energy_delivered = None,
                start_recharging = None,
                end_recharging = None
            )
        
        data = json.loads(value)

        if data.get('user_connection') is not None:
            if data['user_connection'] == True:
                previous_state['connection_state'] = True
                previous_state['charger_id'] = data['charger_id']
                previous_state['user_id'] = data['user_id']
                previous_state['price'] = data['price']
        
        if data.get('recharging') is not None and previous_state['connection_state'] == True:
            if data['recharging'] == True:
                previous_state['energy_delivered'] = data['energy_delivered']
                previous_state['start_recharging'] = data['timestamp']

        if data.get('recharging') is not None and previous_state['connection_state'] == True:
            if data['recharging'] == False:
                previous_state['end_recharging'] = data['timestamp']

                total_energy_delivered = calculate_total_energy_delivered(previous_state)

                return_data = dict(
                    charger_id = previous_state['charger_id'],
                    user_id = previous_state['user_id'],
                    start_recharging = previous_state['start_recharging'],
                    end_recharging = previous_state['end_recharging'],
                    total_energy_delivered = total_energy_delivered,
                    profit = round(total_energy_delivered * previous_state['price'], 2)
                )

                self.state.clear()
                yield json.dumps(return_data)
        
        self.state.update(previous_state)







if __name__ == '__main__':

    env = StreamExecutionEnvironment.get_execution_environment()
    # https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.1.0-1.18/flink-sql-connector-kafka-3.1.0-1.18.jar
    env.add_jars("file:///opt/flink/usrlib/flink-sql-connector-kafka-3.2.0-1.19.jar")

    kafka_consumer = FlinkKafkaConsumer(
        topics='charger-station-signals',
        deserialization_schema=SimpleStringSchema(),
        properties={'bootstrap.servers': 'broker:19092', 'group.id': 'flink_group'}
    )

    kafka_consumer.set_start_from_earliest()
    stream = env.add_source(kafka_consumer)


    stream = stream.key_by(lambda x: json.loads(x)['charger_id'])
    stream = stream.process(TransactionProfit(), output_type=Types.STRING())

    kafka_producer = FlinkKafkaProducer(
        topic='transaction-profit',
        serialization_schema=SimpleStringSchema(),
        producer_config={'bootstrap.servers': 'broker:19092'}
    )

    stream.add_sink(kafka_producer)

    env.execute()
