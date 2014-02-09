#
#
# Install with:
#
# $ sudo pip install -e ./
#
# to install zmqdump and dependencies.
# Tested with pyzmq v. 14.0.1
#

from distutils.core import setup

setup(name='zmqdump',
      version='0.1',
      description='Dump messages on zeromq socket.',
      author='Heinrich Hartmann',
      author_email='derhein@gmail.com',
      url='http://github.com/HeinrichHartmann/zmqdump',
      py_modules=['zmqdump'],
      install_requires=[
          'pyzmq'
      ]
      )
