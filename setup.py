
import os
import sys

from setuptools import setup, find_packages
from ypconfig import __version__

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

major, minor = sys.version_info[:2]  # Python version

if major < 3:
    print("We need at least python 3")
    sys.exit(1)
elif major == 3:
    PYTHON3 = True
    try:
        import lib2to3  # Just a check--the module is not actually used
    except ImportError:
        print("Python 3.X support requires the 2to3 tool.")
        sys.exit(1)

setup(
    name='ypconfig',
    version=__version__,
    description='Tools required for ypconfig',
    author='Mark Schouten',
    author_email='mark@tuxis.nl',
    url='https://github.com/tuxis-ie/ypconfig',
    license='BSD 2-Clause',
    packages=find_packages(exclude=['tests', 'tests.*']),
    platforms=['linux'],
    data_files=[
    ],
    entry_points={'console_scripts': ['ypconfig = ypconfig.cli:main']}
)
