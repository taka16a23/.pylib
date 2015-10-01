#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""window_id_spec -- DESCRIPTION

"""
from xahk.windowspec._windowspec import WindowSpec


class WindowIDSpec(WindowSpec):
    r"""WindowIDSpec

    WindowIDSpec is a WindowSpec.
    Responsibility:
    """
    def __init__(self, id):
        r"""

        @Arguments:
        - `id`:
        """
        self._id = id

    def get_id(self, ):
        r"""SUMMARY

        get_id()

        @Return:

        @Error:
        """
        return self._id

    id = property(get_id)

    def is_satisfied(self, window):
        r"""SUMMARY

        is_satisfied(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return self.id == window.get_id()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_id_spec.py ends here
