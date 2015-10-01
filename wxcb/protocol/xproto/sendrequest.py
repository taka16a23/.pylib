#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: sendrequest.py 280 2015-01-29 00:05:31Z t1 $
# $Revision: 280 $
# $Date: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $

r"""packet -- DESCRIPTION

"""
from xcb import Request, VoidCookie
import wxcb.conn
import wxcb.xobj.display as _display


class SendRequest(object):
    r"""SendRequest

    SendRequest is a object.
    Responsibility:
    """
    def __init__(self, opcode, cookietype, checked=True, reply=None,
                 display=None):
        r"""

        @Arguments:
        - `opcode`:
        - `cookie`:
        - `reply`:
        - `ischecked`:
        - `display`:
        """
        self._opcode = None
        self._cookie = None
        self._checked = None
        self._reply = None
        self._display = None

        self.set_opcode(opcode)
        self.set_cookie_type(cookietype)
        self.set_reply(reply)
        self.set_checked(checked)
        self.set_display(display)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._display

    def set_display(self, display):
        r"""SUMMARY

        set_display()

        @Return:

        @Error:
        """
        self._display = _display.Display(display)

    display = property(get_display, set_display)

    def get_opcode(self, ):
        r"""SUMMARY

        get_opcode()

        @Return:

        @Error:
        """
        return self._opcode

    def set_opcode(self, opcode):
        r"""SUMMARY

        set_opcode(opcode)

        @Arguments:
        - `opcode`:

        @Return:

        @Error:
        """
        self._opcode = int(opcode)

    opcode = property(get_opcode, set_opcode)

    def get_cookie_type(self, ):
        r"""SUMMARY

        get_cookie_type()

        @Return:

        @Error:
        """
        return self._cookie

    def set_cookie_type(self, cookie_type):
        r"""SUMMARY

        set_cookie_type(cookie_type)

        @Arguments:
        - `cookie_type`:

        @Return:

        @Error:
        """
        if not isinstance(cookie_type, (type, )):
            # TODO: (Atami) [2015/01/18]
            raise TypeError()
        self._cookie = cookie_type

    cookietype = property(get_cookie_type, set_cookie_type)

    def ischecked(self, ):
        r"""SUMMARY

        ischecked()

        @Return:

        @Error:
        """
        return self._checked

    def set_checked(self, checked):
        r"""SUMMARY

        set_ischecked(ischecked)

        @Arguments:
        - `ischecked`:

        @Return:

        @Error:
        """
        self._checked = bool(checked)

    checked = property(ischecked, set_checked)

    def get_reply(self, ):
        r"""SUMMARY

        get_reply()

        @Return:

        @Error:
        """
        return self._reply

    def set_reply(self, reply=None):
        r"""SUMMARY

        set_reply()

        @Return:

        @Error:
        """
        if not isinstance(reply, (type, )) and reply is not None:
            # TODO: (Atami) [2015/01/18]
            raise TypeError()
        self._reply = reply

    reply = property(get_reply, set_reply)

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        wxcb.conn.connect(self._display).flush()

    def isvoid(self, ):
        r"""SUMMARY

        isvoid()

        @Return:

        @Error:
        """
        return self.cookietype == VoidCookie and self.reply is None

    def _void_request(self, buf):
        r"""SUMMARY

        _void_request(buf)

        @Arguments:
        - `buf`:

        @Return:

        @Error:
        """
        return wxcb.conn.connect(self._display).core.send_request(
            Request(buf, self.opcode, True, self.checked),
            self.cookietype())

    def _reply_request(self, buf):
        r"""SUMMARY

        _reply_request(buf)

        @Arguments:
        - `buf`:

        @Return:

        @Error:
        """
        return wxcb.conn.connect(self._display).core.send_request(
            Request(buf, self.opcode, False, self.checked),
            self.cookietype(), self.reply)

    def send(self, buf):
        r"""SUMMARY

        send(buffer)

        @Arguments:
        - `buf`:

        @Return:

        @Error:
        """
        if self.isvoid():
            return self._void_request(buf)
        return self._reply_request(buf)

    def __call__(self, buf):
        return self.send(buf)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# packet.py ends here
