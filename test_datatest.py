""" unit tests for datatest module """
import pytest
import pandas as pd
from datatest import DataTest

@pytest.fixture
def data_test():
    ''' return a DataTest over a small DataFrame '''
    data_frame = pd.DataFrame({'char':['a', 'b'], 'num':[3, 4]})
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
    data_test.equals(1, 'num', 3)
    assert len(data_test.errors) == 1
    assert data_test.count == 1
    assert data_test.failed == 1

def test_matches(data_test):
    """ test that matches function populated object correctly """
    data_test.matches(0, 'num', r'\d')
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
    data_test.matches_all('num', r'\d')
    assert not data_test.errors
    assert data_test.count == 1
    assert data_test.failed == 0

def test_not_matches_all(data_test):
    """ test that matches_all function populated object correctly """
    data_test.matches_all('num', r'\D')
    assert len(data_test.errors) == 1
    assert data_test.count == 1
    assert data_test.failed == 1
