


project/
└── app/
    ├── domain/
    │   ├── entities/
    │   │   └── text_message.py
    │   ├── ports/
    │   │   ├── repository_port.py
    │   │   ├── publisher_port.py
    │   │   └── consumer_port.py
    │   └── services/
    │       └── text_processor.py
    │
    ├── application/
    │   ├── text_processing_service.py
    │   └── process_message_usecase.py
    │
    ├── adapters/
    │   ├── mongodb/
    │   │   └── repository.py
    │   └── rabbitmq/
    │       ├── consumer.py
    │       └── publisher.py
    │
    ├── infrastructure/
    │   ├── mongo_connection.py
    │   └── rabbitmq_connection.py
    │
    └── main.py
├── requirements.txt
└── Dockerfile (optionnel)
