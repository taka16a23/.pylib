#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: add.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
r""" add -- add instance decorator

$Revision: 87 $

"""

import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 87 $'
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
