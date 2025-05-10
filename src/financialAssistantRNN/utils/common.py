import os
from box.exceptions import BoxValueError
import yaml
from src.financialAssistantRNN import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML configuration file and return its content as a ConfigBox.

    Raises:
        ValueError: If the YAML file is empty or not valid.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            if not isinstance(content, dict):
                raise ValueError(f"YAML file is empty or not a valid mapping: {path_to_yaml}")

            logger.info(f"YAML file loaded successfully from: {path_to_yaml}")
            return ConfigBox(content)

    except BoxValueError as e:
        raise ValueError(f"BoxValueError while reading YAML: {e}")
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create directories if they do not exist.

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save data to a JSON file.

    Args:
        path (Path): File path
        data (dict): Data to be saved
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load data from a JSON file.

    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON loaded from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary data using joblib.

    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary data using joblib.

    Args:
        path (Path): File path

    Returns:
        Any: Loaded object
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in kilobytes.

    Args:
        path (Path): File path

    Returns:
        str: Size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
