import os
import subprocess
import sys

def create_venv(venv_name):
    if not os.path.exists(venv_name):
        os.makedirs(venv_name)
        subprocess.check_call([sys.executable, "-m", "venv", venv_name])
        print(f"Virtual environment '{venv_name}' created.")
    else:
        print(f"Virtual environment '{venv_name}' already exists.")
    print("To activate, run: source <venv_name>/bin/activate (Linux/Mac) or <venv_name>\Scripts\activate (Windows)")

# Example Usage
create_venv("my_project_venv")
