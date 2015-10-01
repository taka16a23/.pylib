#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""orderedenum -- DESCRIPTION

from "https://docs.python.org/3/library/enum.html#orderedenum"
"""
from enum import Enum


class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# orderedenum.py ends here
