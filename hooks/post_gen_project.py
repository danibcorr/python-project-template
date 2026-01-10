import shutil
from pathlib import Path

project_dir = Path.cwd()

def remove(path: Path) -> None:
    """
    Removes a file or directory at the specified path.
    
    If the path points to a file, it is deleted. If it points to a
    directory, the entire directory tree is removed recursively.
    
    Args:
        path: The filesystem path to remove.
    
    Returns:
        None
    """
    
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)

folders: dict[str, str] = {
    ".devcontainer": "{{ cookiecutter.add_dev_container_folder }}",
    ".vscode": "{{ cookiecutter.add_vscode_folder }}",
    "notebooks": "{{ cookiecutter.add_notebooks_folder }}",
    "prompts": "{{ cookiecutter.add_prompts_folder }}",
}

for folder, enabled in folders.items():
    if enabled != "yes":
        remove(project_dir / folder)
