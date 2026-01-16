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

- **Linting & Type Checking**: [Ruff](https://docs.astral.sh/ruff/) and
  [Mypy](https://www.mypy-lang.org/) for clean, consistent code.
- **Security Scanning**: [Bandit](https://bandit.readthedocs.io/en/latest/) detects
  potential vulnerabilities.
- **Code Complexity Analysis**: [Complexipy](https://rohaquinlop.github.io/complexipy/)
  identifies complex functions and modules.
- **Testing Suite**: Reliable unit testing with
  [Pytest](https://docs.pytest.org/en/stable/).
- **Auto Documentation**: [MkDocs](https://www.mkdocs.org/) +
  [GitHub Pages](https://docs.github.com/en/pages) for automated docs.
- **CI/CD**: [GitHub Actions](https://docs.github.com/en/actions) automates linting,
  testing, and documentation deployment.

And more.

## Getting Started

Before starting, ensure that you have required Python installed and a virtual environment
set up. It is recommended to create an isolated environment to manage dependencies
cleanly. Additionally, ensure that [`uv`](https://github.com/astral-sh/uv) is installed
in your environment to handle grouped dependency installations.

1. Generate Your Project

   Use Cookiecutter to create a new project from the template:

   ```bash
   cookiecutter https://github.com/danibcorr/python-project-template.git
   ```

   Follow the prompts to configure project metadata, package name, and other options.

2. Install Dependencies

   Activate your virtual environment and install all dependencies using the included
   `Makefile`:

   ```bash
   make setup
   ```

   This installs development, testing, and documentation tools as defined in
   `pyproject.toml`.

3. Run the Pipeline

   Execute the quality pipeline, which includes linting, type checking, complexity
   checks, and test execution:

   ```bash
   make pipeline
   ```

4. Run the Full Workflow (Optional)

   To perform a complete setup including dependency installation, full quality checks,
   and local documentation preview:

   ```bash
   make all
   ```

   This ensures that the project environment is fully prepared for development and
   validation.
