# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.rst') as r:
    readme = r.read()

with open('AUTHORS.txt') as a:
    # reSt-ify the authors list
    authors = ''
    for author in a.read().split('\n'):
        authors += '| '+author+'\n'

with open('LICENSE.txt') as l:
    license = l.read()

setup(
    name='jupyternotify',
    version='0.1.9',
    description='A Jupyter Notebook %%magic for Browser Notifications of Cell Completion',
    long_description=readme+'\n\n'+authors+'\nLicense\n-------\n'+license,
    author='Michelangelo D\'Agostino',
    author_email='mdagostino@shoprunner.com',
    url='https://github.com/shoprunner/jupyter-notify',
    license='BSD-3-Clause',
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'jupyternotify': ['js/*.js']},
    install_requires=[
        'ipython',
        'jupyter'
    ]
)
