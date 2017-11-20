"""Simple test class for evaluating data output by our business logic"""
import atexit
import datetime
import re
import sys
import pandas as pd

class DataTest(object):
    """class with test methods, constructed with result data
    expects a pandas dataframe in the contructor
    the data frame is expected to have an index"""

    def __init__(self, data_frame):
        self.data = data_frame

        if not isinstance(data_frame, pd.DataFrame):
            raise TypeError('input to test object was not a pandas.DataFrame')

        self.ids = set(self.data.index.tolist())
        self.checked_ids = []
        self.errors = []
        self.count = 0
        self.failed = 0
        self.finished = False

        atexit.register(self._warn_finish)

    def _warn_finish(self):
        if not self.finished:
            print 'ERROR: DataTest.finish() NOT CALLED: NO TEST OUTPUT SHOWN!'
            sys.exit(1)

    def equals(self, row_id, column, value):
        """test that the value at the given row, col index matches value"""
        self.count += 1
        self.checked_ids.append(row_id)

        found = self.data.at[row_id, column]
        if not found == value:
            self.failed += 1
            self.errors.append('''Bad value in %s at id: %s
                Expected %s
                Found %s\n''' % (column, row_id, value, found))

    def exists(self, row_id, column):
        """test that the value at the given row, col index exists"""
        self.count += 1
        self.checked_ids.append(row_id)

        if pd.isnull(self.data.loc[row_id, column]):
            self.failed += 1
            self.errors.append('''NULL value in %s at id: %s
                Expected a value to exist\n''' % (column, row_id))

    def not_exists(self, row_id, column):
        """test that the value at the given row, col index exists"""
        self.count += 1
        self.checked_ids.append(row_id)

        if not pd.isnull(self.data.loc[row_id, column]):
            self.failed += 1
            self.errors.append('''Non-NULL value found in %s at id: %s
                Expected no value to exist\n''' % (column, row_id))

    def date_in_range(self, row_id, column, range_start, range_end):
        """test that the value at the given row, col index matches regex"""
        self.count += 1
        self.checked_ids.append(row_id)

        if not isinstance(range_start, datetime.datetime):
            raise TypeError('input %s to date_in_range was not a datetime.datetime' % range_start)

        if not isinstance(range_end, datetime.datetime):
            raise TypeError('input %s to date_in_range was not a datetime.datetime' % range_end)

        found = self.data.at[row_id, column]
        if not range_start <= found <= range_end:
            self.failed += 1
            self.errors.append('''Date out of range found in %s at id: %s
                Expected date between %s and %s
                Found %s\n''' % (column, row_id, range_start, range_end, found))

    def matches(self, row_id, column, regex):
        """test that the value at the given row, col index in matches regex"""
        self.count += 1
        self.checked_ids.append(row_id)

        rex = re.compile(regex)

        found = self.data.at[row_id, column]
        if not isinstance(found, str):
            found = str(found)
        if not rex.match(found):
            self.failed += 1
            self.errors.append('''Bad format in %s at id %s:
                Expected to match %s
                Found %s\n''' % (column, row_id, regex, found))


    def matches_all(self, column, regex):
        """test that all values in the given column match regex"""
        self.count += 1
        rex = re.compile(regex)

        for i, row in self.data.iterrows():
            self.checked_ids.append(i)
            found = row[column]
            if not isinstance(found, str):
                found = str(found)
            if not rex.match(found):
                self.errors.append('''Bad format in %s:
                Expected to match %s
                Found %s\n''' % (column, regex, found))
                self.failed += 1
                break

    def finish(self):
        """ report errors and exit w/code """
        self.finished = True

        unchecked_ids = list(self.ids.difference(set(self.checked_ids)))
        unchecked_ids = map(str, unchecked_ids) # convert to string for priting
        if unchecked_ids:
            print 'WARNING: The following IDs were not tested at all: %s' % ' '.join(unchecked_ids)

        if self.errors:
            print 'ERROR: %d/%d tests failed:\n' % (self.failed, self.count)
            for err in self.errors:
                print err
            sys.exit(1)
        print 'OK: %d tests passed' % self.count
        sys.exit(0)
