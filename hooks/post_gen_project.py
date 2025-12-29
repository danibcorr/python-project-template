import os
import shutil

from pathlib import Path

current_path = Path(os.getcwd())
parent_path = current_path.parent.absolute()

def remove(filepath) -> None:
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)
        
cookiecutter_prompts_folder: dict[str, str] = {
    'add_prompt_folder': 'prompt'
}

for cookiecutter_key, folder_name in folders_to_add.items():

    cookiecutter_var: str = '{{cookiecutter.' + f'{cookiecutter_key}' + '}}'
    add_folder: bool = cookiecutter_var == 'yes'
    
    if not add_folder:
        folder_path = os.path.join(
            parent_path, 
            '{{cookiecutter.project_name}}', 
            folder_name
        )

        remove(folder_path)
