# `pyproject.toml` Configuration

## Overview

The `pyproject.toml` file serves as the central configuration hub for the project,
consolidating metadata, dependency management, and tool settings in a single,
standardized location. It follows the [PEP 621](https://peps.python.org/pep-0621/)
specification, which defines a uniform format for Python project metadata and facilitates
interoperability between tools. By leveraging `pyproject.toml`, the project achieves
modular dependency management, consistent tool behavior, and simplified setup for both
development and production environments.

## Build System: `[build-system]` Section

Defines the build backend used for packaging:

```toml
[build-system]
requires = ["uv_build>=0.9.18,<0.10.0"]
build-backend = "uv_build"
```

This configuration uses `uv_build` as the build backend, enabling fast and reliable
package building.

## Project Metadata: `[project]` Section

The `[project]` section defines fundamental information about the project:

```toml
[project]
name = "my-project"
version = "0.0.1"
description = "Project description"
authors = [{name = "Your Name", email = "your@email.com"}]
license = {file = "LICENSE"}
readme = "README.md"
requires-python = ">=3.11"
classifiers = [
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering",
    "Topic :: Software Development",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
]
keywords = ["python"]
```

These fields ensure that packaging tools, dependency managers, and documentation
generators can automatically retrieve key project information. The `classifiers` help
categorize the project on PyPI, while `keywords` improve discoverability.

## UV Configuration: `[tool.uv]` Section

Configures the UV package manager behavior:

```toml
[tool.uv]
default-groups = "all"
cache-keys = [{ file = "pyproject.toml" }, { git = { commit = true } }]
environments = [
    "sys_platform == 'linux'",
]
required-environments = [
    "sys_platform == 'linux' and platform_machine == 'x86_64'"
]
```

- `default-groups = "all"`: Installs all dependency groups by default.
- `cache-keys`: Defines cache invalidation triggers based on file changes and git
  commits.
- `environments`: Specifies supported platforms (Linux).
- `required-environments`: Restricts to Linux x86_64 architecture.

### UV Build Backend: `[tool.uv.build-backend]` Section

```toml
[tool.uv.build-backend]
module-name = "my_module"
module-root = ""
```

Configures the module name and root directory for the build backend.

## Dependency Management: `[dependency-groups]` Section

Dependencies are organized into logical groups, allowing selective installation based on
project requirements. This modular approach supports both development and production
workflows.

### `pipeline` Group: Development Tools

The `pipeline` group includes tools essential for code quality, testing, security, and
automation:

- `bandit`: Security analysis tool for detecting common vulnerabilities.
- `complexipy`: Measures cyclomatic complexity to identify potentially unmaintainable
  code.
- `mypy`: Static type checker to detect type inconsistencies.
- `pytest` and `pytest-order`: Frameworks for running unit tests and controlling test
  execution order.
- `ruff`: A high-performance linter and automatic formatter.
- `isort`: Sorts imports according to standard conventions.
- `deadcode`: Detects unused or unreachable code.
- `pre-commit`: Manages Git pre-commit hooks for automated checks.

### `documentation` Group: Documentation Tools

The `documentation` group contains tools for building and maintaining project
documentation:

- `mkdocs` and `mkdocs-material`: Static site generator and material design theme.
- `mkdocstrings[python]`: Generates API documentation directly from Python docstrings.
- `mkdocs-git-revision-date-localized-plugin`: Displays last update dates for pages.
- `mkdocs-git-authors-plugin`: Shows contributors for each page.
- `mkdocs-enumerate-headings-plugin`: Automatically numbers headings.
- `mkdocs-jupyter`: Integrates Jupyter notebooks into documentation.
- `mkdocs-awesome-nav`: Enhances navigation capabilities.
- `mike`: Provides versioned documentation management.

## Tool-Specific Configuration

### Ruff: `[tool.ruff]`

The Ruff linter is configured to enforce code style, detect errors, and simplify code:

```toml
[tool.ruff]
line-length = 88
indent-width = 4
exclude = [".venv", "build", "dist", ...]
extend-exclude = ["*.ipynb"]
```

- `line-length = 88`: Maximum line length following Black's convention.
- `indent-width = 4`: Standard Python indentation.
- `exclude`: Directories to ignore during linting.
- `extend-exclude`: Additional patterns to exclude (Jupyter notebooks).

#### Ruff Lint Rules: `[tool.ruff.lint]`

```toml
[tool.ruff.lint]
select = ["E", "F", "UP", "B", "SIM"]
ignore = ["E203"]
```

- `E`: Enforces PEP 8 style guidelines.
- `F`: Detects Pyflakes errors such as unused imports.
- `UP`: Applies modern Python syntax checks and upgrades.
- `B`: Detects common programming bugs.
- `SIM`: Suggests code simplifications to improve readability.
- `ignore = ["E203"]`: Ignores whitespace before ':' (conflicts with Black).

#### Ruff Docstring Style: `[tool.ruff.lint.pydocstyle]`

```toml
[tool.ruff.lint.pydocstyle]
convention = "google"
```

Enforces Google-style docstring conventions.

#### Ruff Formatter: `[tool.ruff.format]`

```toml
[tool.ruff.format]
quote-style = "double"
indent-style = "space"
line-ending = "auto"
docstring-code-format = true
docstring-code-line-length = 88
```

Configures automatic code formatting with double quotes, space indentation, and formats
code blocks within docstrings.

### Mypy: `[tool.mypy]`

Mypy performs static type checking, ensuring type safety and consistency:

```toml
[tool.mypy]
check_untyped_defs = true
ignore_missing_imports = true
exclude = ["^(build|dist|venv)", ".venv/"]
cache_dir = "/dev/null"
```

- `check_untyped_defs = true`: Validates functions even if type annotations are missing.
- `ignore_missing_imports = true`: Avoids errors for third-party modules without type
  stubs.
- `exclude`: Directories to skip during type checking.
- `cache_dir = "/dev/null"`: Disables caching to avoid stale cache issues.

### isort: `[tool.isort]`

isort enforces a standardized import order, improving code readability and
maintainability:

```toml
[tool.isort]
profile = "black"
known_first_party = ["my_module"]
sections = ["FUTURE", "STDLIB", "THIRDPARTY", "FIRSTPARTY", "LOCALFOLDER"]
import_heading_stdlib = "Standard libraries"
import_heading_thirdparty = "3pps"
import_heading_firstparty = "Own modules"
import_heading_localfolder = "Own modules"
line_length = 88
include_trailing_comma = true
combine_as_imports = true
skip_glob = [".venv/*", ".uv-cache/*"]
```

Imports are grouped as follows:

1. **FUTURE**: Future imports (`from __future__ import ...`).
2. **STDLIB**: Python standard library modules.
3. **THIRDPARTY**: External dependencies installed via package managers.
4. **FIRSTPARTY**: Modules developed within the current project.
5. **LOCALFOLDER**: Relative imports for local submodules or packages.

The configuration uses Black-compatible formatting with custom section headings for
better organization.

### deadcode: `[tool.deadcode]`

Detects unused code in the project:

```toml
[tool.deadcode]
exclude = [".venv", ".uv-cache", "tests"]
```

Excludes virtual environments and test directories from dead code analysis.
