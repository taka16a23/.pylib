#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sendkeys -- DESCRIPTION

"""
from time import sleep
from xahk2.input.sendkeys.parser import Parser
from xahk2.input.sendkeys.analyzer import XTestAnalyzer


# TODO: (Atami) [2015/12/12]
# test code


class SendKeys(object):
    r"""SendKeys

    SendKeys is a object.
    Responsibility:
    """
    def __init__(self, display, interval=0):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.display = display
        self.interval = interval

    def get_interval(self, ):
        r"""SUMMARY

        get_interval()

        @Return:

        @Error:
        """
        return self.interval

    def set_interval(self, interval):
        r"""SUMMARY

        set_interval(interval)

        @Arguments:
        - `interval`:

        @Return:

        @Error:
        """
        self.interval = interval

    def sendkeys(self, string):
        r"""SUMMARY

        sendkeys(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        expressions = Parser(XTestAnalyzer(self.display)).compile(string)
        for exp in expressions:
            exp.interpret()
            if self.interval:
                self.display.flush()
                sleep(self.interval)
        self.display.flush()

    def direct_sendkeys(self, string, window):
        r"""SUMMARY

        direct_sendkeys(string, window)

        @Arguments:
        - `string`:
        - `window`:

        @Return:

        @Error:
        """
        # TODO: (Atami) [2015/12/12]
        # SendEvent



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sendkeys.py ends here
