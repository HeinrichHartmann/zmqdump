#
#
# Install with:
#
# $ sudo python setup.py install
#
# to install zmqdump with dependencies.
# Tested with pyzmq v. 14.0.1
#

from setuptools import setup

setup(name='zmqdump',
      version='0.1',
      description='Dump messages on zeromq socket.',
      author='Heinrich Hartmann',
      author_email='derhein@gmail.com',
      url='http://github.com/HeinrichHartmann/zmqdump',
      install_requires=[
          'pyzmq>=14.0.1'
      ],
      scripts=['zmqdump']
      )
