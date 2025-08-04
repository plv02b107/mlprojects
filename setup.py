from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements
    from the given requirements.txt file.
    '''
    with open(file_path) as file:
        requirements = [req.strip() for req in file.readlines()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlprojects',
    version='0.1.0',
    author='Pallvi',
    author_email='pallvi02b107@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
