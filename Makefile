.PHONY: setup \
		clean-cache-temp-files \
		doc \
		pipeline all

.DEFAULT_GOAL := all

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

doc:
	@echo "Serving documentation..."
	@uv run mkdocs serve

pipeline: clean-cache-temp-files
	@echo "✅ Pipeline complete."

all: setup pipeline doc
	@echo "✅ All tasks complete."
