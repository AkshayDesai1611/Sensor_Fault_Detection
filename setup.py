from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return all the requirements from requirements.txt

    """
    requirements_list:List[str] = []
    return requirements_list

setup(
    name = "sensor",
    version="0.0.1",
    author = "Akshay",
    author_email="mutalikdesai.akshay412@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements(),

)