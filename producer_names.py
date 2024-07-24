import asyncio
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from pydantic import BaseModel
from confluent_kafka import Producer,Consumer,KafkaException, KafkaError
import logging
from consumer import consume_messages
logging.basicConfig(level=logging.INFO)

# def main():

class Paragraph(BaseModel):
    text:str


kafka_config_producer = {
    'bootstrap.servers': 'localhost:9092'
}
producer2 = Producer(kafka_config_producer)
topic_out = 'names'

def get_names(words):
        print("got names in producer2")
        return words

names = get_names(words)
def produce_names(words):

                for word in capitalized_words:
                    producer.produce(topic_out, key=None, value=word.encode('utf-8'))
                    producer.flush()
                    print(f'Sent: {word}')
                    #logging.info(f'Sent: {word}')