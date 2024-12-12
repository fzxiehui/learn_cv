.PHONY: help venv install 

default: help

VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest

help:
	@echo "help"

venv:
	python -m venv $(VENV)
	echo "*" > $(VENV)/.gitignore

install:
	$(PIP) install -r requirements.txt

