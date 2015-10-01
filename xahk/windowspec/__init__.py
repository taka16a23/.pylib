#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
