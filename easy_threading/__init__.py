#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 374 2015-08-06 04:10:06Z t1 $
# $Revision: 374 $
# $Date: 2015-08-06 13:10:06 +0900 (Thu, 06 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-06 13:10:06 +0900 (Thu, 06 Aug 2015) $

r"""Name: __init__.py


"""
import threading

__revision__ = "$Revision: 374 $"
__version__ = "0.1.0"

__all__ = ['easy_thread', ]


def easy_thread(func, iterater):
    r"""SUMMARY

    easy_thread(func, iterater)

    @Arguments:
    - `func`:
    - `iterater`:

    @Return:
    """
    mainthread = threading.currentThread()
    for elem in iterater:
        thrd = threading.Thread(target=func, args=(elem, ))
        thrd.start()
    for thd in threading.enumerate():
        if mainthread != thd:
            thd.join()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
