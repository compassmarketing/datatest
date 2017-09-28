import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(name='datatest',
      version='1.0',
      description='Test tables of data',
      author='Ed Jaros',
      author_email='ejaros@cmsdm.com',
      packages=['datatest'],
      scripts=['scripts/datatest'],
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      install_requires=[
          'pandas',
          'numpy'
      ]
)
