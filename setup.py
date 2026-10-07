from typing import List

from setuptools import setup,find_packages

def getRequirements():
    try:
        req_lst:List[str] = []
        with open('requirements.txt','r') as file:
            requirements = file.readlines()
            for requirement in requirements:
                requirement = requirement.strip('\n')
                if requirement and requirement != '-e .':
                    req_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found.")

setup(
    name='Network Security',
    version='0.0.1',
    author='Keshav Varshney',
    author_email='keshavvarshney2005@gmail.com',
    packages=find_packages(),
    install_requires=getRequirements()
)