#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_compat -- DESCRIPTION

"""

try:
    from functools import wraps
except ImportError:
    def wraps(original):
        def inner(fn):
            for attribute in ['__module__', '__name__', '__doc__']:
                setattr(fn, attribute, getattr(original, attribute))
            for attribute in ['__dict__']:
                if hasattr(fn, attribute):
                    getattr(fn, attribute).update(getattr(original, attribute))
                else:
                    setattr(fn, attribute,
                            getattr(original, attribute).copy())
            return fn
        return inner



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _compat.py ends here
