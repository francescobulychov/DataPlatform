# Data platform
A data platform is an integrated set of technologies that collectively meet an organization's end-to-end data needs. It enables the acquisition, storage, preparation, delivery, and governance of your data, as well as a security layer for users and applications. 

The main advantage to use a data platform comes from the fact that it's a combination of interoperable, scalable, and replaceable technologies working together to deliver an enterprise's overall data needs.

###### Sources
- https://www.mongodb.com/resources/basics/what-is-a-data-platform

# Event-driven architecture (EDA)
Event-driven architecture (EDA) is a software architecture paradigm concerning the production and detection of events. 

An event can be defined as "a significant change in state". For example, when a consumer purchases a car, the car's state changes from "for sale" to "sold".

An event-driven system typically consists of event emitters (or agents), event consumers (or sinks), and event channels. Emitters have the responsibility to detect, gather, and transfer events. Sinks have the responsibility of applying a reaction as soon as an event is presented forwarding the event to another component or providing a self-contained reaction to such an event. Event channels are conduits in which events are transmitted from event emitters to event consumers.

Building systems around an event-driven architecture simplifies horizontal scalability because application state can be copied across multiple parallel snapshots for high-availability, new events can be initiated anywhere and propagate across the network of data stores and sdding extra nodes is simple as take a copy of the application state, feed it a stream of events and run with it.

## Examples
Netflix implemented an event-driven architecture powered by Apache Kafka to establish a scalable and reliable platform for finance data processing, thus becoming a significant event producer.

###### Sources
- https://en.wikipedia.org/wiki/Event-driven_architecture
- https://estuary.dev/event-driven-architecture-examples/

# Message-oriented middleware (MOM)
Message-oriented middleware (MOM) is software or hardware infrastructure supporting sending and receiving messages between distributed systems.  

This middleware layer allows software components that have been developed independently and that run on different networked platforms to interact with one another. 

Most used MOM are: RabbitMQ, Apache Kafka, IBM MQ, Nats.

###### Sources
- https://en.wikipedia.org/wiki/Message-oriented_middleware

## Message brokers
A message broker  is an intermediary computer program module that translates a message from the formal messaging protocol of the sender to the formal messaging protocol of the receiver.  

The primary purpose of a broker is to take incoming messages from applications and perform some action on them. For example, a message broker may be used to manage a workload queue or message queue for multiple receivers, providing reliable storage, guaranteed message delivery and perhaps transaction management. 

Message brokers are a building block of message-oriented middleware (MOM) but are typically not a replacement for traditional middleware.

###### Sources
- https://en.wikipedia.org/wiki/Message_broker

## Message queuing
The message queue paradigm is typically one part of a larger message-oriented middleware system. 

Message queues implement an asynchronous communication pattern between two or more processes/threads whereby the sending and receiving party do not need to interact with the message queue at the same time. Messages placed onto the queue are stored until the recipient retrieves them. Message queues have implicit or explicit limits on the size of data that may be transmitted in a single message and the number of messages that may remain outstanding on the queue.

###### Sources
- https://en.wikipedia.org/wiki/Message_queue
- https://en.wikipedia.org/wiki/Message_queuing_service

# Event stream processing
Event stream processing is a paradigm which views streams, or sequences of events in time, as the central input and output objects of computation. 

Event streaming platforms provide an architecture that enable software to understand, react to, and operate as events occur.

The most used event streaming platforms are: Apache Kafka , Redpanda.

###### Sources
- https://en.wikipedia.org/wiki/Stream_processing

# Real time stream processing
Real-time stream processing refers to the continuous and real-time analysis of data as it flows into a system. The primary goal is to process data with minimal latency to provide immediate insights or trigger actions.

The most used event streaming platforms are: Apache Kafka, Amazon Kinesis, Apache Flink, Apache NiFi.

# Data visualization
Data visualization tools are software applications that render information in a visual format such as a graph, chart, or heat map for data analysis purposes. Such tools make it easier to understand and work with massive amounts of data.

The most used data visualization platforms are: Grafana, Apache Superset, Kibana, Tableau, Power BI.

# Types of databases

## Relational database
In relational databases, each table stores information represented as attributes (columns) and tuples (rows). Each table has a primary key that uniquely identifies a record in the table. Foreign keys are references to a primary key in a different table.

This type of database should be used with structured data (rows and columns that clearly define data attributes) and when ACID properties (Atomicity, Consistency, Isolation, Durability) are required, but should not be used with big volumes of data because it doesn´t scale well.

Most used relational databases are: MySQL, PostreSQL, Oracle Database, Microsoft SQL Server.

## Columnar database
Columnar databases can utilize algorithms to simplify data retrievals. Compared with traditional databases, they don´t read billions of rows of data but only few long columns. They are usually used for analytics.

Most used columnar databases are: ClickHouse, Apache Cassandra, Amazon Redshift, Apache Druid, MariaDB.

## Document-oriented database
Document-oriented databases store and query data in JSON-like documents, simplifying management and improving reading speed. For example changing attribute of one item doesn´t affect other items.

The advantages of using a document-oriented database are: ease of development, flexible schema, performance at (horizontal) scale. They are usually used in unstructured data.

Most used document-oriented databases are: MongoDB, CouchDB.

## Time-Series database
Time-Series databases are optimized for measurements or events that are tracked, monitored and aggregated over time. The most common uses are in server metrics, application monitoring, sensor data, events etc.

The advantages of using time-series database are: data are highly compressed because of the very high write throughupt and for their similarities between each other, data is written to latest time entry only, efficient large range scans of many records (ex. one month of stock price).

Most used time-series databases are: TimeScaleDB, Prometheus, InfluxDB.

###### Sources
- https://en.wikipedia.org/wiki/Relational_database
- https://en.wikipedia.org/wiki/Data_orientation
- https://en.wikipedia.org/wiki/Document-oriented_database
- https://en.wikipedia.org/wiki/Time_series_database
- https://www.youtube.com/watch?v=VfcRxtBKI54
- https://www.youtube.com/watch?v=vuNEWixlsWY
- https://www.pareto.si/blog/storage-solutions-for-sensor-data/

# Query engines
A query engine is a piece of software that sits on top of a database or server and executes queries against data in that database or server to provide answers for users or applications. 

You can bring a query engine to your data instead of having to move your data somewhere else. A distributed SQL query engine will allow you to query data from a variety of data sources like Hadoop, AWS S3, NoSQL, MySQL, and more, or data from multiple data sources within a single query.

Examples of query engines include Presto, Apache Drill, Cloudera Impala, and Apache Spark.

###### Sources
- https://www.alluxio.io/learn/presto/query/

# Docker
Docker is an open platform for developing, shipping, and running applications. It provides the ability to package and run an application in a loosely isolated environment called a container.

## Docker compose
Docker Compose is a tool that helps you define and share multi-container applications. It is possible to create a YAML file to define the services and with a single command, spin everything up or tear it all down.