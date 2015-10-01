#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: sendkey.py 277 2015-01-28 23:57:11Z t1 $
# $Revision: 277 $
# $Date: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $

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
