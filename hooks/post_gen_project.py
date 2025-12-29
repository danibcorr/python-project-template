import os
import shutil
from pathlib import Path

project_dir = Path.cwd()

def remove(path: Path) -> None:
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)

folders = {
    ".devcontainer": "{{ cookiecutter.add_dev_container_folder }}",
    "notebooks": "{{ cookiecutter.add_notebooks_folder }}",
    "prompts": "{{ cookiecutter.add_prompts_folder }}",
}

for folder, enabled in folders.items():
    if enabled != "yes":
        remove(project_dir / folder)
