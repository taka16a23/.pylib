#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""windowspecs -- DESCRIPTION

"""
from xahk.windowspec._windowspec import WindowSpec


class WindowSpecs(WindowSpec):
    r"""WindowSpecs

    WindowSpecs is a WindowSpec.
    Responsibility:
    """
    def __init__(self, specs):
        r"""

        @Arguments:
        - `specs`:
        """
        WindowSpec.__init__(self, )
        self._specs = []
        for spec in specs:
            self.add_spec(spec)

    def is_satisfied(self, window):
        r"""SUMMARY

        is_satisfied(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        for spec in self._specs:
            if spec.is_satisfied(window):
                return True
        return False

    def add_spec(self, spec):
        r"""SUMMARY

        add_spec(spec)

        @Arguments:
        - `spec`:

        @Return:

        @Error:
        """
        self._specs.append(spec)

    def remove_spec(self, spec):
        r"""SUMMARY

        remove_spec(spec)

        @Arguments:
        - `spec`:

        @Return:

        @Error:
        """
        self._specs.remove(spec)

    def has_spec(self, spec):
        r"""SUMMARY

        has_spec(spec)

        @Arguments:
        - `spec`:

        @Return:

        @Error:
        """
        return spec in self._specs



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# windowspecs.py ends here
