#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _print.py 341 2015-07-24 05:04:33Z t1 $
# $Revision: 341 $
# $Date: 2015-07-24 14:04:33 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:04:33 +0900 (Fri, 24 Jul 2015) $

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
