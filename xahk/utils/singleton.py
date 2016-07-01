#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""singleton -- DESCRIPTION

"""


class SingletonMeta(type):
    """MetaSingleton

    like use.
    class MyClass(BaseClass):
        __metaclass__ = SingletonMeta
    """
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = (super(SingletonMeta, cls)
                                   .__call__(*args, **kwargs))
        return cls._instance


class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# singleton.py ends here
