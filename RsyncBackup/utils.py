#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$
r""" utils -- DESCRIPTION

$Revision$

"""


import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision$'
__version__ = '0.1.0'


def add2list(list_, additions):
    """SUMMARY



    @Arguments:

    - `list_`:
    - `additions`:

    @Return: unique list
    """
    from types import StringType, ListType
    if type(additions) == StringType:
        list_.append(additions)
    elif type(additions) == ListType:
        list_ += additions
    else:
        raise ValueError('Set only string or list type.'
                         '\nYou setted {0}'.format(type(additions)))
    return list(set(list_))


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# utils.py ends here
