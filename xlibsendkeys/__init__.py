#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import sys
from collections import OrderedDict

import Xlib
from Xlib import XK
from Xlib import X
from Xlib.display import Display
from Xlib.ext.xtest import fake_input

from dotavoider import ListDotAvoider
if sys.version_info < (2, 4):
    from sets import Set as set




__version__ = "0.1.0"

__all__ = [ '' ]


SPECIALKEY_NAME_MAP = {
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

UPSTRINGS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             'exclam',       # '!'
             'quotedbl',     # '"'
             'numbersign',   # '#'
             'dollar',       # '$'
             'percent',      # '%'
             'ampersand',    # '&'
             'apostrophe',   # '''
             'quoteright',   # '''
             'grave',        # '`'
             'quoteleft',    # '`'
             'parenleft',    # '('
             'parenright',   # ')'
             'underscore',   # '_'
             'plus',         # '+'
             'asciitilde',   # '~'
             'bar',          # '|'
             'bracketleft',  # '{'
             'bracketright', # '}'
             'equal',        # '='
             'asterisk',     # '*'
             'less',         # '>'
             'greater',      # '<'
             'question',     # '?'
             ]


class KeyAbstract(object):
    r"""SUMMARY
    """

    def __init__(self, display, data):
        r"""

        @Arguments:
        - `display`:
        - `data`:
        """
        self._display = display
        self._data = data

    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            return cmp(self._data, other._data)
        return cmp(self._data, other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._data == other._data
        return self._data == other

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self, ):
        return '{0.__class__.__name__}({1})'.format(self, int(self))


class KeyIntegerAbstract(KeyAbstract):
    r"""SUMMARY
    """

    def __ini__(self, ):
        return self._data

    def __repr__(self, ):
        return '{0.__class__.__name__}({1})'.format(self, self._data)


class KeyStringAbstract(KeyAbstract):
    r"""SUMMARY
    """

    def __str__(self, ):
        return self._data

    def __repr__(self, ):
        return "{0.__class__.__name__}('{1}')".format(self, self._data)


class Keycode(KeyIntegerAbstract):
    r"""SUMMARY
    """

    def press_key(self, time=0, root=0, x=0, y=0):
        r"""SUMMARY

        press()

        @Return:
        """
        fake_input(self._display, X.KeyPress, self._data, time, root, x, y)

    def release_key(self, time=0, root=0, x=0, y=0):
        r"""SUMMARY

        release(time=0, root=0, x=0, y=0)

        @Arguments:
        - `time`:
        - `root`:
        - `x`:
        - `y`:

        @Return:
        """
        fake_input(self._display, X.KeyRelease, self._data, time, root, x, y)

    def to_keysym(self, index=0):
        r"""SUMMARY

        @Arguments:
        - `index`:

        @Return:

        to_keysym()

        Convert a keycode to a keysym, looking in entry index.
        Normally index 0 is unshifted, 1 is shifted, 2 is alt grid, and 3
        is shift+alt grid. If that key entry is not bound, X.NoSymbol is
        returned.
        """
        keysym = self._display.keycode_to_keysym(self._data, index)
        return Keysym(self._display, keysym)


class Keysym(KeyIntegerAbstract):
    r"""SUMMARY
    """

    def to_keycode(self, ):
        r"""SUMMARY

        to_keycode()

        @Return:
        """
        code = self._display.keysym_to_keycode(self._data)
        return Keycode(self._display, code)

    def to_string(self, ):
        r"""SUMMARY

        to_string()

        @Return:
        """
        return Keystring(self._display, XK.keysym_to_string(self._data))

    def press_key(self, time=0, root=0, x=0, y=0):
        r"""SUMMARY

        key_press()

        @Return:
        """
        self.to_keycode().press_key(time, root, x, y)

    def release_key(self, time=0, root=0, x=0, y=0):
        r"""SUMMARY

        release_key()

        @Return:
        """
        self.to_keycode().release_key(time, root, x, y)


class Keystring(KeyStringAbstract):
    r"""SUMMARY
    """

    def to_keysym(self, ):
        r"""SUMMARY

        to_keysym()

        @Return:
        """
        keysym = XK.string_to_keysym(self._data)
        return Keysym(self._display, keysym)

    def press_key(self, time=0, root=0, x=0, y=0):
        r"""SUMMARY

        press_key()

        @Return:
        """
        self.to_keysym().press_key(time, root, x, y)

    def release_key(self, time=0, root=0, x=0, y=0):
        r"""SUMMARY

        release_key()

        @Return:
        """
        self.to_keysym().release_key(time, root, x, y)


