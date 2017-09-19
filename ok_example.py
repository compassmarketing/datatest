#!/usr/bin/env python2.7
""" simple demonstration of compass test class all passing"""

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
DATA_TEST.equals('j2', 'num', 2)
DATA_TEST.matches('j3', 'char', r'\D')
DATA_TEST.matches('j1', 'num', r'\d')
DATA_TEST.matches_all('char', '[a-z]')
DATA_TEST.matches_all('num', '[0-9]')
DATA_TEST.finish()
