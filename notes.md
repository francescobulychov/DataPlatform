# Study of Data Platform Components

## Data platform
A data platform is an integrated set of technologies that collectively meet an organization's end-to-end data needs. It enables the acquisition, storage, preparation, delivery, and governance of your data, as well as a security layer for users and applications. 

The main advantage to use a data platform comes from the fact that it's a combination of interoperable, scalable, and replaceable technologies working together to deliver an enterprise's overall data needs.

###### Sources
- https://www.mongodb.com/resources/basics/what-is-a-data-platform
- https://medium.com/event-driven-utopia/anatomy-of-an-event-streaming-platform-part-1-dc58eb9b2412

## Event-driven architecture (EDA)
Event-driven architecture (EDA) is a software architecture paradigm concerning the production and detection of events. 

An event can be defined as "a significant change in state". For example, when a consumer purchases a car, the car's state changes from "for sale" to "sold".

An event-driven system typically consists of event emitters (or agents), event consumers (or sinks), and event channels. Emitters have the responsibility to detect, gather, and transfer events. Sinks have the responsibility of applying a reaction as soon as an event is presented forwarding the event to another component or providing a self-contained reaction to such an event. Event channels are conduits in which events are transmitted from event emitters to event consumers.

Building systems around an event-driven architecture simplifies horizontal scalability because application state can be copied across multiple parallel snapshots for high-availability, new events can be initiated anywhere and propagate across the network of data stores and sdding extra nodes is simple as take a copy of the application state, feed it a stream of events and run with it.

### Examples
Netflix implemented an event-driven architecture powered by Apache Kafka to establish a scalable and reliable platform for finance data processing, thus becoming a significant event producer.

###### Sources
- https://en.wikipedia.org/wiki/Event-driven_architecture
- https://estuary.dev/event-driven-architecture-examples/
- https://www.youtube.com/watch?v=LHgCA3XVNkw

## Message-oriented middleware (MOM)
Message-oriented middleware (MOM) is software or hardware infrastructure supporting sending and receiving messages between distributed systems.  

This middleware layer allows software components that have been developed independently and that run on different networked platforms to interact with one another. 

Most used MOM are: RabbitMQ, IBM MQ, Nats.

###### Sources
- https://en.wikipedia.org/wiki/Message-oriented_middleware

### Message brokers
A message broker  is an intermediary computer program module that translates a message from the formal messaging protocol of the sender to the formal messaging protocol of the receiver.  

The primary purpose of a broker is to take incoming messages from applications and perform some action on them. For example, a message broker may be used to manage a workload queue or message queue for multiple receivers, providing reliable storage, guaranteed message delivery and perhaps transaction management. 

Message brokers are a building block of message-oriented middleware (MOM) but are typically not a replacement for traditional middleware.

###### Sources
- https://en.wikipedia.org/wiki/Message_broker

### Message queuing
The message queue paradigm is typically one part of a larger message-oriented middleware system. 

Message queues implement an asynchronous communication pattern between two or more processes/threads whereby the sending and receiving party do not need to interact with the message queue at the same time. Messages placed onto the queue are stored until the recipient retrieves them. Message queues have implicit or explicit limits on the size of data that may be transmitted in a single message and the number of messages that may remain outstanding on the queue.

###### Sources
- https://en.wikipedia.org/wiki/Message_queue
- https://en.wikipedia.org/wiki/Message_queuing_service

## Event stream processing
Event stream processing is a paradigm which views streams, or sequences of events in time, as the central input and output objects of computation. 

Event streaming platforms provide an architecture that enable software to understand, react to, and operate as events occur.

The most used event streaming platforms are: Apache Kafka, Redpanda.

###### Sources
- https://en.wikipedia.org/wiki/Stream_processing
- https://www.youtube.com/watch?v=T3Qkl59okjo

## Real time stream processing
Real-time stream processing refers to the continuous and real-time analysis of data as it flows into a system. The primary goal is to process data with minimal latency to provide immediate insights or trigger actions.

The most used event streaming platforms are: Apache Kafka, Amazon Kinesis, Apache Flink, Apache NiFi.

## Data visualization
Data visualization tools are software applications that render information in a visual format such as a graph, chart, or heat map for data analysis purposes. Such tools make it easier to understand and work with massive amounts of data.

The most used data visualization platforms are: Grafana, Apache Superset, Kibana, Tableau, Power BI.

## Types of databases

### Relational database
In relational databases, each table stores information represented as attributes (columns) and tuples (rows). Each table has a primary key that uniquely identifies a record in the table. Foreign keys are references to a primary key in a different table.

This type of database should be used with structured data (rows and columns that clearly define data attributes) and when ACID properties (Atomicity, Consistency, Isolation, Durability) are required, but should not be used with big volumes of data because it doesn´t scale well.

Most used relational databases are: MySQL, PostreSQL, Oracle Database, Microsoft SQL Server.

### Columnar database
Columnar databases can utilize algorithms to simplify data retrievals. Compared with traditional databases, they don´t read billions of rows of data but only few long columns. They are usually used for analytics.

