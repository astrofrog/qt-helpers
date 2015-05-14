import os
from setuptools import setup, Command


setup(name='qt-helpers',
      version='0.0.dev',
      url='http://glueviz.org',
      description='A common front-end to Python Qt libraries',
      author='Chris Beaumont, Thomas Robitaille',
      author_email='glueviz@gmail.com',
      packages=['qt_helpers'],
      keywords=['Scientific/Engineering'],
      classifiers=[
                   "Development Status :: 4 - Beta",
                   "Programming Language :: Python",
                   "License :: OSI Approved :: BSD License",
                  ]
     )