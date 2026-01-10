.PHONY: setup \
		clean-cache-temp-files \
		lint code-check \
		doc  \
		pipeline all

.DEFAULT_GOAL := all

SRC_PROJECT_HOOKS ?= hooks

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
	@uv run isort $(SRC_PROJECT_HOOKS)/
	@uv run ruff check --fix $(SRC_PROJECT_HOOKS)/
	@uv run ruff format $(SRC_PROJECT_HOOKS)/
	@echo "✅ Linting complete."

code-check:
	@echo "Running static code checks..."
	@uv run mypy $(SRC_PROJECT_HOOKS)/
	@uv run complexipy -f $(SRC_PROJECT_HOOKS)/
	@uv run bandit -r $(SRC_PROJECT_HOOKS)/
	@echo "✅ Code and security checks complete."

doc:
	@echo "Serving documentation..."
	@uv run mkdocs serve

pipeline: clean-cache-temp-files lint code-check
	@echo "✅ Pipeline complete."

all: setup pipeline doc
	@echo "✅ All tasks complete."
