#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""xfce4_terminal -- DESCRIPTION

"""
from xahk.wm.window_spec import WindowWMClassSpec
from xahk.bind.key import KeyBinder
from xahk.bind.accelerator import Accelerator
from xahk.x11.modifier import Modifier
from .sendkey_handler import SendKeysHandler


XFCE4_TERMINAL_SPEC = WindowWMClassSpec('xfce4-terminal')
xfce4_terminal = KeyBinder(XFCE4_TERMINAL_SPEC)
xfce4_terminal.bind(
    Accelerator.from_key_label('v', Modifier.Mask.Control), SendKeysHandler('+^v'))
xfce4_terminal.bind(
    Accelerator.from_key_label('Return', Modifier.Mask.Control),
    SendKeysHandler('&{Return}'))
xfce4_terminal.bind(
    Accelerator.from_key_label('k', Modifier.Mask.Control), SendKeysHandler('^k'))
xfce4_terminal.bind(
    Accelerator.from_key_label('n', Modifier.Mask.Control), SendKeysHandler('^n'))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# xfce4_terminal.py ends here
