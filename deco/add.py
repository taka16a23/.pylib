#!/usr/bin/env python
# -*- coding: utf-8 -*-
 r""" add -- add instance decorator


"""

import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


def addto(instance):
    def decorator(f):
        import types
        f = types.MethodType(f, instance, instance.__class__)
        setattr(instance, f.func_name, f)
        return f
    return decorator


def _test():
    r"""Test function."""

    class Foo:
        def __init__(self):
            self.x = 42

    foo = Foo()

    @addto(foo)
    def print_x(self):
        print self.x


    foo.print_x() # would print "42"
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# add.py ends here
