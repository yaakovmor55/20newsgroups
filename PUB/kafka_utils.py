from kafka import KafkaProducer
import json



def get_producer_config():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x:
                             json.dumps(x).encode('utf-8'))
    return producer


def publish_message(producer,topic,message):
    producer.send(topic, message)





