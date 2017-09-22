#!/usr/bin/env python2

from setuptools import setup

setup(name='datatest',
      version='1.0',
      description='Test tables of data',
      author='Ed Jaros',
      author_email='ejaros@cmsdm.com',
      packages=['datatest'],
      scripts=['scripts/datatest'],
      install_requires=[
          'pandas',
          'numpy',
      ],
     )
