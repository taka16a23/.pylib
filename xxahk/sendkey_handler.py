#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sendkey_handler -- DESCRIPTION

"""
from xahk.sendkeys.sendkeys import SendKeys
from xahk.bind.key import KeyEventHandler
from xahk.bind.mouse import MouseEventHandler


class SendKeysHandler(KeyEventHandler, MouseEventHandler):
    r"""SendKeysHandler

    SendKeysHandler is a object.
    Responsibility:
    """
    def __init__(self, line):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._sendkeys = SendKeys(line)

    def on_key_release(self, event):
        r"""SUMMARY

        on_key_press(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        self._sendkeys.send(event.window)

    def on_button_release(self, event):
        r"""SUMMARY

        on_button_press(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """
        self._sendkeys.send()

    def __str__(self):
        return '{}("{}")'.format(super(SendKeysHandler, self).__str__(),
                                 self._sendkeys.line)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sendkey_handler.py ends here
