#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
