#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$
r"""\
Window Manager.

Name: __init__.py



"""

from wm._core import WindowManager
from wm import active
from wm import error
from wm._functions import *


__revision__ = "$Revision$"
__version__ = "0.1.0"


__all__ = [ 'active', 'error', 'WindowManager', ]




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
