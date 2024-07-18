from pydantic import BaseModel
from confluent_kafka import Producer,Consumer,KafkaException, KafkaError
import json
import time

class MessageModel(BaseModel):
    text: str

kafka_config = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address - standard
    #usually ppl use local and the 9092 is the defult port
}

kafka_config2 = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address - standard
    #usually ppl use local and the 9092 is the defult port
    'group.id': 'test',
    'auto.offset.reset': 'earliest' 
}

producer = Producer(kafka_config)
consumer = Consumer(kafka_config2)

# Define a callback function for message delivery reports
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}] key: {msg.key()}, value: {msg.value()}')
        #the value is in byte format so the value will have a b and then the json string
# Create an instance of the Pydantic model
message = MessageModel(text='Hello world!')

# Serialize the Pydantic model to JSON
message_json = message.json()
print(f'{message_json}')
# Produce a message to the "hello-world" topic
topic = 'hello-world'

producer.produce(topic, key = None,value=message_json.encode('utf-8'), callback=delivery_report)
#kafka needs the json to be converted to bytes. thats why we convert the json with encode
#this takes the json and covertes to bytes array for kafka to understand
producer.flush()
time.sleep(2)
consumer.subscribe([topic])
msg = consumer.poll(timeout=20.0)  # Increased timeout to ensure the message is received

if msg is None:
    print("No message received within the timeout.")
elif msg.error():
    if msg.error().code() == KafkaError._PARTITION_EOF:
        print(f'{msg.topic()} [{msg.partition()}] reached end at offset {msg.offset()}')
    else:
        raise KafkaException(msg.error())
else:
    # Message received successfully
    print(f'Received message: {msg.value().decode("utf-8")}')

consumer.close()

