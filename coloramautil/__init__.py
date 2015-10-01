#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 390 2015-08-06 15:47:02Z t1 $
# $Revision: 390 $
# $Date: 2015-08-07 00:47:02 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 00:47:02 +0900 (Fri, 07 Aug 2015) $

r"""Name: __init__.py


"""
from colorama import Fore, Style, Back, init, deinit, reinit
from coloramautil import formatter
from coloramautil.formatter import *



__revision__ = "$Revision: 390 $"
__version__ = "0.1.1"

__all__ = ['Fore', 'Style', 'Back', 'formatter', 'init', 'deinit', 'reinit']
__all__ += formatter.__all__



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
