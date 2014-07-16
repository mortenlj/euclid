#!/usr/bin/env python

__docformat__ = 'restructuredtext'

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(name='euclid-ng',
      version='0.1',
      description='2D and 3D vector, matrix, quaternion and geometry module',
      author='Morten Lied Johansen',
      author_email='mortenjo@ifi.uio.no',
      url='https://bitbucket.org/mortenlj/euclid/',
      py_modules=['euclid'],
      )

