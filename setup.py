from setuptools import find_packages, setup
## find_packages searches all folders having __init__.py and consider them as packages.
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requiremnts
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            #read lines from file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement = line.strip()
                #ignore the empty lines and ignore -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

# print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Amit A",
    author_email="2003.a.amit@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)

# -e . redirects to setup.py so after pip install -r requirements if we do -e . it goes to setup.py so we igonre for cycling
