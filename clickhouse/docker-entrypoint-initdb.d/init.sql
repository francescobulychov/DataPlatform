
create table if not exists data_sensors (
    json String
) engine = Kafka settings
    kafka_broker_list = 'broker:19092',
    kafka_topic_list = 'charger-station-signals',
    kafka_group_name = 'clickhouse_group',
    kafka_format = 'JSONAsString',
    kafka_poll_timeout_ms = 1000,
    kafka_max_block_size = 1;


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
    kafka_format = 'JSONAsString',
    kafka_poll_timeout_ms = 1000,
    kafka_max_block_size = 1;

create table if not exists parse_transaction_profit (
    charger_id String,
    user_id String,
    start_recharging DateTime,
    end_recharging DateTime,
    total_energy_delivered Float32,
    profit Float32
) ENGINE = MergeTree()
order by end_recharging;


create materialized view if not exists transaction_profit_consumer to parse_transaction_profit as
select
    JSONExtractString (json, 'charger_id') as charger_id,
    JSONExtractString (json, 'user_id') as user_id,
    toDateTime(JSONExtractString(json, 'start_recharging')) as start_recharging,
    toDateTime(JSONExtractString(json, 'end_recharging')) as end_recharging,
    JSONExtractFloat(json, 'total_energy_delivered') as total_energy_delivered,
    JSONExtractFloat(json, 'profit') as profit
from transaction_profit
WHERE JSONHas(json, 'profit');


-- flink occupied parking slots

create table if not exists total_occupied (
    json String
) engine = Kafka settings
    kafka_broker_list = 'broker:19092',
    kafka_topic_list = 'total-occupied',
    kafka_group_name = 'flink_group_occupied_counter',
    kafka_format = 'JSONAsString',
    kafka_poll_timeout_ms = 1000,
    kafka_max_block_size = 1;

create table if not exists parse_total_occupied (
    timestamp DateTime,
    occupied INTEGER
) ENGINE = MergeTree()
order by timestamp;


create materialized view if not exists total_occupied_consumer to parse_total_occupied as
select
    toDateTime(JSONExtractString(json, 'timestamp')) as timestamp,
    JSONExtractInt (json, 'occupied') as occupied
from total_occupied
WHERE JSONHas(json, 'occupied');


-- flink violations

create table if not exists violations (
    json String
) engine = Kafka settings
    kafka_broker_list = 'broker:19092',
    kafka_topic_list = 'violations',
    kafka_group_name = 'flink_group_violations',
    kafka_format = 'JSONAsString',
    kafka_poll_timeout_ms = 1000,
    kafka_max_block_size = 1;

create table if not exists parse_violations (
    charger_id String,
    user_id Nullable(String),
    plate String,
    start_parking DateTime,
    start_session Nullable(DateTime),
    end_session Nullable(DateTime),
    end_parking Nullable(DateTime),
    violation String
) ENGINE = MergeTree()
order by start_parking;

create materialized view if not exists violations_consumer to parse_violations as
select
    JSONExtractString (json, 'charger_id') as charger_id,
    JSONExtractString (json, 'user_id') as user_id,
    JSONExtractString (json, 'plate') as plate,
    toDateTime(JSONExtractString(json, 'start_parking')) as start_parking,
    toDateTimeOrNull(JSONExtractString(json, 'start_session')) as start_session,
    toDateTimeOrNull(JSONExtractString(json, 'end_session')) as end_session,
    toDateTimeOrNull(JSONExtractString(json, 'end_parking')) as end_parking,
    JSONExtractString (json, 'violation') as violation
from violations
WHERE JSONHas(json, 'violation');


-- flink full sessions

create table if not exists full_sessions (
    json String
) engine = Kafka settings
    kafka_broker_list = 'broker:19092',
    kafka_topic_list = 'full_sessions',
    kafka_group_name = 'flink_group_full_sessions',
    kafka_format = 'JSONAsString',
    kafka_poll_timeout_ms = 1000,
    kafka_max_block_size = 1;

create table if not exists parse_full_sessions (
    charger_id String,
    start_parking DateTime,
    plate String,
    start_session Nullable(DateTime),
    user_id Nullable(String),
    price Nullable(Float32),
    start_recharging Nullable(DateTime),
    energy_delivered Nullable(INTEGER),
    end_recharging Nullable(DateTime),
    end_session Nullable(DateTime),
    end_parking DateTime
) ENGINE = MergeTree()
order by end_parking;

create materialized view if not exists full_sessions_consumer to parse_full_sessions as
select
    JSONExtractString (json, 'charger_id') as charger_id,
    toDateTime(JSONExtractString(json, 'start_parking')) as start_parking,
    JSONExtractString (json, 'plate') as plate,
    toDateTimeOrNull(JSONExtractString(json, 'start_session')) as start_session,
    JSONExtractString (json, 'user_id') as user_id,
    JSONExtractFloat(json, 'price') as price,
    toDateTimeOrNull(JSONExtractString(json, 'start_recharging')) as start_recharging,
    JSONExtractInt (json, 'energy_delivered') as energy_delivered,
    toDateTimeOrNull(JSONExtractString(json, 'end_recharging')) as end_recharging,
    toDateTimeOrNull(JSONExtractString(json, 'end_session')) as end_session,
    toDateTimeOrNull(JSONExtractString(json, 'end_parking')) as end_parking
