#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 274 2015-01-18 05:08:47Z t1 $
# $Revision: 274 $
# $Date: 2015-01-18 14:08:47 +0900 (Sun, 18 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-18 14:08:47 +0900 (Sun, 18 Jan 2015) $

r"""Name: __init__.py


"""
from getpasswd.log import LOG as _LOG
from getpasswd.getter.abstract import PassGetter
from getpasswd.getter.cmdline import CmdlinePassGetter


try:
    from getpasswd.getter._easygui import EasyGUIPassGetter
except ImportError as err:
    # skip these
    _LOG.warning(str(err))
    _LOG.warning('try "pip install easygui".')

try:
    from getpasswd.getter.wxgui import WXPassGetter
except ImportError as err:
    # skip these
    _LOG.warning(str(err))
    _LOG.warning('try "pip install wx"')


# __all__ = [ ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
