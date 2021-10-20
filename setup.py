from setuptools import setup

setup(
    name='x5gon_content_metadata_dataset',
    version='1.0',
    packages=['x5gon_content_metadata_dataset'],
    url='https://www.x5gon.org/',
    license='CC-BY-4.0',
    author='Sahan Bulathwela and Walid Ben Romdhane',
    author_email='m.bulathwela@ucl.ac.uk',
    description='This repository contains the metadata dataset extracted from X5GON repository with helper code to load the dataset into Python environments for data processing.',
    install_requires=[
        'numpy>=1.14.1',
        'pandas>=1.3.3']
)
