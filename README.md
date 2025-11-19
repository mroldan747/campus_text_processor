# Text Message Processing Service

This project is an asynchronous message processing system built with Python, RabbitMQ, and MongoDB.
It follows an approach, separating adapters, application logic, interfaces, and infrastructure connections.

The service consumes messages from RabbitMQ, processes them, and persists or updates them in MongoDB.

The project uses docker & docker-compose for development

## Running the Project

Start services with Docker Compose
- docker-compose up --build

This launches:

RabbitMQ with management UI

MongoDB

The message processing service

RabbitMQ UI could be accessed with:
http://localhost:15672


## Tests 

I have created a script that publish messages, that the consumer can consume and handle to show the behavior of the service (only for the aiming of this test)

I can be run from inside the text-processor container by running: 

python scripts/send_messages.py

### Unit tests

Inside the tests/unit directory there are the unit tests for the project they can be run inside the text-processor container by running: 

pytest test/unit/



## Architecture Overview

Here I wanted to divide the project in different layers so that the domain stays at the center, and it is not impacted by the rest. Also using interfaces to establish contracts of what is 
needed regardless of what kind of database or broker is used:

- interfaces: abstract contracts (Publisher, Repository, Consumer)

- adapters: concrete implementations for external systems (RabbitMQ, MongoDB)

- application: pure logic (use cases, processor)

- connections: initialization of DB and broker

- main: application bootstrap

- domain: everything that is linked to the domain (entities)
