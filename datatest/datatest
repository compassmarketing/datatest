#!/usr/bin/env python
"""helper module for running tests"""
import os
import sys
import subprocess

def fancy_wrap(test_name):
    """ pad with lines of # """
    wrapper = ''
    wrapper = '#' * len(test_name) + wrapper
    wrapper = '\n%s\n' % wrapper
    return wrapper + test_name + wrapper

def check_wrap_run(test_name, _total_count):
    """ run and report for if file matches naming convetion """
    if not test_name.endswith('_datatest.py'):
        return 0
    print fancy_wrap(test_name)
    try:
        _total_count += 1
        subprocess.check_call(['python', test_name])
        return 0
    except subprocess.CalledProcessError:
        return 1

def run_tests():
    """ main function """
    _fail_count = 0
    _total_count = 0
    if len(sys.argv) > 1:
        for test_cand in sys.argv[1:]:
            _fail_count += check_wrap_run(test_cand, _total_count)
    else:
        # traverse ./testing/ directory, and execute all files ending in '_datatest.py'
        for root, _, files in os.walk("testing"):
            for test_cand in files:
                _fail_count += check_wrap_run(os.path.join(root, test_cand), _total_count)

    if _total_count < 1:
        print 'No tests found'
        sys.exit(1)

    sys.exit(_fail_count)

if __name__ == '__main__':
    run_tests()
