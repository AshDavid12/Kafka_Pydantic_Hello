# Kafka Project

## Overview

This project demonstrates a simple Kafka setup with a producer and a consumer. The producer sends messages to a Kafka topic, and the consumer reads messages from the topic. The project uses aiokafka for asynchronous Kafka operations and pydantic for data validation and parsing.

## Requirements

Python 3.7+
Kafka
Poetry (for dependency management)
Installation

### Install Kafka:

Follow the instructions on the Kafka website to download and start Kafka.  

Install Poetry:  
```
curl -sSL https://install.python-poetry.org | python3 -
```
Install dependencies:

Navigate to the project directory and run:

`poetry install`

## Usage

#### Start Kafka:

Make sure your Kafka server is running on localhost:9092.

#### Run the Producer:

The producer sends a message to the Kafka topic test-topic.

`poetry run python producer.py`

#### Run the Consumer:

The consumer reads messages from the Kafka topic test-topic.


`poetry run python consumer.py`

## Files

consumer.py: Contains the Kafka consumer code.  
producer.py: Contains the Kafka producer code.  
pyproject.toml: Configuration file for Poetry.
