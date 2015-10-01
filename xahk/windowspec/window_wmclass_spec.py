#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: window_wmclass_spec.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""window_wmclass_spec -- DESCRIPTION

"""
from xahk.windowspec._windowspec import WindowSpec


class WindowWMClassSpec(WindowSpec):
    r"""WindowWMClassSpec

    WindowWMClassSpec is a WindowSpec.
    Responsibility:
    """
    def __init__(self, wmclass):
        r"""

        @Arguments:
        - `wmclass`:
        """
        self._wmclass = wmclass

    def is_satisfied(self, window):
        r"""SUMMARY

        is_satisfied(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return self._wmclass in window.wmclass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_wmclass_spec.py ends here
