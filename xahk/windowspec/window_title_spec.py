#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: window_title_spec.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""window_title_spec -- DESCRIPTION

"""
from xahk.windowspec._windowspec import WindowSpec


class WindowTitleSpec(WindowSpec):
    r"""WindowTitleSpec

    WindowTitleSpec is a WindowSpec.
    Responsibility:
    """
    def __init__(self, title):
        r"""

        @Arguments:
        - `title`:
        """
        self._title = title

    def is_satisfied(self, window):
        r"""SUMMARY

        is_satisfied(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return self._title == window.get_title()





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_title_spec.py ends here
