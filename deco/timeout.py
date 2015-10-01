#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: timeout.py 98 2014-01-11 10:09:59Z t1 $
# $Revision: 98 $
# $Date: 2014-01-11 19:09:59 +0900 (Sat, 11 Jan 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-01-11 19:09:59 +0900 (Sat, 11 Jan 2014) $
r""" timeout -- timeout decorator

$Revision: 98 $

"""

import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 98 $'
__version__ = '0.1.0'


import signal
import functools

class TimeoutError(StandardError): pass
# https://wiki.python.org/moin/PythonDecoratorLibrary#Function_Timeout
def timeout(seconds, error_message = 'Function call timed out'):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return functools.wraps(func)(wrapper)

    return decorated


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    import time

    @timeout(1, 'Function slow; aborted')
    def slow_function():
        time.sleep(5)
    slow_function()
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# timeout.py ends here
