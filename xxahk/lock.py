#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""lock -- DESCRIPTION

"""
from xahk.bind.key import KeyEventHandler, GlobalKeyBinder
from xahk.bind.accelerator import Accelerator
from xahk.bind.keyboard_lock import KeyboardLocker
from xahk.x11.modifier import Modifier


class Lock(KeyEventHandler):
    r"""Lock

    Lock is a KeyEventHandler.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._locker = KeyboardLocker((Accelerator(9), ))

    def on_key_press(self, event):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        self._locker.start_locking()


GLOBALKEY = GlobalKeyBinder()
GLOBALKEY.bind(Accelerator.from_key_label('l', Modifier.Mask.Super), Lock())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# lock.py ends here
