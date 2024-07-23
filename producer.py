import asyncio
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from pydantic import BaseModel

class MessageModel(BaseModel):
    text: str

kafka_bootstrap_servers = 'localhost:9092'
message = MessageModel(text='Hello!')
message_json = message.json()


async def producer():
    # Initialize the producer
    producer = AIOKafkaProducer(bootstrap_servers=kafka_bootstrap_servers)
    await producer.start()
    try:
        await producer.send_and_wait('test-topic', value=message_json.encode('utf-8'))
    finally:
        await producer.stop()

if __name__ == "__main__":
    asyncio.run(producer())