#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""scanner -- DESCRIPTION

"""
import string
from abc import ABCMeta, abstractmethod
from enumutil import AutoNumber
from xahk.input.keysymdef import KEYSYMS


REPLACES = [(r'\{\+'   ,'{plus'         ),
            (r'\\\+'   ,'{plus}'        ),
            (r'\{\!'   ,'{exclam'       ),
            (r'\\\!'   ,'{exclam}'      ),
            (r'\{\#'   ,'{numbersign'   ),
            (r'\\\#'   ,'{numbersign}'  ),
            (r'\{\^'   ,'{asciicircum'  ),
            (r'\\\^'   ,'{asciicircum}' ),
            (r'\{\_'   ,'{underscore'   ),
            (r'\_'     ,'{underscore}'  ),
            (r'\{\}\}' ,'{bracketright}'),
            (r'\{\}\ ' ,'{bracketright '),
            (r'\{\{\}' ,'{bracketleft}' ),
            (r'\{\{\ ' ,'{bracketleft ' ),
            # ('{{'    ,'{bracketleft}' ),
            (r'\\\{'   ,'{bracketleft}' ),
            (r'\\\}'   ,'{bracketright}'),
            (r'\"'     ,'{quotedbl}'    ),
            (r'\$'     ,'{dollar}'      ),
            (r'\%'     ,'{percent}'     ),
            (r'\&'     ,'{ampersand}'   ),
            (r"\'"     ,'{apostrophe}'  ),
            (r'\`'     ,'{quoteleft}'   ),
            (r'\('     ,'{parenleft}'   ),
            (r'\)'     ,'{parenright}'  ),
            (r'\~'     ,'{asciitilde}'  ),
            (r'\|'     ,'{bar}'         ),
            (r'\='     ,'{equal}'       ),
            (r'\*'     ,'{asterisk}'    ),
            (r'\>'     ,'{less}'        ),
            (r'\<'     ,'{greater}'     ),
            (r'\?'     ,'{question}'    ),
            (r'\-'     ,'{minus}'       ),
            (r'\,'     ,'{comma}'       ),
            (r'\.'     ,'{period}'      ),
            (r'\/'     ,'{slash}'       ),
            (r'\@'     ,'{at}'          ),
            (r'\:'     ,'{colon}'       ),
            (r'\;'     ,'{semicolon}'   ),
            (r'\['     ,'{braceleft}'   ),
            (r'\]'     ,'{braceright}'  ),
            (r'\\'     ,'{backslash}'   ),
            ]


class TokenType(AutoNumber):
    r"""TokenType

    TokenType is a Enum.
    Responsibility:
    """
    endmarker = () # '\0'
    key       = ()
    button    = ()
    modifier  = ()
    repeat    = ()
    behave    = ()
    geometry  = ()
    curly     = ()


class Token(object):
    r"""Token

    Token is a object.
    Responsibility:
    """
    def __init__(self, tokentype, value=None):
        r"""

        @Arguments:
        - `tokentype`:
        - `value`:
        """
        self.tokentype = tokentype
        self.value = value

    def getvalue(self, ):
        r"""SUMMARY

        getvalue()

        @Return:

        @Error:
        """
        return self.value

    def gettype(self, ):
        r"""SUMMARY

        gettype()

        @Return:

        @Error:
        """
        return self.tokentype

    def hasvalue(self, ):
        r"""SUMMARY

        hasvalue()

        @Return:

        @Error:
        """
        return self.value is not None

    def __contains__(self, elm):
        return elm in TokenType

    def __eq__(self, other):
        if not isinstance(other, (self.__class__, )):
            return False
        return (self.tokentype, self.value) == (other.tokentype, other.value)

    def __ne__(self, other):
        return not self == other

    def __nonzero__(self):
        return self.hasvalue()

    def __repr__(self):
        return ('{0.__class__.__name__}(type={1}, value={0.value})'
                .format(self, str(self.tokentype)))


class Tokenizer(object):
    r"""Tokenizer

    Tokenizer is a object.
    Responsibility:
    """
    def __init__(self, line, point=0):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.line = line + '\x00'
        self.point = point
        self.tokens = []
        self.in_curly = False

    def get_current_point(self, ):
        r"""SUMMARY

        get_current_point()

        @Return:

        @Error:
        """
        return self.point

    def get_char(self, point):
        r"""SUMMARY

        get_char(point)

        @Arguments:
        - `point`:

        @Return:

        @Error:
        """
        return self.line[point]

    def set_point(self, point):
        r"""SUMMARY

        set_point(point)

        @Arguments:
        - `point`:

        @Return:

        @Error:
        """
        self.point = int(point)

    def is_end(self, ):
        r"""SUMMARY

        is_end()

        @Return:

        @Error:
        """
        return self.get_char(self.get_current_point()) == '\x00'

    def list_tokens(self, ):
        r"""SUMMARY

        list_tokens()

        @Return:

        @Error:
        """
        return self.tokens

    def add_token(self, token):
        r"""SUMMARY

        add_token(token)

        @Arguments:
        - `token`:

        @Return:

        @Error:
        """
        self.tokens.append(token)

    def is_in_curly(self, ):
        r"""SUMMARY

        is_in_curly()

        @Return:

        @Error:
        """
        return self.in_curly

    def set_in_curly(self, ):
        r"""SUMMARY

        set_in_curly()

        @Return:

        @Error:
        """
        self.in_curly = True

    def unset_in_curly(self, ):
        r"""SUMMARY

        unset_in_curly()

        @Return:

        @Error:
        """
        self.in_curly = False


class TokenBuilder(object):
    r"""TokenBuilder

    TokenBuilder is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_match(self, tokenizer):
        r"""SUMMARY

        is_match(tokenizer)

        @Arguments:
        - `tokenizer`:

        @Return:

        @Error:
        """

    @abstractmethod
    def build_token(self, tokenizer):
        r"""SUMMARY

        build_token(tokenizer)

        @Arguments:
        - `tokenizer`:

        @Return:

        @Error:
        """


