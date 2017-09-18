"""Simple test class for evaluating data output by our business logic"""
import re

PAL = {
    'ok': '\033[92m',
    'fail' : '\033[91m',
    'endc' : '\033[0m',
    'bold' : '\033[1m',
    }

class Test(object):
    """class wite test methods, constructed with result data"""

    def __init__(self, data_frame):
        self.data = data_frame
        self.errors = []
        self.count = 0
        self.failed = 0

    def equal(self, row_id, column, value):
        """test that the value at the given row, col index in mathces value"""
        self.count += 1

        found = self.data.at[row_id, column]
        if not found == value:
            self.failed += 1
            self.errors.append('''Bad value in %s at id: %s
                    Expected %s
                    Found %s\n''' % (column, row_id, value, found))

    def format(self, row_id, column, regex):
        """test that the value at the given row, col index in mathces format"""
        self.count += 1
        try:
            rex = re.compile(regex)
        except re.error:
            self.errors.append('Error compiling regex from %s')

        found = self.data.at[row_id, column]
        if not rex.match(self.data.at[row_id, column]):
            self.failed += 1
            self.errors.append('''Bad format in %s at id %s:
                Expected to match %s
                Found %s'\n''' % (column, row_id, regex, found))


    def format_all(self, column, regex):
        """test that all values in the given column mathce format"""
        self.count += 1
        try:
            rex = re.compile(regex)
        except re.error:
            self.errors.append('Error compiling regex from %s')

        for row in self.data.itertuples():
            found = getattr(row, column)
            if not rex.match(found):
                self.errors.append('''Bad format in %s at id %s:
                    Expected to match %s
                    Found %s\n''' % (column, getattr(row, 'Index'), regex, found))
                self.failed += 1
                break

    def finish(self):
        """ report errors and exit w/code """
        if self.errors:
            print PAL['fail'] + 'ERROR: %d/%d tests failed:\n' % \
            (self.failed, self.count) + PAL['endc']
            for err in self.errors:
                print err
            exit(1)
        print PAL['green '] + 'OK: %d tests passed' % self.count + PAL['endc']
        exit(0)
