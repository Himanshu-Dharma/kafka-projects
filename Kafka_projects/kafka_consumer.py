import json

from kafka import KafkaConsumer
from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_details"

consumer = KafkaConsumer( ORDER_KAFKA_TOPIC,
                         bootstrap_servers="localhost:9092")

print('picking from producer')
while True:
    for message in consumer:
        print('ongoing transaction..')
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)
