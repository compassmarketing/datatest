#!/usr/bin/env python2.7
""" simple demonstration of compass test class """

from datatest import DataTest
import pandas as pd

TDF = pd.DataFrame({'char':['a', 'b', 'c'], 'num':[1, 2, 3]}, index=['j1', 'j2', 'j3'])

DATA_TEST = DataTest(TDF)
DATA_TEST.equals('j1', 'char', 'a')
DATA_TEST.equals('j1', 'num', 0) # this test fails
DATA_TEST.matches('j1', 'char', r'\D')
DATA_TEST.matches('j1', 'num', r'\d')
DATA_TEST.matches_all('char', '[a-z]')
DATA_TEST.finish()
