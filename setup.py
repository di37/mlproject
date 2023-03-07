from setuptools import setup, find_packages

from typing import List

HYPEN_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements from a file.
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n", "") for requirement in requirements]

        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Isham Rashik",
    author_email="d.isham.ai93@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)