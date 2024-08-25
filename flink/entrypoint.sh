#!/bin/bash

/opt/flink/bin/jobmanager.sh start-foreground &

sleep 10

python /opt/flink/jobs/transaction_profit.py &

wait