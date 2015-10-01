#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_logging -- DESCRIPTION

"""
import sys
from excepthook._hook import ExceptionHook


class LoggingExceptionHook(ExceptionHook):
    r"""LoggingExceptionHook

    LoggingExceptionHook is a ExceptionHook.
    Responsibility:
    """
    def __init__(self, logger):
        r"""

        @Arguments:
        - `logger`:
        """
        super(LoggingExceptionHook, self).__init__()
        self._logger = logger

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
        self._logger.exception('\n'.join([errortype, valuetxt, trcbcktxt]))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _logging.py ends here
