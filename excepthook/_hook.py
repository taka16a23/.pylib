#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _hook.py 341 2015-07-24 05:04:33Z t1 $
# $Revision: 341 $
# $Date: 2015-07-24 14:04:33 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:04:33 +0900 (Fri, 24 Jul 2015) $

r"""_hook -- DESCRIPTION

"""
import sys


class ExceptionHook(object):
    r"""ExceptionHook

    ExceptionHook is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self.is_hooking = False
        self.func = None
        self.start_hook()

    # def __del__(self):
    #     """
    #     INTERNAL COMMENT
    #     Do not imprement `raise'!!
    #     """
    #     self.stop_hook()

    def start_hook(self, ):
        r"""SUMMARY

        start_hook()

        @Return:

        @Error:
        """
        if not self.is_hooking:
            self.func = sys.excepthook
            sys.excepthook = self.on_except
            self.is_hooking = True

    def stop_hook(self, ):
        r"""SUMMARY

        stop_hook()

        @Return:

        @Error:
        """
        if self.is_hooking:
            sys.excepthook = self.func

    def on_except(self, excls, value, trcbck):
        r"""SUMMARY

        on_except(excls, value, trcbck)

        @Arguments:
        - `excls`:
        - `value`:
        - `trcbck`:

        @Return:

        @Error:
        """
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _hook.py ends here
