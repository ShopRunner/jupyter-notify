# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.rst') as f, open('AUTHORS.txt') as a:
    readme = f.read()
    # reSt-ify the authors list
    authors = ''
    for author in a.read().split('\n'):
        authors += '| '+author+'\n'

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='jupyternotify',
    version='0.1.7',
    description='A Jupyter Notebook %%magic for Browser Notifications of Cell Completion',
    long_description=readme+'\n\n'+authors,
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
