#!/usr/bin/env python2.7
""" simple demonstration of compass test class all passing"""

from datetime import datetime
from datatest import DataTest
import numpy as np
import pandas as pd

TDF = pd.DataFrame(
    {
        'char':['a', 'b', 'c', 'd'],
        'num':[1, 2, 3, np.NaN],
        'date':['2017-01-01', '2017-05-15', '2017-08-15', '2017-12-31']
        },
    index=['j1', 'j2', 'j3', 'j4']
    )

TDF['date'] = pd.to_datetime(TDF['date'])

# print TDF
# produces
#    char       date  num
# j1    a 2017-01-01  1.0
# j2    b 2017-05-15  2.0
# j3    c 2017-08-15  3.0
# j4    d 2017-12-31  NaN

DATA_TEST = DataTest(TDF)
DATA_TEST.equals('j1', 'char', 'a')
DATA_TEST.equals('j2', 'num', 2)
DATA_TEST.matches('j3', 'char', r'\D')
DATA_TEST.matches('j1', 'num', r'\d')
DATA_TEST.matches_all('char', '[a-z]')
DATA_TEST.not_exists('j4', 'num')
DATA_TEST.date_in_range('j2', 'date',
                        datetime.strptime('2017-01-14', '%Y-%m-%d'),
                        datetime.strptime('2017-09-16', '%Y-%m-%d')
                       )
DATA_TEST.finish()
