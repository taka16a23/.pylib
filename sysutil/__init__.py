#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 92 2013-12-07 10:20:05Z t1 $
# $Revision: 92 $
# $Date: 2013-12-07 19:20:05 +0900 (Sat, 07 Dec 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-12-07 19:20:05 +0900 (Sat, 07 Dec 2013) $

r"""\
Name: __init__.py


"""
import sys as _sys
import os as _os
from . import redirect

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')

__revision__ = "$Revision: 92 $"
__version__ = "0.1.0"

__all__ = [ '' ]

EXIT_SUCCESS = 0
EXIT_FAILURE = 1


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
