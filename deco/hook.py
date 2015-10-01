#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: hook.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# https://wiki.python.org/moin/PythonDecoratorLibrary#Pre-.2FPost-Conditions
r'''
Provide pre-/postconditions as function decorators.

Example usage:

  >>> def in_ge20(inval):
  ...    assert inval >= 20, 'Input value < 20'
  ...
  >>> def out_lt30(retval, inval):
  ...    assert retval < 30, 'Return value >= 30'
  ...
  >>> @precondition(in_ge20)
  ... @postcondition(out_lt30)
  ... def inc(value):
  ...   return value + 1
  ...
  >>> inc(5)
  Traceback (most recent call last):
    ...
  AssertionError: Input value < 20
  >>> inc(29)
  Traceback (most recent call last):
    ...
  AssertionError: Return value >= 30
  >>> inc(20)
  21

You can define as many pre-/postconditions for a function as you
like. It is also possible to specify both types of conditions at once:

  >>> @conditions(in_ge20, out_lt30)
  ... def add1(value):
  ...   return value + 1
  ...
  >>> add1(5)
  Traceback (most recent call last):
    ...
  AssertionError: Input value < 20

An interesting feature is the ability to prevent the creation of
pre-/postconditions at function definition time. This makes it
possible to use conditions for debugging and then switch them off for
distribution.

  >>> debug = False
  >>> @precondition(in_ge20, debug)
  ... def dec(value):
  ...   return value - 1
  ...
  >>> dec(5)
  4
'''

import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 87 $'
__version__ = '0.1.0'

__all__ = ['before_hook', 'after_hook', 'conditions']

DEFAULT_ON = True

def before_hook(before_hook, use_conditions=DEFAULT_ON):
    return conditions(before_hook, None, use_conditions)

def after_hook(after_hook, use_conditions=DEFAULT_ON):
    return conditions(None, after_hook, use_conditions)

class conditions(object):
    __slots__ = ('__precondition', '__postcondition')

    def __init__(self, pre, post, use_conditions=DEFAULT_ON):
        if not use_conditions:
            pre, post = None, None

        self.__precondition  = pre
        self.__postcondition = post

    def __call__(self, function):
        # combine recursive wrappers (@precondition + @postcondition == @conditions)
        pres  = set((self.__precondition,))
        posts = set((self.__postcondition,))

        # unwrap function, collect distinct pre-/post conditions
        while type(function) is FunctionWrapper:
            pres.add(function._pre)
            posts.add(function._post)
            function = function._func

        # filter out None conditions and build pairs of pre- and postconditions
        conditions = map(None, filter(None, pres), filter(None, posts))

        # add a wrapper for each pair (note that 'conditions' may be empty)
        for pre, post in conditions:
            function = FunctionWrapper(pre, post, function)

        return function

class FunctionWrapper(object):
    def __init__(self, before_hook, after_hook, function):
        self._pre  = before_hook
        self._post = after_hook
        self._func = function

    def __call__(self, *args, **kwargs):
        before_hook  = self._pre
        after_hook = self._post

        if before_hook:
            before_hook(*args, **kwargs)
        result = self._func(*args, **kwargs)
        if after_hook:
            after_hook(result, *args, **kwargs)
        return result


def _test():
    r"""Test function."""
    import doctest
    doctest.testmod()
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# hook.py ends here
