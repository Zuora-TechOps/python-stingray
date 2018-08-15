import os
from setuptools import find_packages, setup
import sys

sys.path.insert(0, os.path.join(os.path.abspath(os.path.curdir), 'src'))
from stingray import __version__, __release__

name = 'python-stingray'

setup(name=name,
      version=__release__,
      description='Stingray Load Balancer REST API client module',
      long_description="""
Python module for interacting with the Stingray Load Balancer REST API.
""",
      url='https://github.com/Zuora-TechOps/python-stingray',
      author='Mark Troyer',
      author_email='disco@blackops.io',
      license='Apache',
      classifiers=[
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet :: Proxy Servers',
          'Topic :: System :: Networking',
      ],
      keywords='stingray zeus steelapp vtm riverbed brocade api',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      zip_safe=False,
      tests_require=[
          'pytest>=3.2.3',
          'pytest-responses>=0.3.0',
      ],
      install_requires=[
          'python-dateutil>=2.6.1',
          'requests>=2.18.1',
          'urllib3>=1.22',
      ],
      command_options={
          'build_sphinx': {
              'project': ('setup.py', name),
              'version': ('setup.py', __version__),
              'release': ('setup.py', __release__),
              'source_dir': ('setup.py', 'docs'),
              'build_dir': ('setup.py', 'docs/_build'),
              'config_dir': ('setup.py', 'docs'),
          }
      }
      )
