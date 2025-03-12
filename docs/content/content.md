# Project Files and Their Functions

This section explains the main files and their roles in the **Python Project Template**.

## `Makefile`

The `Makefile` automates common tasks:

- **install**: Installs or upgrades Poetry and project dependencies.
- **clean**: Removes `__pycache__` and `.pytest_cache` to clean up.
- **lint**: Runs code quality checks with Black, Mypy, and Flake8.
- **test**: Runs tests using [Pytest](https://docs.pytest.org/en/stable/).
- **wiki-up**: Serves documentation locally with MkDocs.
- **pre-commit**: Ensures code is clean and formatted before committing.
- **all**: Runs `clean`, `lint`, `test`, and `wiki-up` to prepare the project.

## `pyproject.toml`

This file configures Poetry and other tools like Black, Flake8, Mypy, and MkDocs:

- **Project Info**: Defines the project name, version, and description.
- **Dependencies**: Lists test, linting, and documentation dependencies like `pytest`,
  `black`, `flake8`, and `mkdocs`.
- **Black Configuration**: Sets line length to 89 characters and prevents string
  normalization (quote changes).
- **Flake8**: Configures line length, warnings to ignore, and which errors to check for.
- **Mypy**: Configures type checking options, including ignoring missing imports and
  treating optional types strictly.
- **Pylint**: Sets line length and disables specific warnings (e.g., duplicated code).
