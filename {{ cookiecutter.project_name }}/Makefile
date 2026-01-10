.PHONY: setup \
		clean-cache-temp-files \
		lint code-check check-dead-code \
		tests \
		doc  \
		pipeline all

.DEFAULT_GOAL := all

SRC_PROJECT_NAME ?= {{ cookiecutter.project_module_name }}
SRC_PROJECT_TESTS ?= {{ cookiecutter.project_test_folder_name }}
SRC_PROJECT_NOTEBOOKS_FOLDER ?= notebooks

setup:
	@echo "Installing dependencies..."
	@uv sync --all-extras
	@uv run pre-commit install
	@echo "✅ Dependencies installed."

clean-cache-temp-files:
	@echo "Cleaning cache and temporary files..."
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type d -name .pytest_cache -exec rm -rf {} +
	@find . -type d -name .mypy_cache -exec rm -rf {} +
	@find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
	@echo "✅ Clean complete."

lint:
	@echo "Running lint checks..."
	@uv run isort $(SRC_PROJECT_NAME)/
	@uv run nbqa isort $(SRC_PROJECT_NOTEBOOKS_FOLDER)/
	@uv run ruff check --fix $(SRC_PROJECT_NAME)/
	@uv run ruff format $(SRC_PROJECT_NAME)/
	@uv run nbqa ruff $(SRC_PROJECT_NOTEBOOKS_FOLDER)/
	@echo "✅ Linting complete."

code-check:
	@echo "Running static code checks..."
	@uv run mypy $(SRC_PROJECT_NAME)/
	@uv run complexipy -f $(SRC_PROJECT_NAME)/
	@uv run bandit -r $(SRC_PROJECT_NAME)/ --exclude $(SRC_PROJECT_TESTS)
	@echo "✅ Code and security checks complete."

check-dead-code:
	@echo "Checking dead code..."
	@uv run deadcode $(SRC_PROJECT_NAME)
	@echo "✅ Dead code check complete."
	
tests:
	@echo "Running tests..."
	@uv run pytest $(SRC_PROJECT_TESTS)/
	@echo "✅ Tests complete."

doc:
	@echo "Serving documentation..."
	@uv run mkdocs serve

pipeline: clean-cache-temp-files lint code-check tests
	@echo "✅ Pipeline complete."

all: setup pipeline doc
	@echo "✅ All tasks complete."
