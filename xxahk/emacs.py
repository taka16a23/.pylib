#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""emacs -- DESCRIPTION

"""
from xahk.wm.window_spec import WindowWMClassSpec
from xahk.bind.key import KeyBinder
from xahk.bind.accelerator import Accelerator
from xahk.x11.modifier import Modifier
from .sendkey_handler import SendKeysHandler



EMACS_SPEC = WindowWMClassSpec('emacs')

EMACS_KEY_BINDER = KeyBinder(EMACS_SPEC)
EMACS_KEY_BINDER.bind(
    Accelerator.from_key_label('n', Modifier.Mask.Control), SendKeysHandler('^n'))
EMACS_KEY_BINDER.bind(
    Accelerator.from_key_label('k', Modifier.Mask.Control), SendKeysHandler('^k'))
EMACS_KEY_BINDER.bind(
    Accelerator.from_key_label('l', Modifier.Mask.Control), SendKeysHandler('^l'))
EMACS_KEY_BINDER.bind(
    Accelerator.from_key_label('j', Modifier.Mask.Control), SendKeysHandler('^j'))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# emacs.py ends here
