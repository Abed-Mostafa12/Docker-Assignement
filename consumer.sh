#!/bin/bash
while true; do
  curl http://producer:5000/data >> /data/log.txt
  sleep 2
done
