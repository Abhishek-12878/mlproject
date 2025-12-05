from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    ''' 
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()  ##This could read the lines or librarys that we are write in the requirement.txt file
        requirements=[req.replace("\n","") for req in requirements] ##This could just move the next line to impliment sthe libraries

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Abhishek',
    author_email='puniaabhishek64@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)