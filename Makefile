SHELL := /bin/bash

.PHONY: all deploy

all: venv

venv: requirements.txt
	test -d venv || python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt
	touch venv

deploy: venv
	source venv/bin/activate && \
	export FLASK_APP="weather_app/app.py" && \
	python -m flask run

test: venv
	source venv/bin/activate && \
	pytest tests
