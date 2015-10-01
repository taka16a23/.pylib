#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" warning -- warning decorator


"""

import sys as _sys
import warnings

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


# https://wiki.python.org/moin/PythonDecoratorLibrary#Generating_Deprecation_Warnings
def deprecated(func):
    '''This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.'''
    def new_func(*args, **kwargs):
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning)
        return func(*args, **kwargs)
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)
    return new_func

def _test():
    r"""Test function."""
    # === Examples of use ===

    @deprecated
    def some_old_function(x,y):
        return x + y

    class SomeClass:
        @deprecated
        def some_old_method(self, x,y):
            return x + y

    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# warning.py ends here
