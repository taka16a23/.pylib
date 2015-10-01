#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_print -- DESCRIPTION

"""
import sys
from excepthook._hook import ExceptionHook


class PrintExceptionHook(ExceptionHook):
    r"""PrintExceptionHook

    PrintExceptionHook is a ExceptionHook.
    Responsibility:
    """
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
        import traceback
        if issubclass(excls, KeyboardInterrupt):
            sys.__excepthook__(excls, value, trcbck)
            return
        errortype = 'Error type: {}'.format(excls)
        valuetxt = 'Uncaught exception: {0}'.format(str(value))
        trcbcktxt = ''.join(traceback.format_tb(trcbck))
        print('\n'.join([errortype, valuetxt, trcbcktxt]))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _print.py ends here
