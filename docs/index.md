<p align="center">
  <img src="./assets/images/logo.png" height="250"/>
  <br/>
</p>

# Python Project Template

Python Project Template provides a ready-to-use structure for Python projects,
integrating best practices for code quality, testing and more. It helps developers start
new projects quickly with a maintainable and professional foundation.

!!! warning

    This template is configured for Linux x86_64 systems. For other platforms, you
    may need to adjust the `environments` and `required-environments` settings in
    `pyproject.toml`.

## Features

The template includes [Ruff](https://docs.astral.sh/ruff/) and
[Mypy](https://www.mypy-lang.org/) for linting and type checking, keeping code clean and
consistent. [Bandit](https://bandit.readthedocs.io/en/latest/) handles security scanning
to detect potential vulnerabilities, while
[Complexipy](https://rohaquinlop.github.io/complexipy/) identifies complex functions and
modules. Unit testing is covered by [Pytest](https://docs.pytest.org/en/stable/), and
documentation is automated with [MkDocs](https://www.mkdocs.org/) deployed via
[GitHub Pages](https://docs.github.com/en/pages). Finally,
[GitHub Actions](https://docs.github.com/en/actions) ties everything together by
automating linting, testing, and documentation deployment in CI/CD.

## Getting Started

Before starting, ensure that you have required Python installed and a virtual environment
set up. It is recommended to create an isolated environment to manage dependencies
cleanly. Additionally, ensure that [`uv`](https://github.com/astral-sh/uv) is installed
in your environment to handle grouped dependency installations.

**Generate Your Project** — Use Cookiecutter to create a new project from the template
and follow the prompts to configure project metadata, package name, and other options:

```bash
cookiecutter https://github.com/danibcorr/python-project-template.git
```

**Install Dependencies** — Activate your virtual environment and install all dependencies
using the included `Makefile`. This installs development, testing, and documentation
tools as defined in `pyproject.toml`:

```bash
make setup
```

**Run the Pipeline** — Execute the quality pipeline, which includes linting, type
checking, complexity checks, and test execution:

```bash
make pipeline
```

**Run the Full Workflow (Optional)** — To perform a complete setup including dependency
installation, full quality checks, and local documentation preview, ensuring that the
project environment is fully prepared for development and validation:

```bash
make all
```
