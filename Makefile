# Declare all phony targets
.PHONY: install clean doc pipeline all

# Default target
.DEFAULT_GOAL := all

# Install project dependencies
install:
	@echo "Installing dependencies..."
	@uv sync --all-extras
	@echo "✅ Dependencies installed."

# Clean cache and temporary files
clean:
	@echo "Cleaning cache and temporary files..."
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type d -name .pytest_cache -exec rm -rf {} +
	@find . -type d -name .mypy_cache -exec rm -rf {} +
	@find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
	@echo "✅ Clean complete."

# Serve documentation locally
doc:
	@echo "Serving documentation..."
	@uv run mkdocs serve

# Run code checks and tests
pipeline: clean
	@echo "✅ Pipeline complete."

# Run full workflow including install and docs
all: install pipeline doc
	@echo "✅ All tasks complete."
