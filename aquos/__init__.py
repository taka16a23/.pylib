#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: __init__.py 189 2014-05-17 09:44:59Z t1 $
# $Revision: 189 $
# $Date: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $
r"""\
Name: __init__.py


"""


from .cmds import FORMATS, CMDS, APART_NAMES
from .client import Aquos


__revision__ = "$Revision: 189 $"
__version__ = "0.1.0"

__all__ = [ 'FORMATS', 'CMDS', 'APART_NAMES', 'Aquos']



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
