# 🐍 Python Project Template

Welcome to the **Python Project Template**! This template is designed to kickstart your
Python projects with essential tools for **code quality, security, complexity analysis,
testing, and deployment**. Whether you're starting fresh or looking to streamline your
development workflow, this template provides a solid foundation.

## 📰 Features

- **Code Quality**: Integrated tools like [ruff](https://docs.astral.sh/ruff/) and
  [Mypy](http://mypy-lang.org/) ensure clean, readable code.
- **Security**: Scan for vulnerabilities with
  [Bandit](https://bandit.readthedocs.io/en/latest/).
- **Code Complexity**: Analyze code complexity with
  [Complexipy](https://rohaquinlop.github.io/complexipy/).
- **Testing**: Built-in support for [Pytest](https://docs.pytest.org/en/stable/) to
  ensure your code works as expected.
- **Documentation**: Automatically generates documentation with
  [MkDocs](https://www.mkdocs.org/) and deploys it to
  [GitHub Pages](https://pages.github.com/).
- **CI/CD Pipeline**: Fully automated GitHub Actions for linting, testing, security
  checks, documentation build, and deployment.

## 🏗️ Installation and Setup

Setting up the environment is quick and easy. Just follow these steps:

### Clone the Repository

Clone the repo and navigate to the project folder:

```bash
git clone https://github.com/yourusername/python-project-template.git
cd python-project-template
```

### Activate Python Environment

Activate your Python virtual environment (depending on your OS and environment setup).

### Install Dependencies

Use the `Makefile` to automate the setup:

```bash
make
```

Alternatively, install dependencies manually:

```bash
pip install -r pyproject.toml
```

### Running the Full CI/CD Pipeline

To run the full pipeline (linting, testing, static analysis, security checks), execute:

```bash
make pipeline
```

To trigger a complete workflow (setup, cleanup, tests, documentation):

```bash
make all
```

### Documentation

Serve your project documentation locally with MkDocs:

```bash
make doc
```

This will start a local server to preview the docs.

## ⚙️ GitHub Actions CI/CD Workflow

Automated CI/CD workflow with GitHub Actions runs on `push` and `pull_request` events for
`main` and `dev` branches. It includes:

1. **Setup**: Installs dependencies and sets up the environment.
2. **Linting & Analysis**: Runs tools like `ruff`, `complexipy`, `mypy`, and `bandit`.
3. **Testing**: Runs tests with `pytest`.
4. **Build Docs**: Generates and serves the MkDocs site.
5. **Deploy Docs**: Deploys documentation to GitHub Pages.

The workflow configuration is found in `.github/workflows/ci-cd-pipeline.yml`.

### Deployment Conditions

Docs are deployed to GitHub Pages only for pull requests to the `main` or `dev` branches.

## 💛 Contributing

Feel free to fork and adapt this template! Contributions are always welcome. If you'd
like to contribute, open a pull request or issue.
