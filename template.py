import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "wasteDetection"

# Directory structure for project components
directories = [
    ".github/workflows",
    "data",
    f"{project_name}",
    f"{project_name}/components",
    f"{project_name}/constant",
    f"{project_name}/constant/training_pipeline",
    f"{project_name}/entity",
    f"{project_name}/exception",
    f"{project_name}/logger",
    f"{project_name}/pipeline",
    f"{project_name}/utils",
    "templates"
]

# Files within project components
files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/logger/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# Combine directories and files
list_of_files = directories + files


def create_project_structure(list_of_files):
    """
    Automates the creation of project folder structure based on the provided list of file paths.

    Args:
        list_of_files (list): A list of file paths representing the desired project structure.

    Returns:
        None
    """
    for filepath in list_of_files:
        filepath = Path(filepath)

        # Ensure file paths are normalized for platform compatibility
        filepath = filepath.resolve()

        # Extract directory and filename
        filedir, filename = os.path.split(filepath)

        # Create directory if it doesn't exist
        if filedir != '':
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Created directory: {filedir} for the file {filename}")

        # Create empty file if it doesn't exist or is empty
        if not filepath.exists() or filepath.stat().st_size == 0:
            with open(filepath, "w"):
                pass
            logging.info(f"Created empty file: {filename}")
        else:
            logging.info(f"{filename} already exists")


# Call the create_project_structure function with list_of_files
create_project_structure(list_of_files)