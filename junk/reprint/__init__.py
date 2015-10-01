#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 97 2014-01-04 08:46:02Z t1 $
# $Revision: 97 $
# $Date: 2014-01-04 17:46:02 +0900 (Sat, 04 Jan 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-01-04 17:46:02 +0900 (Sat, 04 Jan 2014) $

r"""Name: __init__.py


"""
import sys as _sys

__revision__ = "$Revision: 97 $"
__version__ = "0.1.0"

__all__ = [ 'reprint' ]


def reprint(str_):
    r"""SUMMARY

    reprint(str_)

    @Arguments:
    - `str_`:

    @Return:
    """
    _sys.stdout.write('\r' + str_)
    _sys.stdout.flush()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
