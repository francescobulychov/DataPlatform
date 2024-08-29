import json
import datetime
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types

from pyflink.datastream.functions import KeyedProcessFunction, RuntimeContext
from pyflink.datastream.state import ValueStateDescriptor


def send_violation(previous_state, code):

    data = dict(
        charger_id = previous_state['charger_id'],
        user_id = previous_state['user_id'],
        plate = previous_state['plate'],
        start_parking = previous_state['start_parking'],
        start_session = previous_state['start_session'],
        end_session = previous_state['end_session'],
        end_parking = previous_state['end_parking'],
        violation = None
    )

    if code == 0:
        data['violation'] = "Parking without charging"

    elif code == 1:
        data['violation'] = "Long parking before recharging"

    elif code == 2:
        data['violation'] = "Long parking after recharging"
    
    
    return data


def violation_time_before_recharging(previous_state):
    if previous_state['start_session'] is None and previous_state['start_parking'] is not None:
        start_parking = datetime.datetime.strptime(previous_state['start_parking'], '%Y-%m-%d %H:%M:%S')

        now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')

        if (now - start_parking).total_seconds() > 13:
            return True
    return False


def violation_time_after_recharging(previous_state):
    if previous_state['end_session'] is not None:
        end_session = datetime.datetime.strptime(previous_state['end_session'], '%Y-%m-%d %H:%M:%S')

        now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')

        if (now - end_session).total_seconds() > 13:
            return True
    return False


class DetectViolations(KeyedProcessFunction):

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

                end_session = None,
                end_parking = None,
                violations_detected = []
            )
        
        data = json.loads(value)

        if data.get('vehicle_detected') is not None:
            if data['vehicle_detected'] == True:
                previous_state['charger_id'] = data['charger_id']
                previous_state['start_parking'] = data['timestamp']

                previous_state['plate'] = data['plate']

        if 1 not in previous_state['violations_detected'] and violation_time_before_recharging(previous_state) == True:
            previous_state['violations_detected'].append(1)
            yield json.dumps(send_violation(previous_state, 1))

        if data.get('user_connection') is not None:
            if data['user_connection'] == True:
                previous_state['user_id'] = data['user_id']
                previous_state['start_session'] = data['timestamp']

        if data.get('user_connection') is not None:
            if data['user_connection'] == False:
                previous_state['end_session'] = data['timestamp'] 

        if 2 not in previous_state['violations_detected'] and violation_time_after_recharging(previous_state) == True:
            previous_state['violations_detected'].append(2)
            yield json.dumps(send_violation(previous_state, 2))

        self.state.update(previous_state)

        if data.get('vehicle_detected') is not None:
            if data['vehicle_detected'] == False:
                previous_state['end_parking'] = data['timestamp']

                # check if vehicle leaves without charging
                if previous_state['start_session'] == None:
                    yield json.dumps(send_violation(previous_state, 0))

                self.state.clear()






        




if __name__ == '__main__':

    env = StreamExecutionEnvironment.get_execution_environment()
    # https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.1.0-1.18/flink-sql-connector-kafka-3.1.0-1.18.jar
    env.add_jars("file:///opt/flink/usrlib/flink-sql-connector-kafka-3.2.0-1.19.jar")

    kafka_consumer = FlinkKafkaConsumer(
        topics='charger-station-signals',
        deserialization_schema=SimpleStringSchema(),
        properties={'bootstrap.servers': 'broker:19092', 'group.id': 'flink_group_violations'}
    )

    kafka_consumer.set_start_from_earliest()
    stream = env.add_source(kafka_consumer)


    stream = stream.key_by(lambda x: json.loads(x)['charger_id'])
    stream = stream.process(DetectViolations(), output_type=Types.STRING())

    kafka_producer = FlinkKafkaProducer(
        topic='violations',
        serialization_schema=SimpleStringSchema(),
        producer_config={'bootstrap.servers': 'broker:19092'}
    )

    stream.add_sink(kafka_producer)

    env.execute()
