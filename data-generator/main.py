import random
import time
import datetime
import string
import threading
import json
from kafka import KafkaProducer

from kafka.admin import KafkaAdminClient, NewTopic
from kafka.partitioner import DefaultPartitioner

def kafka_setup():
    admin_client = KafkaAdminClient(bootstrap_servers='broker:19092', client_id='admin1')
    
    charger_station_topic = NewTopic(
        name='charger-station-signals',
        num_partitions=100,
        replication_factor=1
    )

    admin_client.create_topics([charger_station_topic])
    admin_client.close()

    global producer
    producer = KafkaProducer(bootstrap_servers='broker:19092')

def send_kafka(data):
    producer.send(
    topic='charger-station-signals',
    key=data['charger_id'].encode('utf-8'),
    value=json.dumps(data).encode('utf-8'),
    partition=int(data['charger_id'].split('-')[-1])
)

def probability_check(probability):
    if random.random() < probability:
        return True
    return False

def get_timestamp():
    return datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S')

class ParkingSensor:
    def __init__(self, charger_id):
        self.timestamp = get_timestamp()
        self.charger_id = charger_id
        self.vehicle_detected = False
        self.plate = None

    def send_ParkingSensor_signal(self):
        data = dict(
            timestamp = self.timestamp,
            charger_id = self.charger_id,
            vehicle_detected = self.vehicle_detected,
            plate = self.plate
        )
        print(f"[+] Sending parking sensor signal:\n {data}\n")
        send_kafka(data)

    def detect_vehicle(self):
        self.timestamp = get_timestamp()
        self.vehicle_detected = True
        self.plate = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        self.send_ParkingSensor_signal()
        
    def detect_vehicle_leave(self):
        self.timestamp = get_timestamp()
        self.vehicle_detected = False
        self.send_ParkingSensor_signal()

        

class UserDataSensor:
    def __init__(self, charger_id):
        self.timestamp = get_timestamp()
        self.charger_id = charger_id
        self.user_id = None
        self.price = None
        self.user_connection = False

    def send_UserDataSensor_signal(self):
        data = dict(
            timestamp = self.timestamp,
            charger_id = self.charger_id,
            user_id = self.user_id,
            price = self.price,
            user_connection = self.user_connection
        )
        print(f"[+] Sending user data sensor signal:\n {data}\n")
        send_kafka(data)
    
    def connect_user(self):
        self.timestamp = get_timestamp()
        self.user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        self.price = round(random.uniform(0.40, 0.99), 2)
        self.user_connection = True
        self.send_UserDataSensor_signal()

    def disconnect_user(self):
        self.timestamp = get_timestamp()
        self.user_id = self.user_id
        self.price = self.price
        self.user_connection = False
        self.send_UserDataSensor_signal()



class ChargerSensor:
    def __init__(self, charger_id):
        self.timestamp = get_timestamp()
        self.charger_id = charger_id
        self.recharging = False
        self.energy_delivered = 0

    def send_ChargerSensor_signal(self):
        data = dict(
            timestamp = self.timestamp,
            charger_id = self.charger_id,
            recharging = self.recharging,
            energy_delivered = self.energy_delivered
        )
        print(f"[+] Sending charger sensor signal:\n {data}\n")
        send_kafka(data)
    
    def start_recharging(self):
        self.timestamp = get_timestamp()
        self.recharging = True
        self.energy_delivered = random.randint(10, 30)
        self.send_ChargerSensor_signal()

    def stop_recharging(self, UserDataSensor):
        self.timestamp = get_timestamp()
        self.recharging = False
        self.energy_delivered = 0
        self.send_ChargerSensor_signal()

        UserDataSensor.disconnect_user()


def simulate_charging_station(charger_id):

    parking_sensor = ParkingSensor(charger_id)
    user_data_sensor = UserDataSensor(charger_id)
    charger_sensor = ChargerSensor(charger_id)

    while True:

        time.sleep(1)

        # 30% probability of vehicle detection if no vehicle is detected
        if not parking_sensor.vehicle_detected and probability_check(0.3):
            parking_sensor.detect_vehicle()
            continue

        # 2% probability of vehicle not using the charger
        if parking_sensor.vehicle_detected and probability_check(0.02):
            time.sleep(random.randint(5, 10)) # 5, 30 change time
            parking_sensor.detect_vehicle_leave()
            continue

        # 98% probability of vehicle using the charger
        if parking_sensor.vehicle_detected:

            # 2% probability of user waiting too much before using charger
            if probability_check(0.02):
                time.sleep(random.randint(15, 20)) 

            time.sleep(random.randint(1, 3))
            user_data_sensor.connect_user()

            time.sleep(random.randint(1, 3))
            charger_sensor.start_recharging()

            time.sleep(random.randint(8, 10)) # 20, 40 change time

            charger_sensor.stop_recharging(user_data_sensor)

            # 2% probability of user not leaving for a while
            if probability_check(0.02):
                time.sleep(random.randint(15, 20))
                parking_sensor.detect_vehicle_leave()
                continue

            # 98% probability of user leaving without extra time
            time.sleep(random.randint(2, 5))
            parking_sensor.detect_vehicle_leave()
            continue
            


if __name__ == "__main__":
    time.sleep(5)

    kafka_setup()

    time.sleep(5)

    charger_ids = [f'charger-{i}' for i in range(0, 100)]

    threads = []
    for charger_id in charger_ids:
        thread = threading.Thread(target=simulate_charging_station, args=(charger_id,))
        threads.append(thread)
        thread.start()