class KeyTokenBuilder(TokenBuilder):
    r"""KeyTokenBuilder

    KeyTokenBuilder is a TokenBuilder.
    Responsibility:
    """
    keys = string.ascii_letters + string.digits + ' '

    def is_match(self, tokenizer):
        r"""SUMMARY

        is_match(tokenizer)

        @Arguments:
        - `tokenizer`:

        @Return:

        @Error:
        """
        if tokenizer.is_in_curly():
            return False
        if tokenizer.get_char(tokenizer.get_current_point()) in self.keys:
            return True
        return False

    def build_token(self, tokenizer):
        r"""SUMMARY

        build_token(tokenizer)

        @Arguments:
        - `tokenizer`:

        @Return:

        @Error:
        """
        tokenizer.add_token(
            Token(TokenType.key, tokenizer.get_char(tokenizer.get_current_point())))
        tokenizer.set_point(tokenizer.get_current_point() + 1)


class KeywordTokenBuilder(TokenBuilder):
    r"""KeywordTokenBuilder

    KeywordTokenBuilder is a TokenBuilder.
    Responsibility:
    """
    keys = string.ascii_letters + string.digits
    key_words = KEYSYMS.keys()

    def is_match(self, tokenizer):
        r"""SUMMARY

        is_match(tokenizer)

        @Arguments:
        - `tokenizer`:

        @Return:

        @Error:
        """
        if not tokenizer.is_in_curly():
            return False
        tokens = tokenizer.list_tokens()
        if not tokens:
            return False
        if tokens[-1].gettype() != TokenType.curly:
            return False
        # parse button token
        point = tokenizer.get_current_point()
        word = ''
        while tokenizer.get_char(point) not in (' ', '}', '\x00'):
            word += tokenizer.get_char(point)
            point += 1
        if word in self.keys or word in self.key_words:
            return True
        return False

    def build_token(self, tokenizer):
        r"""SUMMARY

        build_token(tokenizer)

        @Arguments:
        - `tokenizer`:

        @Return:

        @Error:
        """
        point = tokenizer.get_current_point()
        word = ''
        while tokenizer.get_char(point) not in (' ', '}', '\x00'):
            word += tokenizer.get_char(point)
            point += 1
        tokenizer.add_token(Token(TokenType.key, word))
        tokenizer.set_point(point)
        # skip space
        while tokenizer.get_char(tokenizer.get_current_point()) == ' ':
            tokenizer.set_point(tokenizer.get_current_point() + 1)


