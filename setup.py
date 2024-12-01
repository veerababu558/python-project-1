from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='my_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=required,  # Include dependencies from requirements.txt
)