Most used columnar databases are: ClickHouse, Apache Cassandra, Amazon Redshift, Apache Druid, MariaDB.

### Document-oriented database
Document-oriented databases store and query data in JSON-like documents, simplifying management and improving reading speed. For example changing attribute of one item doesn´t affect other items.

The advantages of using a document-oriented database are: ease of development, flexible schema, performance at (horizontal) scale. They are usually used in unstructured data.

Most used document-oriented databases are: MongoDB, CouchDB.

### Time-Series database
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

## Query engines
A query engine is a piece of software that sits on top of a database or server and executes queries against data in that database or server to provide answers for users or applications. 

You can bring a query engine to your data instead of having to move your data somewhere else. A distributed SQL query engine will allow you to query data from a variety of data sources like Hadoop, AWS S3, NoSQL, MySQL, and more, or data from multiple data sources within a single query.

Examples of query engines include Presto, Apache Drill, Cloudera Impala, and Apache Spark.

###### Sources
- https://www.alluxio.io/learn/presto/query/

## Docker
Docker is an open platform for developing, shipping, and running applications. It provides the ability to package and run an application in a loosely isolated environment called a container.

### Docker compose
Docker Compose is a tool that helps you define and share multi-container applications. It is possible to create a YAML file to define the services and with a single command, spin everything up or tear it all down.

###### Sources
- https://docs.docker.com/guides/docker-overview/
- https://docs.docker.com/compose/



## Final thoughts

L'obiettivo di questo studio é stato quello di interfacciarsi con le varie componenti usate solitamente in una data platform, partendo dalla teoria e dalle definizioni, per avere un'idea delle tecnologie che si andranno ad usare, per evidenziare i motivi e i punti di forza per cui certe tecnologie sono predilette in quest'ambito, e infine per avere un confronto tra le possibili opzioni disponibili, fondamentale per la scelta delle tecnologie piú avanti.

I principali dubbi sorti durante questo studio riguardano il riuscire a distinguere e separare in modo chiaro le differenze tra ció che solitamente fanno i message-oriented middleware e gli event streaming platforms. Infatti nonostante esiste una definizione per ognuna, non appena ci si allontana dalla teoria e ci si avvicina alle tecnologie realmente utilizzate, si nota che la maggior parte possono intrecciare compiti e funzioni di entrambe le parti, possono specializzarsi solo in alcuni specifici ruoli o possono avere differenze sostanziali l'uno con l'altro per il modo con cui riescono a raggiungere lo stesso obiettivo.
Quindi piuttosto che cercare di separare i concetti e immaginare una distinzione chiara e ben definita, bisogna capire che quest'ultimi sono spesso sottogruppi di altri, o condividono solo parzialmente le caratteristiche di altri concetti, perció é importante comprendere a fondo il proprio caso d'uso e valutare ogni tecnologia singolarmente, per trovare quella piú adatta alla propria situazione.



# Data platform requirements

Prima di iniziare a valutare le varie tecnologie e metterle a confronto, mi sembra sensato andare a definire quali saranno i requisiti fondamentali della data platform, in modo da poter ricercare in futuro le caratteristiche piú adatte al mio caso d'uso nelle tecnologie selezionate, e poter escludere automaticamente quelle che non le rispecchiano.

In poche parole, la data platform prevede di raccogliere, monitorare ed analizzare i dati provenienti da un insieme di sensori delle stazioni di ricarica di auto elettriche.
Dei dati probabili che potrebbero essere inviati da questi sensori sono:
- Tempo di sosta di ogni veicolo per ogni parcheggio;
- Tempo di ricarica di ogni veicolo per ogni parcheggio;
- Transazione effettuata dall'utente.

Immagino quindi che i dati prodotti dai sensori potrebbero essere i seguenti:
```
# availability = 0 (available), 1 (occupied)
station_state = {"timestamp":12345678, "id":23, "availability":0}

# status = 0 (not recharging), 1 (recharging)
recharging_state = {"timestamp":12345678, "id":23, "status":0}

payment = {"timestamp":12345678, "id":23, "amount":100}
```

Solamente da questi 3 dati possiamo risalire a molte informazioni, per esempio:
- Percentuale di tempo in cui ogni stazione é disponibile od occupata, identificando quindi le stazioni piú profique;
- Tempo medio di occupazione delle stazioni;
- Durata media di ciascuna sessione di ricarica;
- Quantità di sessioni di ricarica completate in un intervallo di tempo;
- Entrate generate dalle sessioni di ricarica in un determinato periodo.

Bisogna inoltre tenere in considerazione che la storicizzazione dei dati dovrá essere permanente, anche per poter eseguire statistiche sul lungo periodo.


# Choice of technologies

## Grafana

Tra le varie data visualization platforms, la scelta si é concentrata tra Power BI, Tableau, Grafana e Kibana.
Nel mio caso l'opzione migliore sembra essere Grafana poiché supporta maggiormente i dati time-series, nonostante tutte fossero opzioni valide per il monitoraggio di dati IoT.

