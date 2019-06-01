#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-strava',
      version='0.0.1',
      description='Singer.io tap for extracting data from the Strava API',
      author='bsloane@gmail.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_strava'],
      install_requires=[
          'singer-python==5.2.1',
          'stravalib==0.10.2'
      ],
      entry_points='''
          [console_scripts]
          tap-strava=tap_strava:main
      ''',
      packages=['tap_strava'],
      include_package_data=True,
)
