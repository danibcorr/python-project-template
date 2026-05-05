# Standard libraries
from importlib.metadata import version

__version__: str = version("{{ cookiecutter.project_name }}")
__all__: list[str] = ["__version__"]
