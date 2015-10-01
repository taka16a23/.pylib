#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: explorer.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $

r"""explorer -- explorering module info.
"""

import sys as _sys
import re as _re

from .moduleinfowalker import ModuleInfoWalker
from .pager import normalpager

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 87 $'
__version__ = '0.1.0'


## main functions
#
def explorer(key, pager=None, inname=True, infile=False,
             indef=False, insummary=True, indoc=False):
    r"""SUMMARY

    @Arguments:
    - `key`:

    @Return:
    """
    if not pager:
        pager = normalpager

    key = _re.compile(key)
    for d in ModuleInfoWalker():
        if ((inname and key.search(str(d['name']))) or
            (infile and key.search(str(d['file']))) or
            (indef and key.search(str(d['definition']))) or
            (insummary and key.search(str(d['summary']))) or
            (indoc and key.search(str(d['doc'])))):
            pager(key, d, inname=inname, infile=infile, indef=indef,
                  insummary=insummary, indoc=indoc)


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# explorer.py ends here
