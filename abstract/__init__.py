#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 98 2014-01-11 10:09:59Z t1 $
# $Revision: 98 $
# $Date: 2014-01-11 19:09:59 +0900 (Sat, 11 Jan 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-01-11 19:09:59 +0900 (Sat, 11 Jan 2014) $

r"""Name: __init__.py


"""
from abstract import abcs
from abstract import singleton
from abstract.abcs import *
from abstract.singleton import *


__revision__ = "$Revision: 98 $"
__version__ = "0.1.0"

__all__ = ['IterABC', 'BoolABC', 'WithABC', 'FileAdaptorABC', 'Singleton',
           'SingletonMeta', 'SelectABC']


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
