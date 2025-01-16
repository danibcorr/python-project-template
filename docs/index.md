# Python Project Template

Welcome to the **Python Project Template** repository! This template is designed to help you quickly set up a Python project with essential tools and best practices for code quality, testing, and deployment. Whether you’re starting a new project or looking to standardize your development workflow, this template provides a solid foundation.

For more details about the tools and configurations used in this project, see the [Content](./content/content.md) page.

## Features

- **Code Quality Tools**: Integrated with [Black](https://github.com/psf/black) for automatic code formatting, [Flake8](https://flake8.pycqa.org/en/latest/) for linting, and [Mypy](http://mypy-lang.org/) for static type checking.
- **Testing**: Built-in support for [Pytest](https://docs.pytest.org/en/stable/) for testing your Python code.
- **Documentation**: Uses [MkDocs](https://www.mkdocs.org/) for generating beautiful documentation websites, with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.
- **Deployment**: Easily deploys documentation to [GitHub Pages](https://pages.github.com/).

## Installation and Setup

Getting started with this project template is simple. Follow the steps below to set up your development environment and start using the template:

1. **Clone the repository:** First, clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/python-project-template.git
    cd python-project-template
    ```

2. **Install dependencies and set up the project:** This template includes a `Makefile` that automates the setup process, including installing dependencies and
   preparing the environment. To run the setup, simply execute:

    ```bash
    make
    ```

    This will:

    - Install necessary dependencies using Poetry.
    - Run linting, testing, and documentation tasks.

## Contributing

Feel free to fork this template and adapt it to your needs! Contributions are always welcome.
