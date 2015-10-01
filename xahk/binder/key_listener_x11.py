#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: key_listener_x11.py 348 2015-08-04 13:56:54Z t1 $
# $Revision: 348 $
# $Date: 2015-08-04 22:56:54 +0900 (Tue, 04 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-04 22:56:54 +0900 (Tue, 04 Aug 2015) $

r"""key_listener_x11 -- DESCRIPTION

"""
from xcb.xproto import BadWindow

from dotavoider import ListDotAvoider

from xahk.binder.key_listener import KeyListener
from xahk.binder.define import ModifierMask


class KeyListenerX11(KeyListener):
    """Class KeyListenerX11
    """
    # Operations
    def _register_accelerator_impl(self, accelerators):
        """function register_accelerator_impl

        accelerator:

        returns
        """
        # extend firster than multi append
        accs, extend = ListDotAvoider().extend
        for acc in accelerators:
            extend(
                (acc,
                 acc|ModifierMask.Numlock,
                 acc|ModifierMask.Lock,
                 acc|ModifierMask.Mod5,
                 acc|ModifierMask.Numlock|ModifierMask.Lock,
                 acc|ModifierMask.Numlock|ModifierMask.Mod5,
                 acc|ModifierMask.Lock|ModifierMask.Mod5,
                 acc|ModifierMask.Numlock|ModifierMask.Lock|ModifierMask.Mod5
                 ))
        cookies = self._window.grab_keys(accs)
        for cookie in cookies:
            try:
                cookie.check()
            except BadWindow as err:
                from xahk.logger import LOG
                LOG.error('{}'.format(err))
                import os
                os.system('modprobe pcspkr')
                os.system('/usr/bin/beep -f250 -r2 -l50')
                os.system('rmmod pcspkr')
                # TODO: (Atami) [2015/07/23]
                return

    def _unregister_accelerator_impl(self, accelerators):
        """function unregister_accelerator_impl

        accelerator:

        returns
        """
        # extend firster than multi append
        accs, extend = ListDotAvoider().extend
        for acc in accelerators:
            extend(
                (acc,
                 acc|ModifierMask.Numlock,
                 acc|ModifierMask.Lock,
                 acc|ModifierMask.Mod5,
                 acc|ModifierMask.Numlock|ModifierMask.Lock,
                 acc|ModifierMask.Numlock|ModifierMask.Mod5,
                 acc|ModifierMask.Lock|ModifierMask.Mod5,
                 acc|ModifierMask.Numlock|ModifierMask.Lock|ModifierMask.Mod5
                 ))
        cookies = self._window.ungrab_keys(accs)
        for cookie in cookies:
            try:
                cookie.check()
            except BadWindow as err:
                from xahk.logger import LOG
                LOG.error('{}'.format(err))
                import os
                os.system('modprobe pcspkr')
                os.system('/usr/bin/beep -f250 -r2 -l50')
                os.system('rmmod pcspkr')
                # TODO: (Atami) [2015/07/23]
                return



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# key_listener_x11.py ends here
