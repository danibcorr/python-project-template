.PHONY: setup \
		clean-cache-temp-files \
		lint code-check check-dead-code \
		tests \
		doc  \
		pipeline all

.DEFAULT_GOAL := all

SOURCE_PATH ?= {{ cookiecutter.project_module_name }}
TEST_PATH ?= {{ cookiecutter.project_test_folder_name }}
NOTEBOOKS_PATH ?= notebooks

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
	@uv run isort $(SOURCE_PATH)
	@uv run ruff check --fix $(SOURCE_PATH)
	@uv run ruff format $(SOURCE_PATH)
	@echo "✅ Linting complete."

code-check:
	@echo "Running static code checks..."
	@uv run mypy $(SOURCE_PATH)
	@uv run complexipy -f $(SOURCE_PATH)
	@uv run bandit -r $(SOURCE_PATH) --exclude $(TEST_PATH)
	@echo "✅ Code and security checks complete."

check-dead-code:
	@echo "Checking dead code..."
	@uv run deadcode $(SOURCE_PATH)
	@echo "✅ Dead code check complete."
	
tests:
	@echo "Running tests..."
	@uv run pytest $(TEST_PATH)
	@echo "✅ Tests complete."

doc:
	@echo "Serving documentation..."
	@uv run mkdocs serve

pipeline: clean-cache-temp-files lint code-check tests
	@echo "✅ Pipeline complete."

pre-commit: clean-cache-temp-files lint code-check
	@echo "✅ Pipeline pre-commit complete."

all: setup pipeline doc
	@echo "✅ All tasks complete."
