#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""token -- DESCRIPTION

構文に変更があった場合ここを変更すること。
TokenTypes に変更があれば、analyzer.py を編集すること。
"""
from enum import Enum
from collections import OrderedDict


class TokenTypes(Enum):
    r"""TokenTypes

    TokenTypes is a Enum.
    Responsibility:
    """
    KEY_NAME = 1
    BUTTON_NAME = 2
    KEYCODE = 3
    BUTTONCODE = 4
    MODIFIER = 5
    BEHAVE = 6
    REPEAT = 7
    POINT = 8


class Token(object):
    r"""Token

    Token is a object.
    Responsibility:
    """
    __slots__ = ('types', 'value')

    def __init__(self, types, value):
        r"""

        @Arguments:
        - `types`:
        - `value`:
        """
        self.types = types
        self.value = value

    def get_types(self, ):
        r"""SUMMARY

        get_types()

        @Return:

        @Error:
        """
        return self.types

    def get_value(self, ):
        r"""SUMMARY

        get_value()

        @Return:

        @Error:
        """
        return self.value

    def equal_types(self, types):
        r"""SUMMARY

        equal_types(types)

        @Arguments:
        - `types`:

        @Return:

        @Error:
        """
        return self.types == types

    def equal(self, token):
        r"""SUMMARY

        equal(token)

        @Arguments:
        - `token`:

        @Return:

        @Error:
        """
        return self.equal_types(token.get_types()) and self.value == token.get_value()

    def __repr__(self):
        return ('{0.__class__.__name__}(types={0.types.name}, value="{0.value}")'
                .format(self))


REPLACE_MAP = OrderedDict([('{+'  , '{plus'          ),
                           ('\\+' , '{plus}'         ),
                           ('{!'  , '{exclam'        ),
                           ('\\!' , '{exclam}'       ),
                           ('{#'  , '{numbersign'    ),
                           ('\\#' , '{numbersign}'   ),
                           ('{^'  , '{asciicircum'   ),
                           ('\\^' , '{asciicircum}'  ),
                           ('{_'  , '{underscore'    ),
                           ('\\_' , '{underscore}'   ),
                           ('{}}' , '{bracketright}' ),
                           ('{} ' , '{bracketright ' ),
                           ('{{}' , '{bracketleft}'  ),
                           ('{{ ' , '{bracketleft '  ),
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


class Tokenizer(object):
    r"""Tokenizer

    Tokenizer is a object.
    Responsibility:
    """
    _modifiers = ('+', '!', '#', '^')
    _buttons = ('lbutton', 'mbutton', 'rbutton', 'lclick', 'mclick', 'rclick',
                'wheelup', 'weeldown')

    def __init__(self, string):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._string = None
        self.set_string(string) # triming
        self._index = 0
        self._inparen = False

    def __iter__(self):
        self._index = 0
        self._inparen = False
        return self

    def _parse_paren(self, ):
        r"""SUMMARY


        @Return:

        @Error:
        """
        start = self._index
        # increment to end of query
        while self._string[self._index] not in (' ', '}'):
            self._index += 1
        if self._string[self._index] == '}':
            self._inparen = False
        # behave
        query = self._string[start:self._index]
        if query.lower() in ('press', 'release'):
            self._index += 1
            return Token(TokenTypes.BEHAVE, query)
        # point
        if '-' in query:
            self._index += 1
            return Token(TokenTypes.POINT, query)
        if self._string[start-1] == '{':
            if query.isdigit():
                # code
                if int(query) <= 5:
                    self._index += 1
                    return Token(TokenTypes.BUTTONCODE, query)
                self._index += 1
                return Token(TokenTypes.KEYCODE, query)
            # button
            if query.lower() in self._buttons:
                self._index += 1
                return Token(TokenTypes.BUTTON_NAME, query)
            self._index += 1
            return Token(TokenTypes.KEY_NAME, query)
        # repeat
        if query.isdigit():
            self._index += 1
            return Token(TokenTypes.REPEAT, query)

    def next(self, ):
        if len(self._string) <= self._index:
            raise StopIteration()
        # check in paren
        if self._string[self._index] == '{':
            self._index += 1
            self._inparen = True
        # parse in paren
        if self._inparen:
            return self._parse_paren()
        # parse outside paren
        char = self._string[self._index]
        if char in self._modifiers:
            self._index += 1
            return Token(TokenTypes.MODIFIER, char)
        self._index += 1
        return Token(TokenTypes.KEY_NAME, char)

    def get_string(self, ):
        r"""SUMMARY

        get_string()

        @Return:

        @Error:
        """
        return self._string

    def set_string(self, string):
        r"""SUMMARY

        set_string(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        line = string
        for key in REPLACE_MAP.keys():
            if key in line:
                line = line.replace(key, REPLACE_MAP[key])
        self._string = line

    def count_tokens(self, ):
        r"""SUMMARY

        count_tokens()

        @Return:

        @Error:
        """
        return len(list(self))

    def list_tokens(self, ):
        r"""SUMMARY

        list_tokens()

        @Return:

        @Error:
        """
        return list(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# token.py ends here
