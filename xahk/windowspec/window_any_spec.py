#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: window_any_spec.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""window_any_spec -- DESCRIPTION

"""
from xahk.windowspec._windowspec import WindowSpec


class WindowAnySpec(WindowSpec):
    r"""WindowAnySpec

    WindowAnySpec is a WindowSpec.
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
        return True





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_any_spec.py ends here
