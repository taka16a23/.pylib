#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: duplicatefree.py 371 2015-08-06 03:49:18Z t1 $
# $Revision: 371 $
# $Date: 2015-08-06 12:49:18 +0900 (Thu, 06 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-06 12:49:18 +0900 (Thu, 06 Aug 2015) $

r"""duplicatefree -- DESCRIPTION

from "https://docs.python.org/3/library/enum.html#orderedenum"
"""
from enum import Enum


class DuplicateFreeEnum(Enum):
    def __init__(self, *args):
        cls = self.__class__
        if any(self.value == e.value for e in cls):
            a = self.name
            e = cls(self.value).name
            raise ValueError(
                "aliases not allowed in DuplicateFreeEnum:  %r --> %r"
                % (a, e))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# duplicatefree.py ends here
