#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: autonumber.py 371 2015-08-06 03:49:18Z t1 $
# $Revision: 371 $
# $Date: 2015-08-06 12:49:18 +0900 (Thu, 06 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-06 12:49:18 +0900 (Thu, 06 Aug 2015) $

r"""autoenum -- DESCRIPTION

from "https://docs.python.org/3/library/enum.html#autonumber"
"""
from enum import Enum


class AutoNumber(Enum):
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# autoenum.py ends here
