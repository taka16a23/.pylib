#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_windowspec -- DESCRIPTION

"""


class WindowSpec(object):
    r"""WindowSpec

    WindowSpec is a object.
    Responsibility:
    """
    def is_satisfied(self, window):
        r"""SUMMARY

        is_satisfied(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return False

    def __call__(self, window):
        return self.is_satisfied(window)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _windowspec.py ends here
