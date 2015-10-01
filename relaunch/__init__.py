#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 369 2015-08-06 03:39:24Z t1 $
# $Revision: 369 $
# $Date: 2015-08-06 12:39:24 +0900 (Thu, 06 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-06 12:39:24 +0900 (Thu, 06 Aug 2015) $

r"""Name: __init__.py


0.1.1: Modified
"subprocess.Popen" to "os.execl"

"""
import os as _os
import sys as _sys

__revision__ = "$Revision: 369 $"
__version__ = "0.1.1"

__all__ = ['relaunch', ]


def relaunch():
    r"""SUMMARY

    realunch()

    @Return:
    """
    python = _sys.executable
    _os.execl(python, python, *_sys.argv)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
