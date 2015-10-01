#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
