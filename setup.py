from setuptools import find_packages,setup
from typing import List


exp = '-e .'
def get_requirements(file_path:str)->List[str]:

    '''
        retruns a requirements in our requirements.txt file
    '''
    req = []  # requirements list

    with open(file_path) as fp:
        req = fp.readlines()
        req = [r.replace('\n',' ') for r in req]

        if exp in req:
            req.remove(exp)

    return req


setup(

    name='mlproject',
    version='0.0.1',
    author='Naga Tharun',
    author_email='nagatharun.movva@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),

)