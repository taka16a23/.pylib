#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""restart -- DESCRIPTION

"""
from xahk.bind.key import GlobalKeyBinder
from xahk.bind.accelerator import Accelerator
from xahk.x11.modifier import Modifier
from xahk.bind.key import KeyEventHandler

from relaunch import relaunch


class Restart(KeyEventHandler):
    r"""Restart

    Restart is a KeyEventHandler.
    Responsibility:
    """
    def on_key_press(self, event):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        relaunch()


GLOBALKEY = GlobalKeyBinder()
GLOBALKEY.bind(Accelerator.from_key_label('r', Modifier.Mask.Super),
               Restart())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# restart.py ends here
