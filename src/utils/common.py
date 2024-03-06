import os
import sys
import gzip
import yaml
import json
import logging
import joblib
import pandas as pd
from typing import Any
from pathlib import WindowsPath, Path
from box import ConfigBox
from ensure import ensure_annotations
from typing import Iterator, Dict, Any, Union, List
from box.exceptions import BoxValueError


# For Logging
logging_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logging_directory = "logs"
os.makedirs(logging_directory, exist_ok=True)
log_filepath = os.path.join(logging_directory, "running_logs.log")

logging.basicConfig(
    level=logging.INFO,  # set minimum log level to respond
    format=logging_format,  # set the log output format
    handlers=[
        logging.FileHandler(log_filepath),  # set file to write the log messages
        logging.StreamHandler(sys.stdout),  # send log messages to the system output
    ],
)  # set logging configuration

logger = logging.getLogger("sentiment-classifier-logger")  # get logger


# For Reading .json.gz data
@ensure_annotations
def parse(path: Path):
    """
    Parse data from .gz file

    Args:
        path (str): path of .gz file

    Yields:
        Iterator[Dict[str, Any]]: dictionary of containing data
    """
    g = gzip.open(path, "rb")
    for l in g:
        yield json.loads(l)

@ensure_annotations
def get_data_frame(path: Path) -> pd.DataFrame:
    """
    Read .gz file and convert to Pandas DataFrame

    Args:
        path (str): path of .gz file

    Returns:
        pd.DataFrame: dataset
    """
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient="index")


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
