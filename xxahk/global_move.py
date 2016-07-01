#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""global_move -- DESCRIPTION

"""


from xahk.bind.key import GlobalKeyBinder
from xahk.bind.accelerator import Accelerator
from xahk.x11.modifier import Modifier
from .sendkey_handler import SendKeysHandler

GLOBALKEY = GlobalKeyBinder()
GLOBALKEY.bind(Accelerator.from_key_label('n', Modifier.Mask.Control),
               SendKeysHandler('{Down}'))
GLOBALKEY.bind(Accelerator.from_key_label('k', Modifier.Mask.Control),
               SendKeysHandler('{Up}'))
GLOBALKEY.bind(Accelerator.from_key_label('j', Modifier.Mask.Control),
               SendKeysHandler('{Left}'))
GLOBALKEY.bind(Accelerator.from_key_label('l', Modifier.Mask.Control),
               SendKeysHandler('{Right}'))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# global_move.py ends here
