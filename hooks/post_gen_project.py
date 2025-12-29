import os
import shutil
from pathlib import Path

project_dir = Path.cwd().parent / "{{ cookiecutter.project_name }}"

def remove(path: Path) -> None:
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)

folders = {
    "prompt": "{{ cookiecutter.add_prompt_folder }}",
}

for folder, enabled in folders.items():
    if enabled != "yes":
        remove(project_dir / folder)
