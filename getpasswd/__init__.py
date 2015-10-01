#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 440 2015-08-07 01:25:23Z t1 $
# $Revision: 440 $
# $Date: 2015-08-07 10:25:23 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 10:25:23 +0900 (Fri, 07 Aug 2015) $

r"""Name: __init__.py


"""
from getpasswd.core import GetPasswd
from getpasswd.getter import * # must int
from getpasswd.func import GETPASSWD as getpasswd # as function
from getpasswd.func import confirm_passwd


__revision__ = "$Revision: 440 $"
__version__ = "0.0.2"

# __all__ = [ 'getpasswd', 'CmdlinePassGetter', 'EasyGUIPassGetter',
           # 'WXPassGetter', ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
