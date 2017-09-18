#!/usr/bin/env python2.7
""" simple demonstration of compass test class """

from sys import argv

from compass_test import Test
import pandas as pd

TDF = pd.read_csv(argv[1], index_col=0)

T = Test(TDF)
T.equal('j1', 'char', 'a')
T.equal('j1', 'char', 'b')
T.format('j1', 'char', r'\d')
T.format('j1', 'char', r'\D')
T.format_all('char', '[a-z]')
T.finish()
