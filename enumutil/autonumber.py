#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
