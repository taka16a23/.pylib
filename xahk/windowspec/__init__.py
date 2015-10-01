#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""Name: __init__.py


"""
from xahk.windowspec._windowspec import WindowSpec
from xahk.windowspec.window_any_spec import WindowAnySpec
from xahk.windowspec.window_id_spec import WindowIDSpec
from xahk.windowspec.window_title_spec import WindowTitleSpec
from xahk.windowspec.window_wmclass_spec import WindowWMClassSpec


__all__ = ['WindowSpec', 'WindowAnySpec', 'WindowIDSpec', 'WindowTitleSpec',
           'WindowWMClassSpec']



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
