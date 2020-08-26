#!/bin/bash

source venv/bin/activate
export FLASK_APP="weather_app/app.py"
export FLASK_DEBUG=1
HOST=${1:-127.0.0.1}
python -m flask run --host=$HOST
