# streamlit_app.py
#import streamlit as st
import asyncio
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from pydantic import BaseModel
from confluent_kafka import Producer,Consumer,KafkaException, KafkaError
import logging
logging.basicConfig(level=logging.INFO)

# def main():

class Paragraph(BaseModel):
    text:str

kafka_config_consumer = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'hiyyyppiuuiikk',
    'auto.offset.reset': 'earliest' 
}

consumer = Consumer(kafka_config_consumer)

topic = 'paragraph'


kafka_config_producer = {
    'bootstrap.servers': 'localhost:9092'
}
producer2 = Producer(kafka_config_producer)
topic_out = 'names'


consumer.subscribe([topic])
def consume_messages(consumer, producer, timeout=1.0):
    try:
        logging.info("Starting the consumer1...")
        while True:
            msg = consumer.poll(timeout)
            if msg is None:
                continue
            elif msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    logging.info(f'{msg.topic()} [{msg.partition()}] reached end at offset {msg.offset()}')
                else:
                    raise KafkaException(msg.error())
            else:
                logging.info(f'Received message: {msg.value().decode("utf-8")}')
                message_text = msg.value().decode("utf-8")
                words = message_text.split()
                capitalized_words = [word for word in words if word.istitle()]

                for word in capitalized_words:
                    producer.produce(topic_out, key=None, value=word.encode('utf-8'))
                    producer.flush()
                    print(f'Sent: {word}')
                    #logging.info(f'Sent: {word}')
    except KeyboardInterrupt:
        logging.info("Consumer interrupted.")
    finally:
        consumer.close()




if __name__ == "__main__":
    consume_messages(consumer,producer2)