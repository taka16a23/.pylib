#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: __init__.py 441 2015-08-07 01:25:43Z t1 $
# $Revision: 441 $
# $Date: 2015-08-07 10:25:43 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 10:25:43 +0900 (Fri, 07 Aug 2015) $
r"""\
Name: __init__.py


"""
import os as _os

from dotavoider import dotavoid

__revision__ = '$Revision: 441 $'
__version__ = '0.1.0'


__all__ = ['which', ]


def which(filename):
    """docstring for which"""
    join, isfile = _os.path.join, _os.path.isfile
    locations = _os.environ.get("PATH").split(_os.pathsep)
    candlist, append = dotavoid([], 'append')
    for location in locations:
        candidate = join(location, filename)
        if isfile(candidate):
            append(candidate)
    return candlist


def test():
    "Test function."
    pass


if __name__ == '__main__':
    test()




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
