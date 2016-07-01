#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""libre_calc -- DESCRIPTION

"""
from xahk.wm.window_spec import WindowWMClassSpec
from xahk.bind.key import KeyBinder
from xahk.bind.accelerator import Accelerator
from xahk.x11.modifier import Modifier
from .sendkey_handler import SendKeysHandler


LIBREOFFICE_CALC_SPEC = WindowWMClassSpec('libreoffice-calc')

LIBRE_CALC_KEY_BINDER = KeyBinder(LIBREOFFICE_CALC_SPEC)
LIBRE_CALC_KEY_BINDER.bind(
    Accelerator.from_key_label('e', Modifier.Mask.Control), SendKeysHandler('{F2}'))
LIBRE_CALC_KEY_BINDER.bind(
    Accelerator.from_key_label('q', ), SendKeysHandler('{F2}'))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# libre_calc.py ends here
