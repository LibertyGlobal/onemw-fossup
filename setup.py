# coding=utf-8
from setuptools import setup
import os


def readme():
    with open('README') as f:
        return f.read()

scripts = ['bin/fossup',]

data_files = [(os.environ['HOME'], ['etc/.fossuprc'])]

setup(name='fossup',
      version='0.1',
      description='Fossology Upload Tool',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD-3-Clause License',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.0'
      ],
      keywords='fossology fossup cp2foss',
      url='https://gitlab.com/toganlabs/fossup',
      author='Eilís Ní Fhlannagáin',
      author_email='pidge@toganlabs.com',
      license='BSD-3-Clause',
      data_files = data_files,
      scripts = scripts,
      install_requires=[
          'lxml==4.6.3', 'requests==2.25.1', 'bs4==0.0.1', 'requests-toolbelt==0.9.1',
      ],
      zip_safe=False)
