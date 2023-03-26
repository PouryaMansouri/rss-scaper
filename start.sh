#!/bin/sh

cd /app/src

if [ $# -eq 0 ]; then
    echo "Usage: start.sh [PROCESS_TYPE](server)"
    exit 1
fi

PROCESS_TYPE=$1

if [ "$PROCESS_TYPE" = "server" ]; then
    python /app/src/manage.py migrate
    gunicorn \
        --reload \
        --bind 0.0.0.0:8000 \
        --workers 9 \
        --log-level DEBUG \
        --access-logfile "-" \
        --error-logfile "-" \
        --timeout 3600 \
        _core.wsgi
    # --worker-tmp-dir /dev/shm --threads=4 --worker-class=gthread
fi
