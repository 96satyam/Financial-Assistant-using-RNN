import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "financialAssistantRNN"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",         # LSTM/GRU model code
    f"src/{project_name}/components/model.py",
    f"src/{project_name}/utils/__init__.py",              # Helper functions
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",             # Config structure
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",           # Training + inference pipeline
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/predict_pipeline.py",
    f"src/{project_name}/entity/__init__.py",             # Entity classes if needed
    f"src/{project_name}/constants/__init__.py",          # Constant values
    "config/config.yaml",                                 # Data path, project config
    "params.yaml",                                        # Model hyperparameters
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",                              # Experiment + EDA
    "templates/index.html"                                # Web UI later (optional)
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
