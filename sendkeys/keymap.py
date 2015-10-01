#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keymap -- DESCRIPTION

# TODO: (Atami) [2014/03/29]

"""
from t1.listutil.limitlist import ListFill

from xcb2.abstract import ConnectionAbstract
import sendkeys.keysymdef


SPECIALCHAR_TO_NAME = {
    ' ' : "space",
    '\t' : "Tab",
    '\n' : "Return",  # for some reason this needs to be cr, not lf
    '\r' : "Return",
    '\e' : "Escape",
    '!' : "exclam",
    '#' : "numbersign",
    '%' : "percent",
    '$' : "dollar",
    '&' : "ampersand",
    '"' : "quotedbl",
    '\'' : "apostrophe",
    '(' : "parenleft",
    ')' : "parenright",
    '*' : "asterisk",
    '=' : "equal",
    '+' : "plus",
    ',' : "comma",
    '-' : "minus",
    '.' : "period",
    '/' : "slash",
    ':' : "colon",
    ';' : "semicolon",
    '<' : "less",
    '>' : "greater",
    '?' : "question",
    '@' : "at",
    '[' : "bracketleft",
    ']' : "bracketright",
    '\\' : "backslash",
    '^' : "asciicircum",
    '_' : "underscore",
    '`' : "grave",
    '{' : "braceleft",
    '|' : "bar",
    '}' : "braceright",
    '~' : "asciitilde"
    }


class ConvertError(StandardError):
    r"""SUMMARY
    """
    def __init__(self, data=''):
        self.data = data

    def __str__(self, ):
        return self.data


class SymToCodeError(ConvertError):
    r"""SUMMARY
    """
    def __str__(self, ):
        return '{} keysym failed convert to keycode'.format(self.data)


class StrToSymError(ConvertError):
    r"""SUMMARY
    """
    def __str__(self, ):
        return '"{}" failed convert to keysym'.format(self.data)


class KeymapCodes(ConnectionAbstract):
    r"""SUMMARY
    """

    def __init__(self, connection):
        r"""

        @Arguments:
        - `display`:
        """
        ConnectionAbstract.__init__(self, connection)
        self._keymap_codes = ListFill(fill=(), length=256)
        self.get_keyboard_mapping()

    def get_keyboard_mapping(self, ):
        r"""SUMMARY

        get_keyboard_mapping()

        @Return:
        """
        setup = self.connection.get_setup()
        minkeycode, maxkeycode = setup.min_keycode, setup.max_keycode
        lastcode, count = maxkeycode + minkeycode, maxkeycode - minkeycode + 1
        rep = self.connection.core.GetKeyboardMapping(minkeycode, count).reply()
        codes = zip(*[iter(rep.keysyms)] * rep.keysyms_per_keycode) # chunks
        self._keymap_codes[minkeycode:lastcode] = codes
        return codes

    def keycode_to_keysym(self, keycode, index):
        r"""SUMMARY

        keycode_to_keysym(keycode, index)

        Convert a keycode to a keysym, looking in entry index.
        Normally index 0 is unshifted, 1 is shifted, 2 is alt grid, and 3
        is shift+alt grid. If that key entry is not bound, X.NoSymbol is
        returned.

        @Arguments:
        - `keycode`:
        - `index`:

        @Return:
        """
        if keycode <= len(self._keymap_codes):
            if index < len(self._keymap_codes[keycode]):
                return self._keymap_codes[keycode][index]
        return 0


class KeyboardMapping(ConnectionAbstract):
    r"""SUMMARY
    """
    specialchar_to_name = SPECIALCHAR_TO_NAME

    def __init__(self, connection):
        r"""
        """
        ConnectionAbstract.__init__(self, connection)
        self._keymap_codes = KeymapCodes(connection)
        self._keymap_syms = {}
        self._update_keymap()

    def get_keyboard_mapping(self, ):
        r"""SUMMARY

        get_keyboard_mapping()

        @Return:
        """
        return self._keymap_codes.get_keyboard_mapping()

    def keysym_to_keycode(self, keysym):
        r"""SUMMARY

        keysym_to_keycode(keysym)

        @Arguments:
        - `keysym`:

        @Return:
        """
        if not keysym in self._keymap_syms:
            raise SymToCodeError(keysym)
        return self._keymap_syms[keysym][0][1]

    def keysym_to_keycodes(self, keysym):
        r"""SUMMARY

        keysym_to_keycodes(keysym)

        @Arguments:
        - `keysym`:

        @Return:
        """
        if not keysym in self._keymap_syms:
            raise SymToCodeError(keysym)
        return map(lambda x: (x[1], x[0]), self._keymap_syms[keysym])

    def keycode_to_keysym(self, keycode, index):
        r"""SUMMARY

        keycode_to_keysym(keycode, index)

        Convert a keycode to a keysym, looking in entry index.
        Normally index 0 is unshifted, 1 is shifted, 2 is alt grid, and 3
        is shift+alt grid. If that key entry is not bound, X.NoSymbol is
        returned.

        @Arguments:
        - `keycode`:
        - `index`:

        @Return:
        """
        return self._keymap_codes.keycode_to_keysym(keycode, index)

    def _update_keymap(self, ):
        r"""SUMMARY

        _update_keymap()

        @Return:
        """
        setup = self.connection.get_setup()
        first_keycode, count = setup.min_keycode, setup.max_keycode
        lastcode = first_keycode + count
        for codes in self._keymap_syms.itervalues():
            i = 0
            while i < len(codes):
                code = codes[i][1]
                if code >= first_keycode and code < lastcode:
                    del codes[i]
                else:
                    i = i + 1

        keysyms = self.get_keyboard_mapping()

        code = first_keycode
        for syms in keysyms:
            index = 0
            for sym in syms:
                if sym != 0:
                    if self._keymap_syms.has_key(sym):
                        symcodes = self._keymap_syms[sym]
                        symcodes.append((index, code))
                        symcodes.sort()
                    else:
                        self._keymap_syms[sym] = [(index, code)]
                index = index + 1
            code = code + 1

    def keysym_to_str(self, keysym):
        """
            convert a keysym to its equivalent character or
            key description and return it.
            Returns an empty for an unknown keysym.
            That's just a shortcut for :mod:`ooxcb.keysymdef`.
        """
        return sendkeys.keysymdef.names.get(keysym, '')

    def keysym_to_char(self, keysym):
        r"""SUMMARY

        keysym_to_char(keysym)

        @Arguments:
        - `keysym`:

        @Return:
        """
        # special keysyms
        if keysym in (0, 0x00ffffff):
            raise ConvertError("{} is a special keysym".format(keysym))
        # latin-1 keysyms
        elif (0x0020 <= keysym <= 0x007e or 0x00a0 <= keysym <= 0x00ff):
            return unichr(keysym)
        # unicode keysyms
        elif (0x01000100 <= keysym <= 0x0110ffff):
            return unichr(keysym - 0x01000000)
        # legacy keysyms
        elif keysym in sendkeys.keysymdef.legacy_keysyms:
            return unichr(sendkeys.keysymdef.legacy_keysyms[keysym])
        # dunno!
        else:
            raise ConvertError(
                "Unsupported keysym category or legacy keysym: {}"
                .format(keysym))

    def str_to_keysym(self, string):
        r"""SUMMARY

        str_keysym(char_)

        @Arguments:
        - `char_`:

        @Return:
        """
        if string in KeyboardMapping.specialchar_to_name:
            string = KeyboardMapping.specialchar_to_name.get(string)
        sym = sendkeys.keysymdef.keysyms.get(string, None)
        if sym is None:
            raise StrToSymError(string)
        return sym



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keymap.py ends here
