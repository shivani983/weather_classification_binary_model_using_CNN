import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s')

project_name = "ComputerVisionProject"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/prepare_base_model.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/evaluation.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_prepare_base_model.py",
    f"src/{project_name}/pipeline/stage_03_model_trainer.py",
    f"src/{project_name}/pipeline/stage_04_evaluation.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/model.ipynb",
    "templates/index.html",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir ,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok = True)
        logging.info(f"creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filename)==0): 
        with open(filepath,'w') as f:
            pass
        logging.info(f"creating empty file : {filename}")

    else:
        logging.info(f"{filename} is already created")        
