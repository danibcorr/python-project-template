# Declare all phony targets
.PHONY: install clean lint code_check tests doc pipeline all

# Default target
.DEFAULT_GOAL := all

# Variables
SRC_PROJECT_NAME ?= {{ cookiecutter.project_module_name }}
SRC_TESTS ?= {{ cookiecutter.project_test_folder_name }}

# Install project dependencies
install:
	@echo "Installing dependencies..."
	@uv pip install -r pyproject.toml --all-extras
	@echo "✅ Dependencies installed."

# Clean cache and temporary files
clean:
	@echo "Cleaning cache and temporary files..."
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type d -name .pytest_cache -exec rm -rf {} +
	@find . -type d -name .mypy_cache -exec rm -rf {} +
	@find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
	@echo "✅ Clean complete."

# Check code formatting and linting
lint:
	@echo "Running lint checks..."
	@uv run ruff format $(SRC_PROJECT_NAME)/ $(SRC_TESTS)/
	@uv run ruff check $(SRC_PROJECT_NAME)/ $(SRC_TESTS)/
	@uv run isort $(SRC_PROJECT_NAME)/ $(SRC_TESTS)/
	@echo "✅ Linting complete."

# Static analysis and security checks
code_check:
	@echo "Running static code checks..."
	@uv run mypy $(SRC_PROJECT_NAME)/ $(SRC_TESTS)/
	@uv run complexipy -d low $(SRC_PROJECT_NAME)/
	@uv run bandit -r $(SRC_PROJECT_NAME)/ --exclude $(SRC_TESTS)
	@echo "✅ Code and security checks complete."

# Test the code, only if the tests directory exists
tests:
	@echo "Checking if tests directory exists..."
	@if [ -d "$(SRC_TESTS)" ] && [ $$(find $(SRC_TESTS) -name "test_*.py" | wc -l) -gt 0 ]; then \
		echo "Running tests..."; \
		uv run pytest $(SRC_TESTS); \
		echo "✅ Tests complete."; \
	else \
		echo "No tests directory found or no test files. Skipping tests."; \
	fi

# Serve documentation locally
doc:
	@echo "Serving documentation..."
	@uv run mkdocs serve

# Run code checks and tests
pipeline: clean lint code_check tests
	@echo "✅ Pipeline complete."

# Run full workflow including install and docs
all: install pipeline doc
	@echo "✅ All tasks complete."
