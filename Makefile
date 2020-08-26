SHELL := /bin/bash

.PHONY: all deploy

all: venv

venv: requirements.txt
	test -d venv || python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt
	touch venv

deploy: venv
	bin/run.sh

test: venv
	source venv/bin/activate && \
	pytest tests
