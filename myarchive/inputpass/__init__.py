#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 285 2015-01-29 00:12:29Z t1 $
# $Revision: 285 $
# $Date: 2015-01-29 09:12:29 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:12:29 +0900 (Thu, 29 Jan 2015) $

r"""Name: __init__.py


"""
from myarchive.inputpass.abstract import InputPass
from myarchive.inputpass.egui import EasyGUIInputPass
from myarchive.inputpass.cmdline import CmdlineInputPass


__revision__ = "$Revision: 285 $"
__version__ = "0.1.0"

__all__ = [ ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