REPLACE_MAP = OrderedDict([('{+'  , '{plus'          ),
                           ('\\+' , '{plus}'         ),
                           ('{!'  , '{exclam'        ),
                           ('\\!' , '{exclam}'       ),
                           ('{#'  , '{numbersign'    ),
                           ('\\#' , '{numbersign}'   ),
                           ('{^'  , '{asciicircum'   ),
                           ('\\^' , '{asciicircum}'  ),
                           ('{}}' , '{bracketright}' ),
                           ('{{}' , '{bracketleft}'  ),
                           # ('{{'  , '{bracketleft}'  ),
                           ('\\{' , '{bracketleft}'  ),
                           ('\\}' , '{bracketright}' ),
                           ('\"'  , '{quotedbl}'     ),
                           ('$'   , '{dollar}'       ),
                           ('%'   , '{percent}'      ),
                           ('&'   , '{ampersand}'    ),
                           ("'"   , '{apostrophe}'   ),
                           ('`'   , '{quoteleft}'    ),
                           ('('   , '{parenleft}'    ),
                           (')'   , '{parenright}'   ),
                           ('_'   , '{underscore}'   ),
                           ('~'   , '{asciitilde}'   ),
                           ('|'   , '{bar}'          ),
                           ('='   , '{equal}'        ),
                           ('*'   , '{asterisk}'     ),
                           ('>'   , '{less}'         ),
                           ('<'   , '{greater}'      ),
                           ('?'   , '{question}'     ),
                           ('-'   , '{minus}'        ),
                           (','   , '{comma}'        ),
                           ('.'   , '{period}'       ),
                           ('/'   , '{slash}'        ),
                           ('@'   , '{at}'           ),
                           (':'   , '{colon}'        ),
                           (';'   , '{semicolon}'    ),
                           ('['   , '{braceleft}'    ),
                           (']'   , '{braceright}'   ),
                           ('\\'  , '{backslash}'    ),
                           ])


class SendKeyInfo(object):
    r"""SUMMARY
    """

    def __init__(self, modifiers='', keys=None):
        r"""

        @Arguments:
        - `modifiers`:
        - `key`:
        """
        self.modifiers = set(modifiers)
        self.keys = keys or []

    def __repr__(self, ):
        fmt = ('{0.__class__.__name__}'
               '(modifiers={1}, keys={0.keys})').format
        return fmt(self, repr(self.modifiers).replace('set', '', 1))


class Analyzer(object):
    r"""SUMMARY
    """
    _loaded = False
    _ctrl, _shift, _alt, _win = None, None, None, None

    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        self._display = display
        self._sendkey_info = SendKeyInfo()
        self._load_key()

    def _load_key(self, ):
        r"""SUMMARY

        _load_key()

        @Return:
        """
        if self._loaded:
            return
        self._ctrl = Keysym(self._display, XK.XK_Control_L)
        self._shift = Keysym(self._display, XK.XK_Shift_L)
        self._alt = Keysym(self._display, XK.XK_Alt_L)
        self._win = Keysym(self._display, XK.XK_Super_L)
        self._loaded = True

    def analyze(self, tokens):
        r"""SUMMARY

        analyze(tokens)

        @Arguments:
        - `tokens`:

        @Return:
        """
        exlist, append = ListDotAvoider().append
        for token in tokens:
            analized = self.analize_token(token)
            if isinstance(analized, Keysym):
                self._sendkey_info.modifiers.add(analized)
            elif analized in UPSTRINGS:
                self._sendkey_info.modifiers.add(self._shift)
                self._sendkey_info.keys.append(analized)
                append(self._sendkey_info)
                self._sendkey_info = SendKeyInfo() # clear
            else:
                self._sendkey_info.keys.append(analized)
                append(self._sendkey_info)
                self._sendkey_info = SendKeyInfo() # clear
        return exlist

    def analize_token(self, token):
        r"""SUMMARY

        analize_token()

        @Return:
        """
        if '^' == token:
            return self._ctrl
        elif '+' == token:
            return self._shift
        elif '!' == token:
            return self._alt
        elif '#' == token:
            return self._win
        else:
            return Keystring(self._display, token)

    def __call__(self, token):
        return self.analyze(token)


class KeyLineParser(KeyStringAbstract):
    r"""SUMMARY
    """

    def __init__(self, display, line):
        r"""SUMMARY

        __init__(display, line)

        @Arguments:
        - `display`:
        - `line`:

        @Return:
        """
        KeyStringAbstract.__init__(self, display, line)
        self.analizer = Analyzer(self._display)

    def parse_line(self, ):
        r"""SUMMARY

        parse_line()

        @Return:
        """
        tokens = tokenize(replacer(self._data))
        return self.analizer(tokens)


def replacer(line):
    r"""SUMMARY

    replacer(line)

    @Arguments:
    - `line`:

    @Return:
    """
    for key in REPLACE_MAP.keys():
        if key in line:
            line = line.replace(key, REPLACE_MAP[key])
    return line


def tokenize(line):
    r"""SUMMARY

    tokenize(line)

    @Arguments:
    - `line`:

    @Return:
    """
    replaced = replacer(line)

    result_list, append = ListDotAvoider().append
    lineiter = iter(replaced)
    while 1:
        try:
            char = lineiter.next()
            if '{' == char:
                string = ''
                while 1:
                    key = lineiter.next()
                    if '}' == key:
                        break
                    else:
                        string += key
                append(string)
            else:
                append(char)
        except StopIteration:
            break
    return result_list


class SendKeys(object):
    r"""SUMMARY
    """

    def __init__(self, display, line):
        r"""

        @Arguments:
        - `display`:
        - `line`:
        """
        self._display = display
        self._line = line

    def sendkeys(self, ):
        r"""SUMMARY

        sendkeys()

        @Return:
        """
        keys = KeyLineParser(self._display, self._line).parse_line()
        for key in keys:
            for mod in key.modifiers:
                mod.press_key()
            for ky in key.keys:
                ky.press_key()
                ky.release_key()
            for mod in key.modifiers:
                mod.release_key()
            self._display.sync()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
