from setuptools import setup
# https://towardsdatascience.com/create-your-own-python-package-and-publish-it-into-pypi-9306a29bc116


# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
print(this_directory)
long_description = (this_directory / "README.md").read_text()

setup(
    name='ner_metrics',
    version='0.1.2',    
    description='A simple Python snippets for NER evaluation',
    url='https://github.com/PL97/NER_eval',
    author='Le Peng',
    author_email='peng0347@umn.edu',
    license='MIT',
    packages=['ner_metrics'],
    install_requires=['numpy'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)