from full_sessions;


-- charger location

CREATE TABLE if not exists charger_location (
    charger_id String,
    latitude Float64,
    longitude Float64
) ENGINE = MergeTree()
ORDER BY (charger_id);

INSERT INTO charger_location (charger_id, latitude, longitude) 
VALUES ('charger-0', 45.464211, 9.191383), ('charger-1', 41.902783, 12.496366), ('charger-2', 40.851798, 14.268120), ('charger-3', 45.070339, 7.686864), ('charger-4', 43.769562, 11.255814), ('charger-5', 44.494887, 11.342616), ('charger-6', 40.712784, 14.012895), ('charger-7', 45.645238, 13.770655), ('charger-8', 39.223841, 9.121661), ('charger-9', 37.502669, 15.087269), ('charger-10', 45.816667, 8.816667), ('charger-11', 43.717022, 10.396619), ('charger-12', 45.676998, 13.750455), ('charger-13', 40.939979, 14.215834), ('charger-14', 40.416775, 15.091982), ('charger-15', 45.440847, 12.315515), ('charger-16', 45.406435, 11.876761), ('charger-17', 37.798852, 12.438497), ('charger-18', 38.115694, 13.361266), ('charger-19', 37.085742, 15.273263), ('charger-20', 44.698993, 10.629368), ('charger-21', 45.465421, 9.186351), ('charger-22', 42.638426, 12.674297), ('charger-23', 40.640063, 17.141835), ('charger-24', 41.121621, 16.869360), ('charger-25', 44.833338, 11.620512), ('charger-26', 40.850839, 14.268120), ('charger-27', 45.438759, 10.992650), ('charger-28', 41.141464, 16.855331), ('charger-29', 40.834978, 14.250649), ('charger-30', 45.805645, 9.083096), ('charger-31', 43.933201, 12.447680), ('charger-32', 45.157585, 10.791684), ('charger-33', 37.507877, 15.083030), ('charger-34', 40.178866, 18.169771), ('charger-35', 45.879208, 11.929402), ('charger-36', 44.418359, 12.203529), ('charger-37', 45.532689, 9.920080), ('charger-38', 41.253089, 13.606439), ('charger-39', 39.339399, 8.975089), ('charger-40', 38.132053, 15.650524), ('charger-41', 44.405650, 8.946256), ('charger-42', 40.851774, 14.268124), ('charger-43', 45.438611, 12.326667), ('charger-44', 46.066667, 11.116667), ('charger-45', 44.111488, 12.394236), ('charger-46', 43.722839, 10.401688), ('charger-47', 45.133333, 7.733333), ('charger-48', 45.464664, 9.188540), ('charger-49', 45.814121, 9.085176), ('charger-50', 40.827213, 14.035060), ('charger-51', 41.608634, 13.081963), ('charger-52', 43.212319, 13.303762), ('charger-53', 43.700936, 7.268391), ('charger-54', 45.221907, 11.690140), ('charger-55', 42.995602, 13.861454), ('charger-56', 43.769087, 11.255838), ('charger-57', 45.088017, 7.688010), ('charger-58', 40.732234, 14.003790), ('charger-59', 38.251234, 15.593222), ('charger-60', 41.008713, 14.355739), ('charger-61', 39.288798, 9.103395), ('charger-62', 41.125833, 16.869722), ('charger-63', 38.115556, 13.361111), ('charger-64', 44.011823, 12.611630), ('charger-65', 43.848667, 10.504484), ('charger-66', 45.160646, 10.797379), ('charger-67', 41.902916, 12.495067), ('charger-68', 42.073385, 14.121089), ('charger-69', 45.816739, 8.824979), ('charger-70', 40.678177, 17.946947), ('charger-71', 40.655448, 14.793078), ('charger-72', 44.692709, 10.630505), ('charger-73', 40.761375, 14.337454), ('charger-74', 43.766682, 11.255965), ('charger-75', 45.465421, 9.185924), ('charger-76', 41.892916, 12.482520), ('charger-77', 45.639228, 12.135198), ('charger-78', 37.774929, 15.056223), ('charger-79', 45.480519, 9.195293), ('charger-80', 38.907192, 16.594348), ('charger-81', 43.784874, 11.196102), ('charger-82', 41.238358, 13.575472), ('charger-83', 45.440198, 12.315289), ('charger-84', 45.848292, 9.391297), ('charger-85', 40.639339, 15.805867), ('charger-86', 37.774929, 15.056223), ('charger-87', 45.480519, 9.195293), ('charger-88', 41.903215, 12.495315), ('charger-89', 40.748876, 14.537888), ('charger-90', 45.665554, 8.761230), ('charger-91', 41.123650, 16.869860), ('charger-92', 38.788439, 15.236289), ('charger-93', 44.493671, 11.342636), ('charger-94', 40.848333, 14.269999), ('charger-95', 41.279284, 13.406029), ('charger-96', 45.043570, 10.214764), ('charger-97', 43.705092, 10.396885), ('charger-98', 38.148782, 13.581671), ('charger-99', 45.498952, 11.339181);
