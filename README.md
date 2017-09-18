# datatest

dataetst is a python library to be used in verifying output from out business processes.

datatest exports a single class ```datatest.DataTest``` which expects a ```pandas.DataFrame``` in its constructor.
```datatest.DataTest``` exposes four methods:
 * ```equals(row_id, column, value)``` - tests that the value at the given row, col index is of the same type and equal to the input value
 * ```matches(row_id, column, regex)``` - tests that the value at the given row, col index matches regex
 * ```matches_all(column, regex)``` - tests that all values in the given column match regex
 * ```finish()``` - report errors and exit with appropriate status code

```DataTest.finish()``` __must__ be called to recieve the test reporting and error code. The module will complain loudly if a test exits before ```DataTest.finish()``` is called.

### Example Usage
the script
```python
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
```
would show output:
```
ERROR: 1/5 tests failed:

Bad value in num at id: j1
                Expected 0
                Found 1

```
the script
```python
#!/usr/bin/env python2.7
""" simple demonstration of compass test class """

from datatest import DataTest
import pandas as pd

TDF = pd.DataFrame({'char':['a', 'b', 'c'], 'num':[1, 2, 3]}, index=['j1', 'j2', 'j3'])

DATA_TEST = DataTest(TDF)
DATA_TEST.equals('j1', 'char', 'a')
DATA_TEST.equals('j1', 'num', 1) # this test passes 
DATA_TEST.matches('j1', 'char', r'\D')
DATA_TEST.matches('j1', 'num', r'\d')
DATA_TEST.matches_all('char', '[a-z]')
DATA_TEST.finish()
```
would show output:
```
OK: 5 tests passed
```
