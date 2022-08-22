import yaml 
from housing.exception import HousingException
import os, sys 

def read_yaml_file(file_path:str) -> dict:
    """_summary_

    Args:
        file_path (str): reads yaml file and returns the content as dictonary

    Returns:
        dict: file content 
        """

    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e ,sys) from e 