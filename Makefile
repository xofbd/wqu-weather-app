SHELL := /bin/bash

.PHONY: all deploy

all: venv

venv:
	python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt

deploy: venv
	source venv/bin/activate && \
	export FLASK_APP=app.py && \
	python -m flask run
