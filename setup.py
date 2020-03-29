#!/usr/bin/env python
# encoding: utf-8

from brc import VERSION
from distutils.core import setup

with open('requirements.txt') as f:
    reqs = f.read().strip().split('\n')

setup(name='brc',
      version=VERSION,
      install_requires=reqs,
      description='Brawlhalla Ranked Crawler',
      py_modules=['brc'],
      packages=['brc'],
      dependency_links=[],
)