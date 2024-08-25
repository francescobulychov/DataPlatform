
create table if not exists data_sensors (
    json String
) engine = Kafka settings
    kafka_broker_list = 'broker:19092',
    kafka_topic_list = 'charger-station-signals',
    kafka_group_name = 'clickhouse_group',
    kafka_format = 'JSONAsString';


-- parking sensor
create table if not exists parse_parking_sensor (
    timestamp DateTime,
    charger_id String,
    vehicle_detected Bool,
    plate String
) ENGINE = MergeTree()
order by timestamp;


create materialized view if not exists parking_sensor_consumer to parse_parking_sensor as
select
    toDateTime(JSONExtractString(json, 'timestamp')) as timestamp,
    JSONExtractString (json, 'charger_id') as charger_id,
    JSONExtractBool (json, 'vehicle_detected') as vehicle_detected,
    JSONExtractString (json, 'plate') as plate
from data_sensors
WHERE JSONHas(json, 'vehicle_detected');


-- user data sensor
create table if not exists parse_user_data_sensor (
    timestamp DateTime,
    charger_id String,
    user_id String,
    price Float32,
    user_connection Bool
) ENGINE = MergeTree()
order by timestamp;


create materialized view if not exists user_data_sensor_consumer to parse_user_data_sensor as
select
    toDateTime(JSONExtractString(json, 'timestamp')) as timestamp,
    JSONExtractString (json, 'charger_id') as charger_id,
    JSONExtractString (json, 'user_id') as user_id,
    JSONExtractFloat(json, 'price') as price,
    JSONExtractBool (json, 'user_connection') as user_connection
from data_sensors
WHERE JSONHas(json, 'user_id');


-- charger sensor
create table if not exists parse_charger_sensor (
    timestamp DateTime,
    charger_id String,
    recharging Bool,
    energy_delivered INTEGER
) ENGINE = MergeTree()
order by timestamp;


create materialized view if not exists charger_sensor_consumer to parse_charger_sensor as
select
    toDateTime(JSONExtractString(json, 'timestamp')) as timestamp,
    JSONExtractString (json, 'charger_id') as charger_id,
    JSONExtractBool (json, 'recharging') as recharging,
    JSONExtractInt (json, 'energy_delivered') as energy_delivered
from data_sensors
WHERE JSONHas(json, 'recharging');



-- flink transaction profit

create table if not exists transaction_profit (
    json String
) engine = Kafka settings
    kafka_broker_list = 'broker:19092',
    kafka_topic_list = 'transaction-profit',
    kafka_group_name = 'flink_group',
    kafka_format = 'JSONAsString';


create table if not exists parse_transaction_profit (
    charger_id String,
    user_id String,
    start_recharging DateTime,
    end_recharging DateTime,
    profit Float32
) ENGINE = MergeTree()
order by end_recharging;


create materialized view if not exists transaction_profit_consumer to parse_transaction_profit as
select
    JSONExtractString (json, 'charger_id') as charger_id,
    JSONExtractString (json, 'user_id') as user_id,
    toDateTime(JSONExtractString(json, 'start_recharging')) as start_recharging,
    toDateTime(JSONExtractString(json, 'end_recharging')) as end_recharging,
    JSONExtractFloat(json, 'profit') as profit
from transaction_profit
WHERE JSONHas(json, 'profit');