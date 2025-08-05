"""
Unique source of truth for the version number.
"""

# Standard libraries
import importlib.metadata


__version__: str = importlib.metadata.version({{ cookiecutter.project_module_name }})