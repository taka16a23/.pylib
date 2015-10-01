#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: __init__.py


"""
import os as _os

from dotavoider import dotavoid

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
