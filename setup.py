from setuptools import setup, find_packages

VERSION = '0.0.4' 
DESCRIPTION = 'Package to certify variables'
LONG_DESCRIPTION = 'A python package designed to certify that variables are formatted as intended, and have the right contents'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="PyCertify", 
        version=VERSION,
        author="Ishan Jain",
        author_email="ishanjain0421@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'qol', 'validation', 'input'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)