class ModifierTokenBuilder(TokenBuilder):
    r"""ModifierTokenBuilder

    ModifierTokenBuilder is a TokenBuilder.
    Responsibility:
    """
    modifiers = ('+', '#', '!', '^')

    def is_match(self, tokenizer):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        if tokenizer.is_in_curly():
            return False
        if tokenizer.get_char(tokenizer.get_current_point()) in self.modifiers:
            return True
        return False

    def build_token(self, tokenizer):
        r"""SUMMARY

        build_token(tokenizer)

        @Arguments:
        - `tokenizer`:

        @Return:

        @Error:
        """
        point = tokenizer.get_current_point()
        char = tokenizer.get_char(point)
        tokenizer.add_token(Token(TokenType.modifier, char))
        tokenizer.set_point(point + 1)


class CurlyTokenBuilder(TokenBuilder):
    r"""CurlyTokenBuilder

    CurlyTokenBuilder is a TokenBuilder.
    Responsibility:
    """
    def is_match(self, tokenizer):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        if tokenizer.get_char(tokenizer.get_current_point()) in ('{', '}'):
            return True
        return False

    def build_token(self, tokenizer):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        char = tokenizer.get_char(tokenizer.get_current_point())
        tokenizer.add_token(Token(TokenType.curly, char))
        if char == '{':
            tokenizer.set_in_curly()
        elif char == '}':
            tokenizer.unset_in_curly()
        tokenizer.set_point(tokenizer.get_current_point() + 1)


class ButtonTokenBuilder(TokenBuilder):
    r"""ButtonTokenBuilder

    ButtonTokenBuilder is a TokenBuilder.
    Responsibility:
    """
    buttons = ('lbutton', 'lclick', 'rbutton', 'rclick', 'mbutton',
               'mclick', 'wheeldown', 'wheelup')

    def is_match(self, tokenizer):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        if not tokenizer.is_in_curly():
            return False
        tokens = tokenizer.list_tokens()
        if not tokens:
            return False
        if tokens[-1].gettype() != TokenType.curly:
            return False
        # parse button token
        point = tokenizer.get_current_point()
        word = ''
        while tokenizer.get_char(point) not in (' ', '}', '\x00'):
            word += tokenizer.get_char(point)
            point += 1
        word = word.lower()
        if word in self.buttons:
            return True
        return False

    def build_token(self, tokenizer):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        point = tokenizer.get_current_point()
        word = ''
        while tokenizer.get_char(point) not in (' ', '}', '\x00'):
            word += tokenizer.get_char(point)
            point += 1
        word = word.lower()
        tokenizer.add_token(Token(TokenType.button, word))
        tokenizer.set_point(point)
        # skip space
        while tokenizer.get_char(tokenizer.get_current_point()) == ' ':
            tokenizer.set_point(tokenizer.get_current_point() + 1)


class RepeatTokenBuilder(TokenBuilder):
    r"""RepeatTokenBuilder

    RepeatTokenBuilder is a TokenBuilder.
    Responsibility:
    """
    def is_match(self, tokenizer):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        if not tokenizer.is_in_curly():
            return False
        # return False, if last token is curly
        tokens = tokenizer.list_tokens()
        if not tokens:
            return False
        lasttoken = tokens[-1].gettype()
        if lasttoken in (TokenType.curly, TokenType.behave):
            return False
        point = tokenizer.get_current_point()
        word = ''
        while tokenizer.get_char(point) not in (' ', '}', '\x00'):
            word += tokenizer.get_char(point)
            point += 1
        word = word.lower()
        if not word.isdigit():
            return False
        # skip space
        while tokenizer.get_char(point) == ' ':
            point += 1
        point2 = point
        word2 = ''
        while tokenizer.get_char(point2) not in (' ', '}', '\x00'):
            word2 += tokenizer.get_char(point)
            point2 += 1
        if lasttoken == TokenType.button and word2.isdigit():
            return False
        if lasttoken in (TokenType.key, TokenType.button):
            return True
        if 2 <= len(tokens) and (
                lasttoken, tokens[-2]) == (TokenType.geometry, TokenType.geometry):
            return True
        return False

    def build_token(self, tokenizer):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        point = tokenizer.get_current_point()
        word = ''
        while tokenizer.get_char(point) not in (' ', '}', '\x00'):
            word += tokenizer.get_char(point)
            point += 1
        word = word.lower()
        if not word.isdigit():
            raise StandardError('not digits')
        tokenizer.add_token(Token(TokenType.repeat, int(word)))
        tokenizer.set_point(point)
        # skip space
        while tokenizer.get_char(tokenizer.get_current_point()) == ' ':
            tokenizer.set_point(tokenizer.get_current_point() + 1)


