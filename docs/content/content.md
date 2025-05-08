# Python Project Template Documentation

## Overview

The **Python Project Template** provides an easy setup for Python projects with built-in tools for code quality, security, testing, and documentation. It automates tasks and creates a consistent project structure.

## Project Files and Functions

### `Makefile`

* **`install`**: Installs and upgrades dependencies using `uv` and `pyproject.toml`.
* **`clean`**: Removes cache files (`__pycache__`, `.pytest_cache`, etc.).
* **`lint`**: Runs code checks (Black, Mypy, Flake8, Pylint).
* **`test`**: Runs tests with [Pytest](https://docs.pytest.org/en/stable/).
* **`wiki-up`**: Serves documentation locally using [MkDocs](https://www.mkdocs.org/).
* **`pre-commit`**: Runs quality checks before committing.
* **`all`**: Runs `clean`, `lint`, `test`, and `wiki-up`.

### `pyproject.toml`

Defines project settings and dependencies:

* **`[project]`**: Project metadata.
* **`[tool.uv]`**: Defines default dependency groups.
* **`[dependency-groups]`**: Groups dependencies for tasks (e.g., `pipeline`, `documentation`).
* Tool configurations for Black, Flake8, Mypy, and Pylint.