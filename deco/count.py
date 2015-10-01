#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" count -- count decorator


"""

import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class countcalls(object):
   "Decorator that keeps track of the number of times a function is called."

   __instances = {}

   def __init__(self, f):
      self.__f = f
      self.__numcalls = 0
      countcalls.__instances[f] = self

   def __call__(self, *args, **kwargs):
      self.__numcalls += 1
      return self.__f(*args, **kwargs)

   @staticmethod
   def count(f):
      "Return the number of times the function f was called."
      return countcalls.__instances[f].__numcalls

   @staticmethod
   def counts():
      "Return a dict of {function: # of calls} for all registered functions."
      return dict([(f, countcalls.count(f)) for f in countcalls.__instances])


class countcalls2(object):
   "Decorator that keeps track of the number of times a function is called."

   __instances = {}

   def __init__(self, f):
      self.__f = f
      self.__numcalls = 0
      countcalls2.__instances[f] = self

   def __call__(self, *args, **kwargs):
      self.__numcalls += 1
      return self.__f(*args, **kwargs)

   def count(self):
      "Return the number of times the function f was called."
      return countcalls2.__instances[self.__f].__numcalls

   @staticmethod
   def counts():
      "Return a dict of {function: # of calls} for all registered functions."
      return dict([(f.__name__, countcalls2.__instances[f].__numcalls) for f in countcalls2.__instances])


def _test():
    r"""Test function."""
    @countcalls
    def f():
       print 'f called'

    @countcalls
    def g():
       print 'g called'

    f()
    f()
    f()
    print f.count() # prints 3
    print countcalls.counts() # same as f.counts() or g.counts()
    g()
    print g.count() # prints 1
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# count.py ends here
