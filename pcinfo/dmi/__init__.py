#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 284 2015-01-29 00:10:44Z t1 $
# $Revision: 284 $
# $Date: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $

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


__revision__ = "$Revision: 284 $"
__version__ = "0.1.0"

__all__ = [ '' ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
