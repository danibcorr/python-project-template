.PHONY: setup \
		clean-cache-temp-files \
		format \
		lint code-check test \
		doc  \
		pipeline all

.DEFAULT_GOAL := all

PATH_PROJECT_ROOT ?= .
TEST_PATH ?= tests

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
	@uv run isort hooks tests
	@uv run ruff check --fix hooks tests
	@uv run ruff format hooks tests
	@echo "✅ Linting complete."

code-check:
	@echo "Running static code checks..."
	@uv run mypy $(PATH_PROJECT_ROOT)
	@uv run complexipy -f $(PATH_PROJECT_ROOT)
	@echo "✅ Code checks complete."

test:
	@echo "Running tests..."
	@uv run pytest $(TEST_PATH) -v
	@echo "✅ Tests complete."

format:
	@echo "Formatting documents..."
	@npx prettier --write .
	@echo "✅ Formatting complete."

doc:
	@echo "Serving documentation..."
	@uv run zensical serve

pipeline: clean-cache-temp-files format lint code-check test
	@echo "✅ Pipeline complete."

all: setup pipeline doc
	@echo "✅ All tasks complete."
