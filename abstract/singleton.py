#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: singleton.py 104 2014-02-15 13:03:03Z t1 $
# $Revision: 104 $
# $Date: 2014-02-15 22:03:03 +0900 (Sat, 15 Feb 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-02-15 22:03:03 +0900 (Sat, 15 Feb 2014) $

r"""singleton -- a parts of abstract

"""

import sys as _sys
import os as _os

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 104 $'
__version__ = '0.1.0'


class Singleton(object):
    """Singleton.

    like use.
    class MyClass(Singleton, BaseClass):
        pass
    """
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class SingletonMeta(type):
    """MetaSingleton

    like use.
    class MyClass(BaseClass):
        __metaclass__ = SingletonMeta
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = (super(SingletonMeta, cls)
                                   .__call__(*args, **kwargs))
        return cls._instances[cls]



class DispatchSingletonMeta(type):
    """Single Dispatch Singleton Meta.

    like use.
    class MyClass(BaseClass):
        __metaclass__ = DispatchSingletonMeta
        def __init__(self, etc):
            self._etc = etc
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if not args:
            key = ''
            args = tuple(key)
        else:
            key = args[0]
        if cls not in cls._instances:
            cls._instances[cls] = {}
        if key not in cls._instances[cls]:
            cls._instances[cls][key] = (super(DispatchSingletonMeta, cls)
                                        .__call__(*args, **kwargs))
        return cls._instances[cls][key]


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# singleton.py ends here
