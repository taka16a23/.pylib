#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
# TODO: (Atami) [2014/04/22]
# write test

from pcinfo.dmi.baseboard import getbaseboard
from pcinfo.dmi.cache import getcache
from pcinfo.dmi.chassis import getchassis
from pcinfo.dmi.connector import getconnector
from pcinfo.dmi.memory import getmemory
from pcinfo.dmi.processor import getprocessor
from pcinfo.dmi.slot import getslot
from pcinfo.dmi.system import getsystem


__version__ = "0.1.0"

__all__ = [ '' ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
