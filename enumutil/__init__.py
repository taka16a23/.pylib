#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 371 2015-08-06 03:49:18Z t1 $
# $Revision: 371 $
# $Date: 2015-08-06 12:49:18 +0900 (Thu, 06 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-06 12:49:18 +0900 (Thu, 06 Aug 2015) $

r"""Name: __init__.py


"""
from enum import Enum, IntEnum, EnumMeta
from enumutil.autonumber import AutoNumber
from enumutil.orderedenum import OrderedEnum
from enumutil.duplicatefree import DuplicateFreeEnum


__revision__ = "$Revision: 371 $"
__version__ = "0.1.1"

__all__ = ['AutoNumber', 'OrderedEnum', 'DuplicateFreeEnum', 'Enum', 'IntEnum',
           'EnumMeta']




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
