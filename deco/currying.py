#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" currying -- currying decorator


"""

import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class curried(object):
  '''
  Decorator that returns a function that keeps returning functions
  until all arguments are supplied; then the original function is
  evaluated.
  '''

  def __init__(self, func, *a):
    self.func = func
    self.args = a

  def __call__(self, *a):
    args = self.args + a
    if len(args) < self.func.func_code.co_argcount:
      return curried(self.func, *args)
    else:
      return self.func(*args)


def _test():
    r"""Test function."""
    @curried
    def add(a, b):
        return a + b

    add1 = add(1)

    print add1(2)

    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# currying.py ends here
