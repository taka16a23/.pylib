#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 482 2015-08-29 03:36:29Z t1 $
# $Revision: 482 $
# $Date: 2015-08-29 12:36:29 +0900 (Sat, 29 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-29 12:36:29 +0900 (Sat, 29 Aug 2015) $

r"""Name: __init__.py


"""
from itertools import chain, product


__revision__ = "$Revision: 482 $"
__version__ = "0.1.0"

__all__ = ['iter_bruteforce', ]


def iter_bruteforce(charset, min_, max_):
    return (
        ''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(min_, max_ + 1)))




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
