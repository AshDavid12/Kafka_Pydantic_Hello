import asyncio
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from pydantic import BaseModel

class MessageModel(BaseModel):
    text: str

async def main():
    # Kafka configuration
    kafka_bootstrap_servers = 'localhost:9092'
    
    # Initialize the producer
    producer = AIOKafkaProducer(bootstrap_servers=kafka_bootstrap_servers)
    await producer.start()

    # Initialize the consumer
    consumer = AIOKafkaConsumer(
        'test-topic',
        bootstrap_servers=kafka_bootstrap_servers,
        group_id='test',
        auto_offset_reset='earliest'
    )
    await consumer.start()

    try:
        # Create an instance of the Pydantic model
        message = MessageModel(text='Hello world!')
        
        # Serialize the Pydantic model to JSON
        message_json = message.json()
        print(f'Sending message: {message_json}')
        
        # Produce a message to the "hello-world" topic
        await producer.send_and_wait('test-topic', value=message_json.encode('utf-8'))
        print("Message sent successfully!")
        
        # Consume the message
        async for msg in consumer: #async loop 
            message_json = msg.value.decode('utf-8') #byes format get back to json format
            message = MessageModel.parse_raw(message_json) #get it back to pydantic object
            print(f"Consumed message: {message.text}") #text arrtibute of pydantic object
            break  # Exit after consuming one message

    finally:
        # Stop the producer and consumer
        await producer.stop()
        await consumer.stop()

# Run the event loop
asyncio.run(main())
