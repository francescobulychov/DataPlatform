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
