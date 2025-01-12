.PHONY: install clean lint test wiki-up pre-commit all

.DEFAULT_GOAL := all

SRC_PROJECT_NAME ?= src
SRC_TESTS ?= tests

install:
	@echo "Upgrading pip..."
	pip install --upgrade pip
	@echo "Installing poetry..."
	pip install poetry
	@echo "Installing dependecies with poetry..."
	poetry install

clean:
	@echo "Cleaning pycache..."
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +

lint:
	@echo "Checking Code Format with Black..."
	poetry run black --check $(SRC_PROJECT_NAME)/
	@echo "Checking Code Annotations with Mypy..."
	poetry run mypy $(SRC_PROJECT_NAME)/
	@echo "Checking Code Style and Quality with Flake8..."
	poetry run flake8 $(SRC_PROJECT_NAME)/

test:
	@echo "Runing PyTest Tests..."
	poetry run pytest $(SRC_PROJECT_NAME)/$(SRC_TESTS)/
	
wiki-up:
	@echo "Runing MkDocs..."
	mkdocs serve

pre-commit: clean lint test

all: clean lint test wiki-up