#!/bin/bash

function backupDB () {
  sudo docker exec $1 /usr/bin/mysqldump -u root --password=root $2 > ../backup/backup.sql
}

read -p "### Type CONTAINER ID: " container_id
read -p "### Type  DATABASE NAME: " database_name

backupDB $container_id $database_name

