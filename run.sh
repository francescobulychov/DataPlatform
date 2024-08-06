#!/bin/bash

dirs=(
    "./clickhouse/var/lib/clickhouse/"
    "./clickhouse/var/log/clickhouse-server/"
    "./clickhouse/docker-entrypoint-initdb.d/"
    "./grafana/var/lib/grafana/"
)

for dir in ${dirs[@]}; do

    if [ ! -d $dir ]; then
        mkdir -p $dir
    fi
done

if [ ! -f ".env" ]; then
    CURRENT_UID=$(id -u)
    CURRENT_GID=$(id -g)
    echo "CURRENT_UID=${CURRENT_UID}" > .env
    echo "CURRENT_GID=${CURRENT_GID}" >> .env
fi

docker compose up -d
