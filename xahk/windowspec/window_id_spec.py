#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: window_id_spec.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

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