class BehaveTokenBuilder(TokenBuilder):
    r"""BehaveTokenBuilder

    BehaveTokenBuilder is a TokenBuilder.
    Responsibility:
    """
    behaves = ('press', 'release', 'up', 'down')

    def is_match(self, tokenizer):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        if not tokenizer.is_in_curly():
            return False
        tokens = tokenizer.list_tokens()
        if not tokens:
            return False
        lasttoken = tokens[-1].gettype()
        if lasttoken not in (TokenType.key, TokenType.button):
            return False
        point = tokenizer.get_current_point()
        word = ''
        while tokenizer.get_char(point) not in (' ', '}', '\x00'):
            word += tokenizer.get_char(point)
            point += 1
        word = word.lower()
        if word in self.behaves:
            return True
        return False

    def build_token(self, tokenizer):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        point = tokenizer.get_current_point()
        word = ''
        while tokenizer.get_char(point) not in (' ', '}', '\x00'):
            word += tokenizer.get_char(point)
            point += 1
        word = word.lower()
        tokenizer.add_token(Token(TokenType.behave, word))
        tokenizer.set_point(point)
        # skip space
        while tokenizer.get_char(tokenizer.get_current_point()) == ' ':
            tokenizer.set_point(tokenizer.get_current_point() + 1)


class GeometryTokenBuilder(TokenBuilder):
    r"""GeometryTokenBuilder

    GeometryTokenBuilder is a TokenBuilder.
    Responsibility:
    """
    def is_match(self, tokenizer):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        if not tokenizer.is_in_curly():
            return False
        tokens = tokenizer.list_tokens()
        if not tokens:
            return False
        if tokens[-1].gettype() != TokenType.button:
            return False
        point = tokenizer.get_current_point()
        word = ''
        while tokenizer.get_char(point) not in (' ', '}', '\x00'):
            word += tokenizer.get_char(point)
            point += 1
        # skip space
        while tokenizer.get_char(point) == ' ':
            point += 1
        point2 = point
        word2 = ''
        while tokenizer.get_char(point2) not in (' ', '}', '\x00'):
            word2 += tokenizer.get_char(point)
            point2 += 1
        if word2 == '':
            return False
        if word.isdigit() and word2.isdigit():
            return True
        return False

    def build_token(self, tokenizer):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        point = tokenizer.get_current_point()
        word = ''
        while tokenizer.get_char(point) not in (' ', '}', '\x00'):
            word += tokenizer.get_char(point)
            point += 1
        tokenizer.add_token(Token(TokenType.geometry, int(word)))
        # skip space
        while tokenizer.get_char(point) == ' ':
            point += 1
        point2 = point
        word2 = ''
        while tokenizer.get_char(point2) not in (' ', '}', '\x00'):
            word2 += tokenizer.get_char(point)
            point2 += 1
        tokenizer.add_token(Token(TokenType.geometry, int(word2)))
        tokenizer.set_point(point2)


#### Scanner
##
class Scanner(object):
    r"""Scanner

    Scanner is a object.
    Responsibility:
    """
    builders = (KeyTokenBuilder(),
                KeywordTokenBuilder(),
                ModifierTokenBuilder(),
                CurlyTokenBuilder(),
                ButtonTokenBuilder(),
                RepeatTokenBuilder(),
                # BehaveTokenBuilder(),
                GeometryTokenBuilder(),
    )

    def scan(self, line):
        r"""SUMMARY

        scan(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        tokenizer = Tokenizer(line)
        while not tokenizer.is_end():
            self._tokenize(tokenizer)
        return tokenizer.list_tokens()

    def _tokenize(self, tokenizer):
        r"""SUMMARY

        _tokenize(tokenizer)

        @Arguments:
        - `tokenizer`:

        @Return:

        @Error:
        """
        for builder in self.builders:
            if builder.is_match(tokenizer):
                builder.build_token(tokenizer)
                return
        raise StandardError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# scanner.py ends here
