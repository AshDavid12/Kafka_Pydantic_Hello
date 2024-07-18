import asyncio
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from pydantic import BaseModel

class MessageModel(BaseModel):
    text: str

kafka_bootstrap_servers = 'localhost:9092'
message = MessageModel(text='Hello!')
        
# Serialize the Pydantic model to JSON
message_json = message.json()
async def producer():
    # Initialize the producer
    producer = AIOKafkaProducer(bootstrap_servers=kafka_bootstrap_servers)
    await producer.start()
    try:
        await producer.send_and_wait('test-topic', value=message_json.encode('utf-8'))
    finally:
        await producer.stop()


async def consumer():
    consumer = AIOKafkaConsumer(
        'test-topic',
        bootstrap_servers=kafka_bootstrap_servers,
        group_id='test',
        auto_offset_reset='earliest'
    )
    await consumer.start()
    try:
        async for msg in consumer:
            message_json = msg.value.decode('utf-8') #byes format get back to json format
            message = MessageModel.parse_raw(message_json) #get it back to pydantic object
            print(f"Consumed message: {message.text}") #text arrtibute of pydantic object
            break  # Exit after consuming one message
    finally:
        await consumer.stop()

async def main():
    await producer()
    await consumer()
asyncio.run(main())
  




        
 

