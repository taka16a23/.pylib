#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""xsendkey -- DESCRIPTION

"""
from wxcb import conn
from wxcb.xobj.display import Display

from xsendkey.sender import XIntervalSender
from xsendkey.parser import Parse


class XSendkey(object):
    r"""_XSendkey

    _XSendkey is a object.
    Responsibility:
    """
    def __init__(self, line):
        r"""

        @Arguments:
        - `line`:
        """
        self._line = line

    def send(self, window, interval=0, display=None):
        r"""SUMMARY

        send(window, display=None)

        @Arguments:
        - `window`:
        - `display`:

        @Return:

        @Error:
        """
        parser = Parse()
        parser.parse(self._line, display)
        sender = XIntervalSender(parser.get_xinputs(), interval)
        sender.set_window(window)
        sender.send()

    def flush(self, display=None):
        r"""SUMMARY

        flush(display=None)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        Display(display).flush()




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# xsendkey.py ends here
