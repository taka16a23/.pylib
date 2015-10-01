#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: __init__.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
"""\
Name: __init__.py


"""


__revision__ = "$Revision: 87 $"
__version__ = "0.1.0"

__all__ = [ ]

# TODO: (Atami) [2013/09/04]
# class get elements from current directory files

import os as _os

if 'nt' == _os.name:
    from .nt_ref import *

elif 'posix' == _os.name:
    from .posix_ref import *



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
