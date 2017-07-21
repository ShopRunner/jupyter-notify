# -*- coding: utf-8 -*-


from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='jupyternotify',
    version='0.1.4',
    description='A Jupyter Notebook %%magic for Browser Notifications of Cell Completion',
    long_description=readme,
    author='Michelangelo D\'Agostino',
    author_email='mdagostino@shoprunner.com',
    url='https://github.com/shoprunner/jupyter-notify',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'jupyternotify': ['js/*.js']},
    install_requires=[
        'ipython',
        'jupyter'
    ]
)
