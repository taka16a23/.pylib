#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""core -- part a keymap

"""

import sys as _sys
import os as _os
import re as _re

from t1.dictutil import DictUtil

from keymap.posix.dumpkeys import DumpKeys
from keymap.posix.error import UnpackError

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'

RENAME_MAP = {'one':          '1',
              'two':          '2',
              'three':        '3',
              'four':         '4',
              'five':         '5',
              'six':          '6',
              'seven':        '7',
              'eight':        '8',
              'nine':         '9',
              'zero':         '0',
              'ntilde':       'ñ',
              'comma':        ',',
              'minus':        '-',
              'space':        ' ',
              'period':       '.',
              'colon':        ':',
              'semicolon':    ';',
              'at':           '@',
              'bracketleft':  '[',
              'bracketright': ']',
              'slash':        '/',
              'backslash':    '\\',
              'exclam':       '!',
              'quotedbl':     '"',
              'numbersign':   '#',
              'dollar':       '$',
              'percent':      '%',
              'ampersand':    '&',
              'apostrophe':   "'",
              'parenleft':    '(',
              'parenright':   ')',
              'underscore':   '_',
              'plus':         '+',
              'asciitilde':   '~',
              'grave':        '`',
              'asciicircum':  '^',
              'equal':        '=',
              'asterisk':     '*',
              'less':         '<',
              'greater':      '>',
              'question':     '?',
              'braceleft':    '{',
              'braceright':   '}',
              'bar':          '|',
              }

SPECIAL_KEY_FMT = '<{}>'
SPECIAL_UPKEY_FMT = r'<\{}>'


class KeyMap(DictUtil):
    r"""Plain keymap dictionary <int, str>.

    @Arguments:
    - `voidsymbol`: replace 'VoidSymbol' string.
    """
    _rename_map = RENAME_MAP
    _special_fmt = SPECIAL_KEY_FMT
    _regexp = '^plain'

    def __init__(self, voidsymbol='', rename=True):
        self.voidsymbol = voidsymbol
        self._rename_flag = rename
        self._parse_dumpkeys()

    def reload(self, ):
        r"""Reload keymap.

        reload()
        """
        self.clear()
        self._parse_dumpkeys()

    def _parse_dumpkeys(self, ):
        r"""Parse and set dictionary keycode, char from dumpkeys.

        _parse_dumpkeys()
        """
        for line in self._iter_lines():
            keycode, char = self._parse_line(line)
            if self._rename_flag:
                char = self._filter_char(char)
            self.setmap(keycode, char)

    def _iter_lines(self, ):
        r"""Generator each matched line from dumpkeys command.

        _iter_lines()

        @Return:
        yield line.
        """
        for line in DumpKeys():
            if self._ismatch_line(line):
                yield line

    def _ismatch_line(self, line):
        r"""Check matched line.

        _ismatch_line(line)

        @Arguments:
        - `line`: target statements

        @Return:
        None, if not matched.
        match object, if matched.
        """
        return _re.search(self._regexp, line)

    def _parse_line(self, line):
        r"""Parse keycode and char from line.

        _parse_line(line)

        @Arguments:
        - `line`: (str)

        @Return:
        int, str

        Split statements to list by space.
        'plain\tkeycode 255 = VoidSymbol\n'
        => ['plain\tkeycode', '255', '=', 'VoidSymbol', '\n']
        """
        try:
            _, keycode, _, char, _ = [x for x in line.split(' ') if not x == '']
        except ValueError, err:
            raise UnpackError(err)
        return keycode, char

    def _filter_char(self, char):
        r"""Filtering char.

        _filter_char(char)

        @Arguments:
        - `char`: (str)

        @Return:
        str
        """
        if char.startswith(('+')):
            char = char[1:]
        elif char in self._rename_map:
            char = self._rename_map[char]
        elif char == 'VoidSymbol':
            char = self.voidsymbol
        else:
            char = self._special_fmt.format(char)
        return char

    def setmap(self, keycode, char):
        r"""Alternative set dictionary for this.

        setmap(keycode, char)

        @Arguments:
        - `keycode`: int
        - `char`: str
        """
        self[int(keycode)] = char


class KeyUpMap(KeyMap):
    r"""For Key up dictionary."""
    _special_fmt = SPECIAL_UPKEY_FMT


class KeyShiftMap(KeyMap):
    r"""For Modifier key shift dictionary."""
    _special_fmt = SPECIAL_KEY_FMT
    _regexp = r'^[\t\s]+shift[\t\s]+keycode'


class KeyMapAbstract(object):
    r"""
    """

    def __init__(self, ):
        r"""
        """
        self._keymap = KeyMap()

    def getkey(self, keycode):
        r"""SUMMARY

        getkey(keycode)

        @Arguments:
        - `keycode`:

        @Return:
        """
        return self._keymap.get(keycode, '')

    def getmatchkeys(self, value):
        r"""SUMMARY

        getmatchkeys(vlaue)

        @Arguments:
        - `vlaue`:

        @Return:
        """
        results = []
        for key, val in self._keymap.iteritems():
            if value == val:
                results.append(key)
        return results


class KeyMapUpAbstract(object):
    r"""
    """
    def __init__(self, ):
        r"""
        """
        self._keyupmap = KeyUpMap()

    def getupkey(self, keycode):
        r"""SUMMARY

        getshiftkey(keycode)

        @Arguments:
        - `keycode`:

        @Return:
        """
        return self._keyupmap.get(keycode, '')


class KeyMapShiftAbstract(object):
    r"""
    """

    def __init__(self, ):
        r"""
        """
        self._shiftmap = KeyShiftMap()

    def getshiftkey(self, keycode):
        r"""SUMMARY

        getshiftkey(keycode)

        @Arguments:
        - `keycode`:

        @Return:
        """
        return self._shiftmap.get(keycode, '')


class KeyMaps(KeyMapAbstract, KeyMapUpAbstract, KeyMapShiftAbstract):
    r"""Key Maps."""

    def __init__(self, ):
        r"""
        """
        KeyMapAbstract.__init__(self)
        KeyMapUpAbstract.__init__(self)
        KeyMapShiftAbstract.__init__(self)

KEYMAPS = KeyMaps()


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# core.py ends here
