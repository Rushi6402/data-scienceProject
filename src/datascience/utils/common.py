import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError



@ensure_annotations
def read_yaml(path_to_yaml:path) -> ConfigBox:
    """ reads yaml file and returns
    
    Aegs:
        path_to_yaml (str): path like input
    
    
    Raises:
       ValuError: if yaml file is empty 
       e: empty file
    
    Returns:
        ConfogBox: ConfigBox type
    """


    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("f:taml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def craete_directories(path_to_directories: list,verbose=True):
    """create list of directories
    Args:
        path_to_directories (list):list of path of directories
        ignore_log (bool , optional): ignore if multiple dirs is not be creates ,Defaults to
        """
    for  path  in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory st : {path}")

@ensure_annotations
def save_json(path: Path,data: dict):
    """save json data
    Args:
       path (path): path to json file
        data (dict): data to be saved in json file
    """
     
    with open (path, "w") as f:
        json.dump(data, f,index=4)
    
    logger.info(f"json  file saved at : {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """load json fie data
    
    Args
        path (Path ):path to json file
    
    
    Returns:
        ConfigBox: data as class attributes instead of dict
    """

    with open (path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any,path: Path) :
    """Save  binary file
    
    Args:
       data (Any ): data to be saved as binary
       path (path ): path to binary file
    """
    
   
    joblib.dump(value=data ,filename=path) 
    logger.info(f"Binary file saved successfully at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary file

    Args:
        path (Path): path to binary file

    Returns:
        Any: loaded object stored in the file 
    """

    data = joblib.load(path)
    logger.info(f"Binary file loaded successfully from: {path}")
    return data