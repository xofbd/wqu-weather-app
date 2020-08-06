SHELL := /bin/bash

all: venv

venv: requirements.txt
	python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt

deploy: venv
	source venv/bin/activate && \
	export FLASK_APP=app.py && \
	python -m flask run
