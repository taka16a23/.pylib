#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _compat.py 307 2015-02-07 03:48:46Z t1 $
# $Revision: 307 $
# $Date: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $

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
