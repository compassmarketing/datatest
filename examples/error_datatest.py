""" simple demonstration of compass test class with errors """
import os
import sys
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))

from datatest import DataTest
import pandas as pd

TDF = pd.DataFrame({'char':['a', 'b', 'c'], 'num':[1, 2, 3]}, index=['j1', 'j2', 'j3'])

# print TDF
# produces
#    char  num
# j1    a    1
# j2    b    2
# j3    c    3

DATA_TEST = DataTest(TDF)
DATA_TEST.equals('j1', 'char', 'a')
DATA_TEST.equals('j1', 'num', 0) # this test fails
DATA_TEST.matches('j1', 'char', r'\D')
DATA_TEST.matches('j1', 'num', r'\D') # this test fails
DATA_TEST.matches_all('char', '[a-z]')
DATA_TEST.matches_all('num', '[012]') # this test fails
DATA_TEST.finish()
