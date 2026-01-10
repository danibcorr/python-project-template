# `pyproject.toml` Configuration

## Overview

The `pyproject.toml` file serves as the central configuration hub for the project,
consolidating metadata, dependency management, and tool settings in a single,
standardized location. It follows the [PEP 621](https://peps.python.org/pep-0621/)
specification, which defines a uniform format for Python project metadata and facilitates
interoperability between tools. By leveraging `pyproject.toml`, the project achieves
modular dependency management, consistent tool behavior, and simplified setup for both
development and production environments.

## Project Metadata: `[project]` Section

The `[project]` section defines fundamental information about the project. This includes
the project name, version, description, author information, and the minimum supported
Python version. An example configuration is:

```toml
[project]
name = "my-project"
version = "0.0.1"
description = "Project description"
authors = [{name = "Your Name", email = "your@email.com"}]
requires-python = ">=3.11"
```

These fields ensure that packaging tools, dependency managers, and documentation
generators can automatically retrieve key project information. This metadata also
standardizes versioning and distribution across different environments.

## Dependency Management: `[dependency-groups]` Section

Dependencies are organized into logical groups, allowing selective installation based on
project requirements. This modular approach supports both development and production
workflows.

### `pipeline` Group: Development Tools

The `pipeline` group includes tools essential for code quality, testing, security, and
automation:

- `pytest` and `pytest-order`: Frameworks for running unit tests and controlling test
  execution order.
- `ruff`: A high-performance linter and automatic formatter.
- `mypy`: Static type checker to detect type inconsistencies.
- `bandit`: Security analysis tool for detecting common vulnerabilities.
- `complexipy`: Measures cyclomatic complexity to identify potentially unmaintainable
  code.
- `isort`: Sorts imports according to standard conventions.
- `nbqa`: Extends linting capabilities to Jupyter notebooks.
- `deadcode`: Detects unused or unreachable code.
- `pre-commit`: Manages Git pre-commit hooks for automated checks.

### `documentation` Group: Documentation Tools

The `documentation` group contains tools for building and maintaining project
documentation:

- `mkdocs` and `mkdocs-material`: Static site generator and material design theme.
- `mkdocstrings`: Generates API documentation directly from Python docstrings.
- `mkdocs-jupyter`: Integrates Jupyter notebooks into documentation.
- `mike`: Provides versioned documentation management.
- Additional plugins: Enhance navigation, metadata handling, and site functionality.

## Tool-Specific Configuration

### Ruff: `[tool.ruff]`

The Ruff linter is configured to enforce code style, detect errors, and simplify code
where possible:

```toml
[tool.ruff]
line-length = 88
indent-width = 4
select = ["E", "F", "UP", "B", "SIM"]
```

- `E`: Enforces PEP 8 style guidelines.
- `F`: Detects Pyflakes errors such as unused imports.
- `UP`: Applies modern Python syntax checks and upgrades.
- `B`: Detects common programming bugs.
- `SIM`: Suggests code simplifications to improve readability.

### Mypy: `[tool.mypy]`

Mypy performs static type checking, ensuring type safety and consistency:

```toml
[tool.mypy]
check_untyped_defs = true
ignore_missing_imports = true
```

- `check_untyped_defs = true`: Validates functions even if type annotations are missing.
- `ignore_missing_imports = true`: Avoids errors for third-party modules without type
  stubs, preventing unnecessary interruptions.

### isort: `[tool.isort]`

isort enforces a standardized import order, improving code readability and
maintainability. Imports are grouped as follows:

1. **STDLIB**: Python standard library modules.
2. **THIRDPARTY**: External dependencies installed via package managers.
3. **FIRSTPARTY**: Modules developed within the current project.
4. **LOCALFOLDER**: Relative imports for local submodules or packages.

This grouping ensures that import statements remain organized and easy to navigate,
facilitating collaboration across multiple developers and modules.
