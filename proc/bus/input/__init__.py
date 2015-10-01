#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 96 2013-12-23 13:08:21Z t1 $
# $Revision: 96 $
# $Date: 2013-12-23 22:08:21 +0900 (Mon, 23 Dec 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-12-23 22:08:21 +0900 (Mon, 23 Dec 2013) $

r"""Name: __init__.py


"""
import os

__revision__ = "$Revision: 96 $"
__version__ = "0.1.0"

__all__ = [ '' ]

if os.path.exists('/proc/bus/input/devices'):
    from . import devices





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
