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
Delle probabili informazioni che potrebbe aver senso estrarre da questi sensori sono:
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


# Temperature monitor

La seguente applicazione di monitoraggio della temperatura é stata utile per prendere confidenza con le varie tecnologie utilizzate e per avere un punto di partenza per un progetto piú complesso.

## Docker Compose
É stato creato un file di docker compose per mettere assieme i tre servizi: Kafka, ClickHouse e Grafana.
Per quanto riguarda Kafka, ho utilizzato il file di esempio dalla [repo ufficiale](https://github.com/apache/kafka/blob/trunk/docker/examples/docker-compose-files/single-node/plaintext/docker-compose.yml), per ClickHouse ho seguito la guida del [docker hub](https://hub.docker.com/r/clickhouse/clickhouse-server/), mentre per Grafana é stata molto utile la [guida ufficiale](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/).

Una volta fatto ció, ho reso persistenti i volumi per ClickHouse e Grafana, in modo da mantenere i database, le configurazioni e le dashboard.
In questo caso é interessante notare che Grafana predilige le modifiche al file di configurazione tramite variabili dell'environment sul file di docker compose dove, per esempio, se la configurazione che vogliamo modificare é la seguente:
```
[dashboards]
min_refresh_interval = 1s
```
é possibile aggiungere l'omonima variabile:
```
GF_DASHBOARDS_MIN_REFRESH_INTERVAL=1s
```
ClickHouse invece prevede di aggiungere i file contenenti le modifiche della configurazione nelle seguenti cartelle:
```
/etc/clickhouse-server/config.d/
/etc/clickhouse-server/users.d/
```
e sará ClickHouse stesso a integrare ed applicare le modifiche secondo quanto detto nella loro [documentazione](https://clickhouse.com/docs/en/operations/configuration-files).

Sempre per quanto riguarda ClickHouse, é possibile aggiungere le query da eseguire durante l'inizializzazione del servizio nella cartella `docker-entrypoint-initdb.d` sotto forma di file .sql.

I servizi devono essere avviati tramite l'eseguibile run.sh, che é un semplice script che controlla l'esistenza di tutti i file e le cartelle necessarie al corretto funzionamento, e nel caso della loro assenza li crea. Dopodiché identifica l'utente corrente e imposta ogni utente di ogni servizio con quest'ultimo, per evitare ogni tipo di problema relativo ai permessi. Poiché lo script é stato scritto in bash, non supporta il sistema operativo Windows.

## From data generator to Kafka
Per generare dei dati ipotetici di un sensore di temperatura ho scritto un semplice script in python che, dopo aver generato un messaggio contenente il timestamp e un numero randomico tra 0 e 30, crea un producer per Kafka, specificando il `bootstrap_server` e il `topic` in questione (in questo caso topic-test), e invia i dati sotto forma di JSON rendendoli disponibili ad eventuali consumer in ascolto. Dopodiché continua ad inviare ogni secondo il timestamp e un nuovo valore che non si discosta piú di un numero dal valore precedente, in modo da poter visualizzare su Grafana un grafico piú realistico.
```
def get_temperature(i):

    if i == 0:
        return i + 1
    elif i == 30:
        return i - 1
    else:
        return random.choice([i-1, i+1])


def generate_data():

    producer = KafkaProducer(bootstrap_servers='broker:19092')
    celsius = random.randint(0, 30)

    while True:
        current_time = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S')
        celsius = get_temperature(celsius)

        new_message = dict(
            timestamp = current_time,
            celsius = celsius
        )

        producer.send(
            topic='topic-test',
            value=json.dumps(new_message).encode('utf-8')
        )
        print(f"[+] Generated temperature: {celsius}°C at {current_time}")
        time.sleep(1)

if __name__ == "__main__":
    generate_data()
```

## From Kafka to ClickHouse

Per fare in modo che una table di ClickHouse sia un consumer di Kafka é bastato configurare l'engine di quest'ultima nel seguente modo:
```
create table if not exists kafka_data (
    json String
) engine = Kafka settings
    kafka_broker_list = 'broker:19092',
    kafka_topic_list = 'topic-test',
    kafka_group_name = 'consumer-group-1',
    kafka_format = 'JSONAsString',
    kafka_poll_timeout_ms = 1000,
    kafka_max_block_size = 1
;
```
Le ultime due opzioni non erano strettamente necessarie per il corretto funzionamento, ma hanno permesso di ottenere i dati non appena disponibili per vederne la rappresentazione grafica istantaneamente.

In seguito é stata creata un'altra table collegata alla prima per estrarre i dati dal JSON e per poterla connettere a Grafana:
```
create table if not exists parse_data (
    timestamp DateTime,
    celsius INTEGER
) engine = MergeTree()
order by timestamp;

create materialized view if not exists consumer to parse_data as
select
    toDateTime(JSONExtractString(json, 'timestamp')) as timestamp,
    JSONExtractString (json, 'celsius') as celsius
from kafka_data;
```

## From ClickHouse to Grafana

Infine, grazie al rispettivo plugin, é stato aggiunto ClickHouse come sorgente di dati a Grafana ed é stata creata una dashboard che mostra l'andamento della temperatura e la media di quest'ultima.
![grafana_temperature_example](https://github.com/user-attachments/assets/01fb5137-b3d8-4b69-b874-094c4f52e5e4)

###### Sources
- https://hub.docker.com/r/apache/kafka
- https://github.com/apache/kafka/blob/trunk/docker/examples/docker-compose-files/single-node/plaintext/docker-compose.yml
- https://kafka.apache.org/quickstart
- https://needablackcoffee.medium.com/learn-apache-kafka-with-these-python-examples-454b5275109e
- https://dboostme.medium.com/befriend-python-kafka-clickhouse-in-10-minutes-216902b9deab
- https://hub.docker.com/r/clickhouse/clickhouse-server/
- https://clickhouse.com/docs/en/install
- https://clickhouse.com/docs/en/getting-started/quick-start
- https://clickhouse.com/docs/knowledgebase/kafka-to-clickhouse-setup
- https://clickhouse.com/docs/en/operations/configuration-files
- https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/


# Charger station data generator
Il generatore di dati di un'ipotetica colonnina di ricarica di auto elettriche é stato scritto in python e utilizza il multi-threading per simulare i dati di 100 colonnine di ricarica simultanemente, invocando la funzione `simulate_charging_station`.
```
if __name__ == "__main__":

    charger_ids = [f'charger-{i}' for i in range(1, 101)]

    threads = []
    for charger_id in charger_ids:
        thread = threading.Thread(target=simulate_charging_station, args=(charger_id,))
        threads.append(thread)
        thread.start()
```

Il generatore di dati é composto da 3 classi, dove ognuna rappresenta un sensore:
- `ParkingSensor`: simula il sensore di parcheggio che riconosce quando un veicolo viene posteggiato o quando abbandona il parcheggio, inviando inoltre i dati riguardanti la relativa targa.  

    É composto dai seguenti campi:
    - `timestamp`;
    - `charger_id`: stringa che identifica la colonnina di ricarica;
    - `vehicle_detected`: valore booleano che indica se un veicolo é posteggiato o meno;
    - `plate`: stringa che rappresenta la targa del veicolo in questione.

    É composto dai seguenti metodi:
    - `send_ParkingSensor_signal`: invocato ogni qualvolta che é necessario inviare il segnale;
    - `detect_vehicle`: invocato quando viene riconosciuto un veicolo, utile per cambiare lo stato di `vehicle_detected` da `False` a `True` e a generare una stringa randomica per la targa;
    - `detect_vehicle_leave`: invocato quando un veicolo abbandona il parcheggio, utile per cambiare lo stato di `vehicle_detected` da `True` a `False`.
```
class ParkingSensor:
    def __init__(self, charger_id):
        self.timestamp = get_timestamp()
        self.charger_id = charger_id
        self.vehicle_detected = False
        self.plate = None

    def send_ParkingSensor_signal(self):
        data = dict(
            timestamp = self.timestamp,
            charger_id = self.charger_id,
            vehicle_detected = self.vehicle_detected,
            plate = self.plate
        )
        print(f"[+] Sending parking sensor signal:\n {data}\n")

    def detect_vehicle(self):
        self.timestamp = get_timestamp()
        self.vehicle_detected = True
        self.plate = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        self.send_ParkingSensor_signal()
        
    def detect_vehicle_leave(self):
        self.timestamp = get_timestamp()
        self.vehicle_detected = False
        self.send_ParkingSensor_signal()
```

- `UserDataSensor`: simula il sensore che riconosce quando un utente, dopo aver parcheggiato il veicolo, si identifica alla colonnina tramite apposita app o tessera RFID e quando viene disconnesso.

    É composto dai seguenti campi:
    - `timestamp`;
    - `charger_id`: stringa che identifica la colonnina di ricarica;
    - `user_id`: stringa che identifica l'utente;
    - `price`: float che rappresenta il prezzo dell'energia EUR/kWh che l'utente pagherá nella sessione di ricarica. Per mantenere un valore realistico, quest'ultimo é compreso tra 0.40EUR e 0.99EUR, e che solitamente varia tra un utente e l'altro in base all'applicazione che usa o all'abbonamento a cui é registrato;
    - `user_connection`: valore booleano che indica se un utente é connesso o meno alla stazione di ricarica.

    É composto dai seguenti metodi:
    - `send_UserDataSensor_signal`: invocato ogni qualvolta che é necessario inviare il segnale;
    - `connect_user`: invocato quando un utente si connette alla colonnina, genera quindi una stringa randomica che identifica l'utente e un float randomico che rappresenta il prezzo dell'energia;
    - `disconnect_user`: invocato quando un utente si disconnette dalla colonnina.
```
class UserDataSensor:
    def __init__(self, charger_id):
        self.timestamp = get_timestamp()
        self.charger_id = charger_id
        self.user_id = None
        self.price = None
        self.user_connection = False

    def send_UserDataSensor_signal(self):
        data = dict(
            timestamp = self.timestamp,
            charger_id = self.charger_id,
            user_id = self.user_id,
            price = self.price,
            user_connection = self.user_connection
        )
        print(f"[+] Sending user data sensor signal:\n {data}\n")
    
    def connect_user(self):
        self.timestamp = get_timestamp()
        self.user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        self.price = round(random.uniform(0.40, 0.99), 2)
        self.user_connection = True
        self.send_UserDataSensor_signal()

    def disconnect_user(self):
        self.timestamp = get_timestamp()
        self.user_id = self.user_id
        self.price = self.price
        self.user_connection = False
        self.send_UserDataSensor_signal()
```

- `ChargerSensor`: simula il sensore connesso all'erogatore di energia, che quindi riconosce quando un veicolo viene collegato o scollegato e quanta energia deve essere emessa.

    É composto dai seguenti campi:
    - `timestamp`;ChargerSensor
    - `charger_id`: stringa che identifica la colonnina di ricarica;
    - `recharging`: valore booleano che rappresenta se il veicolo é collegato alla colonnina e quindi é possibile erogare energia;
    - `energy_delivered`: intero che indica quanta energia il veicolo connesso supporta e di conseguenza quanta energia in kW deve essere erogata.

    É composto dai seguenti metodi:
    - `send_ChargerSensor_signal`: invocato ogni qualvolta che é necessario inviare il segnale;
    - `start_recharging`: invocato quando un veicolo viene connesso alla colonnina di ricarica, genera quindi un valore randomico per la potenza in kW da erogare per il veicolo in questione;
    - `stop_recharging`: invocato quando il veicolo termina la ricarica e viene disconnesso dalla colonnina. Questo metodo invoca inoltre `UserDataSensor.disconnect_user()` per disconnettere automaticamente l'utente ed essere pronto ad una nuova sessione di ricarica.
```
class ChargerSensor:
    def __init__(self, charger_id):
        self.timestamp = get_timestamp()
        self.charger_id = charger_id
        self.recharging = False
        self.energy_delivered = 0

    def send_ChargerSensor_signal(self):
        data = dict(
            timestamp = self.timestamp,
            charger_id = self.charger_id,
            recharging = self.recharging,
            energy_delivered = self.energy_delivered
        )
        print(f"[+] Sending charger sensor signal:\n {data}\n")
    
    def start_recharging(self):
        self.timestamp = get_timestamp()
        self.recharging = True
        self.energy_delivered = random.randint(10, 30)
        self.send_ChargerSensor_signal()

    def stop_recharging(self, UserDataSensor):
        self.timestamp = get_timestamp()
        self.recharging = False
        self.energy_delivered = 0
        self.send_ChargerSensor_signal()

        UserDataSensor.disconnect_user()
```

La funzione principale `simulate_charging_station` permette di simulare un ipotetico traffico di dati dei sensori di una singola colonnina di ricarica, generando eventi randomici basati sulle probabilitá grazie alla funzione `probability_check` a cui viene passata la probabilitá in questione come parametro e la quale restituisce un valore booleano in base al successo o meno di questo evento.
```
def probability_check(probability):
    if random.random() < probability:
        return True
    return False
```

La funzione `simulate_charging_station` inizializza per prima cosa i vari sensori.
```
def simulate_charging_station(charger_id):

    parking_sensor = ParkingSensor(charger_id)
    user_data_sensor = UserDataSensor(charger_id)
    charger_sensor = ChargerSensor(charger_id)
```

Dopodiché entra in un loop in cui ogni secondo vengono generati i vari eventi, che sono i seguenti:
- Quando non sono presenti veicoli sul parcheggio, c'é il 30% di probabilitá ogni secondo che possa arrivare un nuovo veicolo;
```
# 30% probability of vehicle detection if no vehicle is detected
if not parking_sensor.vehicle_detected and probability_check(0.3):
    parking_sensor.detect_vehicle()
    continue
```
- Quando un veicolo é parcheggiato, c'é il 5% di probabilitá che quest'ultimo non usufruisca della colonnina di ricarica e vada via dopo poco, facendo cosí un'infrazione;
```
# 5% probability of vehicle not using the charger
if parking_sensor.vehicle_detected and probability_check(0.05):
    time.sleep(random.randint(5, 30))
    parking_sensor.detect_vehicle_leave()
    continue
```
- Quando un veicolo é parcheggiato, c'é il 95% di probabilitá che l'utente si connetta correttamente alla colonnina e inizi la sessione di ricarica. Dopodiché quest'ultima terminerá e l'utente verrá disconnesso.
```
# 95% probability of vehicle using the charger
if parking_sensor.vehicle_detected:
    time.sleep(random.randint(1, 3))
    user_data_sensor.connect_user()

    time.sleep(random.randint(1, 3))
    charger_sensor.start_recharging()

    time.sleep(random.randint(8, 10)) # 20, 40 change time

    charger_sensor.stop_recharging(user_data_sensor)
```
- Quando un utente ha finito la sessione di ricarica ma é sul parcheggio, c'é il 15% di probabilitá che rimanga sul parcheggio oltre il tempo limite, generando cosí un'infrazione;
```
# 15% probability of user not leaving for a while
if probability_check(0.15):
    time.sleep(random.randint(7, 10))
    parking_sensor.detect_vehicle_leave()
    continue
```
- Quando un utente ha finito la sessione di ricarica ma é sul parcheggio, c'é l'85% di probabilitá che abbandoni il parcheggio subito dopo aver ricaricato il veicolo.
```
# 85% probability of user leaving without extra time
time.sleep(random.randint(2, 5))
parking_sensor.detect_vehicle_leave()
continue
```

Ovviamente utilizzare tempistiche realistiche comporterebbe che ogni sessione di ricarica duri all'ancirca 40 minuti, perció i tempi simulati sono stati pesantemente abbreviati nel seguente modo:
- Sessione realistica (30min - 50 min):
    - 0s: arrivo dell'utente al parcheggio;
    - 2m: l'utente si identifica alla colonnina;
    - 1m: l'utente connette il proprio veicolo alla colonnina;
    - 20m-40m: sessione di ricarica del veicolo;
    - 5m: breve sosta al termine della ricarica.
- Sessione simulata (30sec - 50 sec):
    - 0s: arrivo dell'utente al parcheggio;
    - 2s: l'utente si identifica alla colonnina;
    - 1s: l'utente connette il proprio veicolo alla colonnina;
    - 20s-40s: sessione di ricarica del veicolo;
    - 5s: breve sosta al termine della ricarica.


# Apache Kafka
Dopo aver valutato diverse opzioni, ho deciso di usare Kafka inviando tutti i segnali ad un solo topic, il quale peró é suddiviso in molteplici partizioni, esattamente una per ogni colonnina di ricarica. Questo permette di garantire l'ordine dei messaggi all'interno di una singola partizione e quindi per ogni colonnina di ricarica, data l'importanza di mantenere l'ordine degli eventi. Un'altra ragione fondamentale dietro questa scelta é la semplicitá di poter consumare i dati e aggregarli per analisi specifiche.

L'idea sarebbe infatti quella di aggregare i dati con Apache Flink per creare un singolo record per ogni evento concluso, che inizia con l'arrivo del veicolo sul parcheggio e termina quando quest'ultimo lascia la postazione, in modo da avere le informazioni piú ordinate e sopratutto all'interno di una singola table da cui é possibile estrarre statistiche future piú facilmente. 

I dati verranno in ogni caso salvati anche cosí come sono per una questione di storicizzazione o per qualche caso specifico in cui é richiesto avere il dato immediatamente.

Questo approccio permette di aggiungere nuove colonnine semplicemente aggiungendo nuove partizioni al topic senza modificare la struttura esistente, poiché Kafka gestisce automaticamente il bilanciamento delle partizioni e garantisce la scalabilità orizzontale del sistema.

Un'eventuale introduzione futura di topic per ogni luogo geografico migliora ulteriormente la scalabilità. Ad esempio, si potrebbe creare un topic per ogni città, regione o paese, con partizioni dedicate alle colonnine all'interno di quella specifica area geografica.

## How it is implemeneted
La creazione del topic con le rispettive partizioni (una per ogni colonnina simulata) é stata gestita interamente sullo script in python che si occupa di generare i dati, sfruttando la libreria di python `kafka-python-ng`.

In questo caso é stato creato un topic chiamato `charger-station-signals` a cui sono state inizializzate 100 partizioni.  
Dopodiché é stato inizializzato anche il `producer` che verrá usato ogni qualvolta verrá inviato un messaggio a Kafka.
```
def kafka_setup():
    admin_client = KafkaAdminClient(bootstrap_servers='broker:19092', client_id='admin1')
    
    charger_station_topic = NewTopic(
        name='charger-station-signals',
        num_partitions=100,
        replication_factor=1
    )

    admin_client.create_topics([charger_station_topic])
    admin_client.close()

    global producer
    producer = KafkaProducer(bootstrap_servers='broker:19092')
```

Infine é stato creato un metodo `send_kafka` che si occupa di inviare il messaggio specificando:
- Nome del topic;
- Chiave da utilizzare, in questo caso il rispettivo `charger-id`;
- Il messaggio in questione in formato JSON;
- Numero della partizione a cui allocare il messaggio (`charger-0` allocato alla partizione 0 e cosí via).

```
def send_kafka(data):
    producer.send(
    topic='charger-station-signals',
    key=data['charger_id'].encode('utf-8'),
    value=json.dumps(data).encode('utf-8'),
    partition=int(data['charger_id'].split('-')[-1])
)
```