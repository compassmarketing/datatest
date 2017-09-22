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


## datatest
datatest is a helper script included with the datatest module which locates and executes tests.
Its behavior is as follows:
 - If no command line arguments are given, it recursively descends into ```./testing``` and calls python on all files ending with ```_datatest.py```
 - If command line arguments are given, it calls python on all arguments ending with ```_datatest.py```
 - In either case it prints the name of the file being executed padded with `#####` and its exit code is 0 if all tests pass, 1 (with a special message) if no tests are found, and the number of test files with errors in all other cases.

### example
consider the ```testing/`` directory of this repo.
its contents are as follows:
```
testing
├── error_datatest.py
└── ok_datatest.py
```

running ```datatest``` in the base directory of ths repo exits with code 1 and produces
```

#########################
testing/error_datatest.py
#########################

WARNING: The following IDs were not tested at all: j2 j3
ERROR: 3/6 tests failed:

Bad value in num at id: j1
                Expected 0
                Found 1

Bad format in num at id j1:
                Expected to match \D
                Found 1

Bad format in num at id j3:
                Expected to match [012]
                Found 3


######################
testing/ok_datatest.py
######################

OK: 7 tests passed
```

running ```datatest testing/ok_datatest.py``` exits with code 0 and produces
```

######################
testing/ok_datatest.py
######################

OK: 7 tests passed
```

running ```datatest fooBar.js``` exits with code 1 and produces
```

No tests found
```
