# Python Project Template — Technical Documentation

## Overview

The **Python Project Template** offers a standardized, maintainable foundation for Python
projects, with integrated tooling for:

- Code quality enforcement
- Static analysis and security auditing
- Automated testing
- Documentation generation
- Development automation via Make and GitHub Actions

This template is intended to streamline development processes, promote consistency across
projects, and encourage best practices.

## Project Structure and Core Components

### `Makefile` – Automation of Common Development Tasks

The `Makefile` defines reusable commands to facilitate routine operations such as
installation, cleaning, linting, testing, and documentation. These tasks can be executed
using `make <target>`.

#### `make install`

Installs and upgrades the project’s dependencies using
[`uv`](https://github.com/astral-sh/uv), based on the `pyproject.toml` file. This
includes both development and documentation tools, organized by dependency groups.

#### `make clean`

Cleans the workspace by removing generated cache and temporary files, including:

- Python bytecode (`.pyc`, `.pyo`)
- Cache directories: `__pycache__`, `.pytest_cache`, `.mypy_cache`

This ensures a clean state for test and lint runs.

#### `make lint`

Formats and analyzes code using [Ruff](https://docs.astral.sh/ruff/):

- Automatically applies code formatting.
- Performs static lint checks on both source and test directories to ensure adherence to
  defined coding standards.

#### `make code_check`

Performs in-depth code analysis and security checks:

- **Mypy**: Validates static type annotations.
- **Complexipy**: Analyzes code complexity to identify overly complicated logic
  structures.
- **Bandit**: Detects common security issues in Python code.

This step is essential for maintaining robust, secure, and maintainable codebases.

#### `make tests`

Executes the project's unit tests using [Pytest](https://docs.pytest.org/en/stable/). If
no tests or test files are detected, the command exits gracefully without failure.

#### `make doc`

Serves the documentation locally using [MkDocs](https://www.mkdocs.org/). This allows for
live previews of your documentation before deployment.

#### `make pipeline`

Runs a full quality pipeline comprising:

- Environment cleanup
- Code linting and formatting
- Static analysis and security scans
- Test execution

This target is suitable for continuous integration environments and pre-release
validations.

#### `make all`

Performs a complete workflow:

- Installs dependencies
- Executes the full quality pipeline
- Builds and serves the documentation

Recommended for initial setup and full-cycle verifications.

## `pyproject.toml` – Centralized Project Configuration

The `pyproject.toml` file defines the project's metadata, dependency groups, and tool
configurations in accordance with modern Python standards.

### `[project]`

Specifies metadata such as:

- Project name, version, and description
- Python version compatibility
- Required runtime dependencies (if any)

This section aligns with PEP 621 standards for project metadata.

### `[dependency-groups]`

Organizes development dependencies into logical groups:

- **`pipeline`**: Tools used for static analysis, linting, security checks, complexity
  analysis, and testing:

  - `pytest`, `pytest-order`, `ruff`, `mypy`, `bandit`, `complexipy`

- **`documentation`**: Tools used to build and extend project documentation with MkDocs
  and various plugins:

  - `mkdocs-material`, `mkdocstrings`, `mkdocs-jupyter`, etc.

These groups allow selective installation via `uv`, improving modularity and dependency
management.

### `[tool.ruff]`

Defines configuration for **Ruff**, the linter and code formatter:

- Line and indentation style
- Linting rules to enforce (e.g., error detection, unused imports, code simplifications)
- Excluded directories (e.g., `venv`, `dist`, `.pytest_cache`, `.ipynb_checkpoints`)
- Formatting settings for docstrings and imports

### `[tool.mypy]`

Configures **Mypy**, the static type checker:

- Enables checks on untyped function definitions
- Ignores unresolved imports (helpful for missing stubs)
- Excludes irrelevant directories such as build environments

These settings help detect type-related issues early in the development process.

## Development Workflow

A typical development and validation workflow using this template may include the
following steps:

1. **Setup**

   ```bash
   make install
   ```

2. **Clean Environment**

   ```bash
   make clean
   ```

3. **Code Linting and Analysis**

   ```bash
   make lint
   make code_check
   ```

4. **Run Tests**

   ```bash
   make tests
   ```

5. **Generate and Preview Documentation**

   ```bash
   make doc
   ```

6. **Full Workflow Execution**

   ```bash
   make all
   ```

These commands can be used locally or integrated into CI/CD pipelines for automated
validation.
