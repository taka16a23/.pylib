#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" log -- logging decorator


"""

import sys as _sys
import functools
import logging

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# https://wiki.python.org/moin/PythonDecoratorLibrary#Logging_decorator_with_specified_logger_.28or_default.29

class log_with(object):
    '''Logging decorator that allows you to log with a
specific logger.
'''
    # Customize these messages
    ENTRY_MESSAGE = 'Entering {}'
    EXIT_MESSAGE = 'Exiting {}'

    def __init__(self, logger=None):
        self.logger = logger

    def __call__(self, func):
        '''Returns a wrapper that wraps func.
The wrapper will log the entry and exit points of the function
with logging.INFO level.
'''
        # set logger if it was not set earlier
        if not self.logger:
            logging.basicConfig()
            self.logger = logging.getLogger(func.__module__)

        @functools.wraps(func)
        def wrapper(*args, **kwds):
            self.logger.info(self.ENTRY_MESSAGE.format(func.__name__))  # logging level .info(). Set to .debug() if you want to
            f_result = func(*args, **kwds)
            self.logger.info(self.EXIT_MESSAGE.format(func.__name__))   # logging level .info(). Set to .debug() if you want to
            return f_result
        return wrapper


def _test():
    r"""Test function."""
    return 0


if __name__ == '__main__':
    logging.basicConfig()
    log = logging.getLogger('custom_log')
    log.setLevel(logging.DEBUG)
    log.info('ciao')

    @log_with(log)     # user specified logger
    def foo():
        print 'this is foo'
    foo()

    @log_with()        # using default logger
    def foo2():
        print 'this is foo2'
    foo2()
    _sys.exit(_test())


# output
# >>> ================================ RESTART ================================
# >>>
# INFO:custom_log:ciao
# INFO:custom_log:Entering foo # uses the correct logger
# this is foo
# INFO:custom_log:Exiting foo
# INFO:__main__:Entering foo2  # uses the correct logger
# this is foo2
# INFO:__main__:Exiting foo2




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# log.py ends here
