from setuptools import setup

setup(
    name='nereval',
    version='0.1.0',    
    description='A simple Python snippets for NER evaluation',
    url='https://github.com/PL97/NER_eval',
    author='Le Peng',
    author_email='peng0347@umn.edu',
    license='MIT',
    packages=['nereval'],
    install_requires=['re',
                      'numpy',                     
                      'collections'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
    ],
)