#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""subscanner -- DESCRIPTION

"""
from xsendkey.token import TokenType, Token
from xcb2.xobj.key import Namesym, Key
import xsend


"""
{k 5}: send 'k' 5 times
{k press}: press 'k'
{Sym200} send 'keysym 200'
{U+3042} send unicode 3042
{ASC200} send ASCII code
{LClick 10} send LClick 10 times
{LClick 100 200} send LClick X100 Y200
"""



BEHAVE = {'press': TokenType.press,
          'down': TokenType.press,
          'release': TokenType.release,
          'up': TokenType.release,}


# TODO: (Atami) [2014/10/29]
BUTTON = {'lbutton':    0,
          'lclick':     0,
          'rbutton':    1,
          'rclick':     1,
          'mbutton':    2,
          'mclick':     2,
          'wheeldown':  3,
          'wheelup':    4,}


class ButtonSubscan(object):
    r"""ButtonCombination

    ButtonToken is a object.
    Responsibility:
    """
    def __init__(self, list_, index=0):
        r"""

        @Arguments:
        - `list_`:
        - `index`:
        """
        self._list = list_
        self._index = index

    def hasnext(self, ):
        r"""SUMMARY

        hasnext()

        @Return:

        @Error:
        """
        return self._index <= len(self._list) - 1

    def get_token1(self, ):
        r"""SUMMARY

        get_token1()

        @Return:

        @Error:
        """

        token = self._list[self._index]
        tkntype = BEHAVE.get(token, None)
        if tkntype is not None:
            return Token(tkntype)
        if token.isdigit():
            return Token(TokenType.repeat, int(token))
        # TODO: (Atami) [2014/10/30]
        raise StandardError()

    def get_token2(self, ):
        r"""SUMMARY

        get_token2()

        @Return:

        @Error:
        """
        if 0 == self._index:
            return Token(TokenType.geox, int(self._list[self._index]))
        if 1 == self._index:
            return Token(TokenType.geoy, int(self._list[self._index]))
        # TODO: (Atami) [2014/10/30]
        raise StandardError()

    def get_token3(self, ):
        r"""SUMMARY

        get_token3()

        @Return:

        @Error:
        """
        if self._index in (0, 1):
            return self.get_token2()
        if 2 == self._index:
            return self.get_token1()
        # TODO: (Atami) [2014/10/30]
        raise StandardError()

    def get_token(self, ):
        r"""SUMMARY

        get_token()

        @Return:

        @Error:
        """
        length = len(self._list)
        if 1 == length:
            return self.get_token1()
        if 2 == length:
            return self.get_token2()
        if 3 == length:
            return self.get_token3()
        raise StandardError()

    def __iter__(self):
        self._index = 0
        return self

    def next(self, ):
        if not self.hasnext():
            raise StopIteration()
        token = self.get_token()
        self._index += 1
        return token


class KeySubscan(object):
    r"""KeyCombination

    KeyCombination is a object.
    Responsibility:
    """
    def __init__(self, list_, index=0):
        r"""

        @Arguments:
        - `list_`:
        - `index`:
        """
        self._list = list_
        self._index = index

    def hasnext(self, ):
        r"""SUMMARY

        hasnext()

        @Return:

        @Error:
        """
        return self._index <= len(self._list) - 1

    def get_token1(self, ):
        r"""SUMMARY

        get_token1()

        @Return:

        @Error:
        """
        token = self._list[self._index]
        tkntype = BEHAVE.get(token, None)
        if tkntype is not None:
            return Token(tkntype)
        if token.isdigit():
            return Token(TokenType.repeat, int(token))
        raise StandardError()

    def get_token(self, ):
        r"""SUMMARY

        get_token()

        @Return:

        @Error:
        """
        length = len(self._list)
        if 1 == length:
            return self.get_token1()
        raise StandardError()

    def __iter__(self):
        self._index = 0
        return self

    def next(self, ):
        if not self.hasnext():
            raise StopIteration()
        token = self.get_token()
        self._index += 1
        return token


class Subscanner(object):
    r"""CurlyScanner

    CurlyScanner is a object.
    Responsibility:
    """
    # TODO: (Atami) [2014/10/29]
    button = {'lbutton':   0,
              'lclick':    0,
              'rbutton':   1,
              'rclick':    1,
              'mbutton':   2,
              'mclick':    2,
              'wheeldown': 3,
              'wheelup':   4,}

    def __init__(self, line):
        r"""

        @Arguments:
        - `line`:
        """
        self._line = line
        self._sub = None

    def hasnext(self, ):
        r"""SUMMARY

        hasnext()

        @Return:

        @Error:
        """
        return self._sub is None or self._sub.hasnext()

    def list_phrase(self, ):
        r"""SUMMARY

        list_phrase()

        @Return:

        @Error:
        """
        phrases = self._line.split(' ')
        while '' in phrases:
            phrases.remove('')
        return phrases

    def get_token(self, phrase):
        r"""SUMMARY

        get_token(phrase)

        @Arguments:
        - `phrase`:

        @Return:

        @Error:
        """
        lower = phrase.lower()
        # button
        if lower in self.button:
            return Token(TokenType.button, self.button[lower])
        # Code
        if phrase.startswith('Code'):
            val = phrase.replace('Code', '')
            if not val.isdigit():
                # TODO: (Atami) [2014/10/30]
                raise StandardError(val)
            return Token(TokenType.key, xsend.KeySend(Key(int(val))))
        # unicode
        if phrase.startswith('Uni'):
            # TODO: (Atami) [2014/10/29]
            return Token(TokenType.key, phrase.replace('uni', ''))
        # symbol name
        namesym = Namesym(phrase)
        if not namesym.isdefined():
            # TODO: (Atami) [2014/10/28]
            raise SyntaxError('"{}" not defined symbol name'.format(phrase))
        key = Namesym(namesym).to_sym().to_key()
        return Token(TokenType.key, xsend.KeySend(key))

    def get_sub_token(self, type_, list_):
        r"""SUMMARY

        get_sub_token(type_)

        @Arguments:
        - `type_`:

        @Return:

        @Error:
        """
        if type_ == TokenType.button:
            return ButtonSubscan(list_)
        if type_ in (TokenType.key, ):
            return KeySubscan(list_)
        raise StandardError()

    def __iter__(self):
        self._sub = None
        return self

    def next(self, ):
        if not self._sub is None:
            return self._sub.next()
        lis = self.list_phrase()
        token = self.get_token(lis[0])
        self._sub = self.get_sub_token(token, lis[1:])
        return token



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# subscanner.py ends here
