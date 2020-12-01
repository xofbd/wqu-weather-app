#!/usr/bin/env bash

if [[ -e venv ]]; then
    source venv/bin/activate
fi

export FLASK_APP="weather_app"
export FLASK_DEBUG=1
export DEPLOY=local

HOST=${1:-127.0.0.1}
python -m flask run --host=$HOST
