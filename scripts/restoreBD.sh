#!/bin/bash

function restoreDB () {
  cat ../backup/backup.sql | sudo docker exec -i $1 /usr/bin/mysql -u root --password=root $2
}

read -p "### Type CONTAINAR ID: " container_id
read -p "### Type DATABASE NAME: " database_name

restoreDB $container_id $database_name
