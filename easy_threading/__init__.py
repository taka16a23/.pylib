#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import threading

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
