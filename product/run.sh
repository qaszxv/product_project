#!/bin/bash

# Check if RabbitMQ and Elasticsearch are up and running before starting the service.

is_rabbitmq_ready() {
    eval "curl -I http://${RABBIT_HOST}:${RABBIT_PORT}"
}

i=0
while ! is_rabbitmq_ready; do
    i=`expr $i + 1`
    if [ $i -ge 10 ]; then
        echo "$(date) - rabbitmq still not ready, giving up"
        exit 1
    fi
    echo "$(date) - waiting for rabbimq to be ready"
    sleep 3
done

is_elasticsearch_ready() {
    eval "curl -I http://${ELASTICSEARCH_HOST}:${ELASTICSEARCH_PORT}"
}

i=0
while ! is_elasticsearch_ready; do
    i=`expr $i + 1`
    if [ $i -ge 10 ]; then
        echo "$(date) - elasticsearch still not ready, giving up"
        exit 1
    fi
    echo "$(date) - waiting for elasticsearch to be ready"
    sleep 3
done

# Run Service
nameko run product.service --backdoor 3000