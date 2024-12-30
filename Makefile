.PHONY: help venv install run

default: help

VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest
NOTEBOOK = $(VENV)/bin/jupyter-notebook

help:
	@echo "help"

venv:
	python -m venv $(VENV)
	echo "*" > $(VENV)/.gitignore

install:
	$(PIP) install -r requirements.txt

run:
	$(NOTEBOOK) --port 8000
