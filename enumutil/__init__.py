#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from enum import Enum, IntEnum, EnumMeta
from enumutil.autonumber import AutoNumber
from enumutil.orderedenum import OrderedEnum
from enumutil.duplicatefree import DuplicateFreeEnum


__version__ = "0.1.1"

__all__ = ['AutoNumber', 'OrderedEnum', 'DuplicateFreeEnum', 'Enum', 'IntEnum',
           'EnumMeta']




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
