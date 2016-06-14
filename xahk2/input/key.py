#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""key -- DESCRIPTION

"""
from xcb import xtest

from xahk2.input.keysym import KeySym
from xahk2.input.eventcode import EventCode


class X11Key(object):
    """Class X11Key
    """
    _modifiers = [KeySym.from_name('Control_R'),
                  KeySym.from_name('Control_L'),
                  KeySym.from_name('Alt_R'),
                  KeySym.from_name('Alt_L'),
                  KeySym.from_name('Shift_R'),
                  KeySym.from_name('Shift_L'),
                  KeySym.from_name('Super_R'),
                  KeySym.from_name('Super_L'),
    ]

    # Operations
    def __init__(self, display, keycode):
        """function __init__

        display:
        keycode:

        returns
        """
        self.display = display
        self._code = keycode

    def get_display(self):
        """function get_display

        returns
        """
        return self.display

    def get_code(self):
        """function get_code

        returns
        """
        return self._code

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:

        @Error:
        """
        return self.display.get_setup().roots[0].root

    def list_keysyms(self):
        """function list_keysyms

        returns
        """
        rep = self.display.core.GetKeyboardMapping(self._code, 1).reply()
        return [KeySym.from_number(sym) for sym in rep.keysyms]

    def _fake_input(self, evcode):
        r"""SUMMARY

        _fake_input(evcode, time, x, y)

        @Arguments:
        - `evcode`:

        @Return:

        @Error:
        """
        return self.display(xtest.key).FakeInputChecked(
            # EventCode, code, time, window, x, y, deviceid
            evcode, self._code, 0, self.root, 0, 0, 0)

    def press(self, ):
        """function press

        returns
        """
        return self._fake_input(EventCode.KeyPress)

    def release(self, ):
        """function release

        returns
        """
        return self._fake_input(EventCode.KeyRelease)

    def tap(self, ):
        """function tap

        returns
        """
        return [self.press(), self.release()]

    def has_keysym(self, keysym):
        """function has_keysym

        keysym:

        returns
        """
        return keysym in self.list_keysyms()

    def __contains__(self, keysym):
        """function __contains__

        keysym:

        returns
        """
        return keysym in self.list_keysyms()

    def is_modifier(self):
        """function is_modifier

        returns
        """
        keysyms = self.list_keysyms()
        for modkeysym in self._modifiers:
            if modkeysym in keysyms:
                return True
        return False

    def __repr__(self):
        return '{0.__class__.__name__}(code={0._code}, {1})'.format(
            self, self.list_keysyms())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# key.py ends here
