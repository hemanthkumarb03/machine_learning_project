"""
As we run pip install -r requirements.txt, using setup py file we automate that step

"""
from setuptools import setup 
from typing import List



def get_requirements_list()->List[str]:
    """
    Description: This function is goin to retrun list of 
    Requirements mentioned in requirements.txt

    Returns:
        List[str]: _description_
    """
    with open(REQUIREMENTS_FILE_NAME) as f:
        return f.readlines()


#Declaring Variables for setup
PROJECT_NAME = 'housing-predictor'
VERSION = "0.0.1"
AUTHOR = 'Hemanth'
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = "My First Machine Learning Project",
    packages = PACKAGES ,
    install_requires = get_requirements_list()
)

