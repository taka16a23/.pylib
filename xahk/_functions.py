#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _functions.py 463 2015-08-17 07:02:19Z t1 $
# $Revision: 463 $
# $Date: 2015-08-17 16:02:19 +0900 (Mon, 17 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-17 16:02:19 +0900 (Mon, 17 Aug 2015) $

r"""_functions -- DESCRIPTION

"""

from xahk.wm import WindowManager, Display


def list_windows():
    r"""SUMMARY

    list_windows()

    @Return:

    @Error:
    """
    return WindowManager(Display()).list_windows()





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _functions.py ends here
