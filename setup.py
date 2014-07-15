#!/usr/bin/env python

'''
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: setup.py 7 2006-08-14 16:36:11Z Alex.Holkner $'

from distutils.core import setup

setup(name='euclid-ng',
      version='0.1',
      description='2D and 3D vector, matrix, quaternion and geometry module',
      author='Morten Lied Johansen',
      author_email='mortenjo@ifi.uio.no',
      url='https://bitbucket.org/mortenlj/euclid/',
      py_modules=['euclid'],
      )