###### Sources
- https://www.linkedin.com/advice/0/what-best-data-visualization-tools-iot-skills-data-management-usrmc
- https://www.intuz.com/guide-on-best-data-visualization-tools-for-iot-apps
- https://logit.io/blog/post/top-grafana-dashboards-and-visualisations/
- https://www.reddit.com/r/grafana/comments/16b12dl/grafana_as_a_bi_tool/

## Apache Kafka

Dopo un'attento studio sulle event streaming platforms e sui message broker, ho deciso di optare per Kafka poiché sembra rispecchiare al meglio le esigenze del mio caso d'uso.
Grazie a Kafka é possibile infatti disaccoppiare le varie sorgenti dei dati dalle destinazioni in cui dovranno confluire, inserendosi come broker. É inoltre progettato per gestire grandi volumi di dati in streaming in modo efficiente, cosa che alcuni suoi concorrenti come RabbitMQ o NiFi potrebbero avere difficoltà a gestire. Altre opzioni invece, come Redpanda, non hanno un ecosistema maturo come quello di Kafka, il quale puó vantare anche un ottimo supporto dalla community.
Una valida alternativa sarebbe potuta essere Amazon Kinesis, ma non é open source come Kafka e i costi possono aumentare rapidamente con l'aumento del volume dei dati.
Un ulteriore vantaggio di Kafka é che permette di scalare orizzontalmente aggiungendo nuovi broker e partizioni.

###### Sources
- https://www.youtube.com/watch?v=DU8o-OTeoCc
- https://www.hellointerview.com/learn/system-design/deep-dives/kafka
- https://www.hellointerview.com/learn/system-design/answer-keys/ad-click-aggregator
- https://www.confluent.io/blog/event-streaming-platform-1/
- https://www.youtube.com/watch?v=Ch5VhJzaoaI
- https://www.youtube.com/watch?v=d1IzZLiBsy0
- https://www.confluent.io/blog/stream-processing-iot-data-best-practices-and-techniques/
- https://aws.amazon.com/compare/the-difference-between-rabbitmq-and-kafka/

## ClickHouse

Per la scelta del database sono state valutate diverse opzioni: InfluxDB, Prometheus, Timescale e Clickhouse.
Prometheus, nonostante sia una tecnologia spesso usata in questo ambito e spesso associata con Grafana, é stata esclusa poiché é stata pensata per una persistenza dei dati a breve termine, mentre nel nostro caso é necessaria una storicizzazione dei dati permanente, senza considerare che non é stata progettata per interagire direttamente con Kafka. Timescale é stato invece scartato poiché svolge bene operazioni semplici di monitoraggio, ma ci sono alternative migliori come Clickhouse che riescono a dare il meglio sia nel monitoraggio sia nella parte analitica dei dati.
InfluxDB rimane tutt'ora una valida opzione, ma in seguito a vari studi confronti sembra che Clickhouse sia superiore in termini di performance, senza dimenticare la sua compressione dei dati che é ottima nel caso in cui quest'ultimi dovranno essere mantenuti permanentemente.

###### Sources
- https://www.timestored.com/data/time-series-database-benchmarks#taxi-ride
- https://www.inf.unibz.it/~dignoes/res/pvldb2023-slides.pdf
- https://www.vldb.org/pvldb/vol16/p3363-khelifati.pdf
- https://www.metricfire.com/blog/grafana-data-sources/#Popular-Grafana-data-sources
- https://db-engines.com/en/system/ClickHouse%3BInfluxDB%3BPrometheus
- https://db-engines.com/en/ranking
- https://db-engines.com/en/ranking/time+series+dbms

## Apache Flink

La parte analitica dei dati richiede di eseguire operazioni complesse, ed effettuare query in tempo reale sul database potrebbe diventare inefficiente, perció é stato deciso di utilizzare Apache Flink per eseguire queste operazioni separatamente, prendendo i dati direttamente da Kafka e reinserendoli in quest'ultimo per fornire a ClickHouse dati giá elaborati.

###### Sources
- https://www.youtube.com/watch?v=anYQeoSbo5A
- https://www.youtube.com/watch?v=JfqoVuVDYUE


## Final thoughts

Nella scelta delle varie tecnologie é stato anche tenuto conto della sinergia tra loro, infatti tutte i vari componenti si supportano a vicenda in modo nativo.
In conclusione, la data platform gestirá i dati nel seguente modo:
- I dati provenienti dai sensori verranno inviati a Kafka, il quale si occuperá di separarli in code ordinate e di renderli disponibili sia a Clickhouse e sia a Flink;
- Flink gestirá l'elaborazione di operazioni complesse sui dati grezzi, per poi reinserirli nuovamente in Kafka;
- Clickhouse procederá a prelevare sia i dati grezzi e sia i dati elaborati da Flink;
- I dati verranno passati da Clickhouse a Grafana e quindi visualizzati.

![data_platform](https://github.com/user-attachments/assets/c2d28a55-8c47-4db7-ac5c-8789ffa415d7)