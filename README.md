# Kafka Producer and Consumer with Pydantic  

This project demonstrates the use of a Kafka producer and consumer in Python, using the Confluent Kafka library and Pydantic for data validation and serialization.

## Features

Kafka Producer: Sends messages to a Kafka topic.  
Kafka Consumer: Listens for messages from a Kafka topic.  
Pydantic Integration: Uses Pydantic for data validation and JSON serialization.  

## Requirements

Python 3.7+
Kafka server running on localhost:9092 (default settings)
## Installation
Clone the repository:

```
git clone https://github.com/yourusername/kafka-pydantic-hello.git
cd kafka-pydantic-hello
```
### Install dependencies:
Using Poetry:
If you don't have Poetry installed, you can install it by following the instructions here.  
`poetry install`  

## Branches
- check out branch async for a version of this project that deploysasynchronous Kafka using aiokafka operations and pydantic for data validation and parsing. 
