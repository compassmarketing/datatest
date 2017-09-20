""" unit tests for datatest module """
import pytest
import pandas as pd
import numpy as np
from datatest import DataTest

# pylint: disable=redefined-outer-name
# disable warning to allow re-use of pytest fixture
# without linter becoming upset
@pytest.fixture
def data_test():
    ''' return a DataTest over a small DataFrame '''
    data_frame = pd.DataFrame({'char':['a', 'b', 'c'], 'num':[3, 4, np.NaN]})
    _data_test = DataTest(data_frame)
    yield _data_test
    _data_test.finished = True

def test_consturct_without_df():
    """ ensure TypeError raised on bad constructor call """
    with pytest.raises(TypeError):
        DataTest("Not a dataframe")

def test_good_constructor(data_test):
    """ test that normal constructor call returns default DataTest """
    assert not data_test.errors
    assert data_test.count == 0
    assert data_test.failed == 0

def test_equals(data_test):
    """ test that equals function populated object correctly """
    data_test.equals(0, 'num', 3)
    assert not data_test.errors
    assert data_test.count == 1
    assert data_test.failed == 0

def test_not_equals(data_test):
    """ test that equals function populated object correctly """
    data_test.equals(0, 'num', 4)
    assert len(data_test.errors) == 1
    assert data_test.count == 1
    assert data_test.failed == 1

def test_exists(data_test):
    """ test that equals function populated object correctly """
    data_test.exists(1, 'num')
    data_test.exists(2, 'num')
    assert len(data_test.errors) == 1
    assert data_test.count == 2
    assert data_test.failed == 1

def test_not_exists(data_test):
    """ test that equals function populated object correctly """
    print data_test
    data_test.not_exists(2, 'num')
    data_test.not_exists(1, 'num')
    assert len(data_test.errors) == 1
    assert data_test.count == 2
    assert data_test.failed == 1

def test_matches(data_test):
    """ test that matches function populated object correctly """
    data_test.matches(0, 'char', r'[a-z]')
    assert not data_test.errors
    assert data_test.count == 1
    assert data_test.failed == 0

def test_not_matches(data_test):
    """ test that matches function populated object correctly """
    data_test.matches(1, 'num', r'\D')
    assert len(data_test.errors) == 1
    assert data_test.count == 1
    assert data_test.failed == 1

def test_matches_all(data_test):
    """ test that matches_all function populated object correctly """
    data_test.matches_all('char', r'[a-z]')
    assert not data_test.errors
    assert data_test.count == 1
    assert data_test.failed == 0

def test_not_matches_all(data_test):
    """ test that matches_all function populated object correctly """
    data_test.matches_all('num', r'\D')
    assert len(data_test.errors) == 1
    assert data_test.count == 1
    assert data_test.failed == 1
