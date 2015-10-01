#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 80 2013-11-22 07:02:28Z t1 $
# $Revision: 80 $
# $Date: 2013-11-22 16:02:28 +0900 (Fri, 22 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-22 16:02:28 +0900 (Fri, 22 Nov 2013) $

r"""\
Name: __init__.py

doc search
module name search
class name search
method name search
function name search
variables search
pip search
cache use

name:
file:
type:
definition:
summary:
doc:
source:



search name __builtin__

builtin function
    search: name doc



"""

from .moduleinfowalker import ModuleInfoWalker
from .explorer import explorer


__revision__ = "$Revision: 80 $"
__version__ = "0.1.0"

__all__ = [ 'ModuleInfoWalker', 'explorer']



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
