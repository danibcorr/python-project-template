.PHONY: setup \
		clean-cache-temp-files \
		lint code-check test \
		doc  \
		pipeline all

.DEFAULT_GOAL := all

PATH_PROJECT_ROOT ?= .
PATH_TEST ?= tests

setup:
	@echo "Installing dependencies..."
	@uv sync --all-extras
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
	@uv run isort $(PATH_PROJECT_ROOT)
	@uv run ruff check --fix $(PATH_PROJECT_ROOT)
	@uv run ruff format $(PATH_PROJECT_ROOT)
	@echo "✅ Linting complete."

code-check:
	@echo "Running static code checks..."
	@uv run mypy $(PATH_PROJECT_ROOT)
	@uv run complexipy -f $(PATH_PROJECT_ROOT)
	@echo "✅ Code and security checks complete."

test:
	@echo "Running tests..."
	@uv run pytest $(PATH_TEST) -v
	@echo "✅ Tests complete."

doc:
	@echo "Serving documentation..."
	@uv run mkdocs serve

pipeline: clean-cache-temp-files lint code-check test
	@echo "✅ Pipeline complete."

all: setup pipeline doc
	@echo "✅ All tasks complete."
