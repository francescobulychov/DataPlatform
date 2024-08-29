#!/bin/bash

/opt/flink/bin/jobmanager.sh start-foreground &

sleep 10

python /opt/flink/jobs/transaction_profit.py &
python /opt/flink/jobs/total_occupied.py &
python /opt/flink/jobs/detect_violations.py &

wait