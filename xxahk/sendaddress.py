#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sendaddress -- DESCRIPTION

"""
from xahk.bind.key import GlobalKeyBinder
from xahk.bind.accelerator import Accelerator
from xahk.x11.modifier import Modifier
from .sendkey_handler import SendKeysHandler


GLOBALKEY = GlobalKeyBinder()
GLOBALKEY.bind(Accelerator.from_key_label('t', Modifier.Mask.Super),
               SendKeysHandler('taka16a23@gmail.com'))
GLOBALKEY.bind(Accelerator.from_key_label('T', Modifier.Mask.Super),
               SendKeysHandler('takahiroatsumi0517@gmail.com'))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sendaddress.py ends here
