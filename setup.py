
import sys
import os


# Make sure we are running python3.5+
if 10 * sys.version_info[0] + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")


from setuptools import setup


def readme():
    print("Current dir = %s" % os.getcwd())
    print(os.listdir())
    with open('README.rst') as f:
        return f.read()

setup(
      name             =   'cni_challenge_on_chris',
      # for best practices make this version the same as the VERSION class variable
      # defined in your ChrisApp-derived Python class
      version          =   '0.1',
      description      =   'ChRIS plugin to create a Docker image to run on the CNI Challenge Test dataset',
      long_description =   readme(),
      author           =   'AWC',
      author_email     =   'aiwern.chung@childrens.harvard.edu',
      url              =   'http://wiki',
      packages         =   ['cni_challenge_on_chris'],
      install_requires =   ['chrisapp', 'pudb'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['cni_challenge_on_chris/cni_challenge_on_chris.py'],
      license          =   'MIT',
      zip_safe         =   False
     )
