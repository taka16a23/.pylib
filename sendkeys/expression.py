#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""expression -- DESCRIPTION

"""



class Expression(object):
    r"""SUMMARY
    """
    __slots__ = ('code', 'press', 'release', 'kwargs')

    def __init__(self, code, press=True, release=True, kwargs=None):
        r"""

        @Arguments:
        - `code`:
        - `press`:
        - `release`:
        """
        self.code = code
        self.press = press
        self.release = release
        self.kwargs = kwargs or {}

    def __repr__(self, ):
        return ('{0.__class__.__name__}'
                '(code={1}, press={0.press}, release={0.release},'
                ' kwargs={0.kwargs})'
                .format(self, repr(self.code)))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# expression.py ends here
