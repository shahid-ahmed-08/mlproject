from setuptools import find_packages,setup
from typing import List

hyphen_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this fuunction will retuen the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if hyphen_dot in requirements:
            requirements.remove(hyphen_dot)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Shahid',
    author_email='shahid91309@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)