#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _windowspec.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

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
