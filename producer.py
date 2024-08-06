import random
import time
import datetime
import json
from kafka import KafkaProducer # pip install kafka-python-ng

def get_temperature(i):
    if i == 0:
        return i + 1
    elif i == 30:
        return i - 1
    else:
        return random.choice([i-1, i+1])

producer = KafkaProducer(bootstrap_servers='localhost:9092')
celsius = random.randint(0, 30)

while True:
    current_time = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S')
    celsius = get_temperature(celsius)

    new_message = dict(
        timestamp = current_time,
        celsius = celsius
    )

    producer.send(
        topic='topic-test',
        value=json.dumps(new_message).encode('utf-8')
    )
    print(f"[+] Generated temperature: {celsius}°C at {current_time}")
    time.sleep(1)

