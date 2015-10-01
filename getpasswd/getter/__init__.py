#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
