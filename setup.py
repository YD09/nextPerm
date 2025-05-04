from setuptools import setup, find_packages

setup(
    name='nextperm',
    version='0.1.0',
    author='Yash Dhake ,Sayali ',
    author_email='dhakeyash123@gmail.com , varkhadesayali@gmail.com',
    description='A Python library for next permutation and combinatorial utilities inspired by C++ STL and Java Collections.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/YD09/nextPerm',  
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.6',
)
