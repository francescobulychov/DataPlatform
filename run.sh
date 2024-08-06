#!/bin/bash

dirs=(
    "./clickhouse/var/lib/clickhouse/"
    "./clickhouse/var/log/clickhouse-server/"
    "./clickhouse/docker-entrypoint-initdb.d/"
    "./clickhouse/etc/clickhouse-server/config.d/"
    "./clickhouse/etc/clickhouse-server/users.d/"
    "./grafana/var/lib/grafana/"
)

for dir in ${dirs[@]}; do

    if [ ! -d $dir ]; then
        mkdir -p $dir
    fi
done

files=(
    "./clickhouse/docker-entrypoint-initdb.d/init.sql"
    "./clickhouse/etc/clickhouse-server/config.d/docker_related_config.xml"
)

for file in ${files[@]}; do

    if [ ! -f $file ]; then
        file_name=$(basename $file)
        cp ./.backup_files/$file_name $file
    fi
done


if [ ! -f ".env" ]; then
    CURRENT_UID=$(id -u)
    CURRENT_GID=$(id -g)
    echo "CURRENT_UID=${CURRENT_UID}" > .env
    echo "CURRENT_GID=${CURRENT_GID}" >> .env
fi

docker compose up -d
