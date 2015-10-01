#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""tokens -- DESCRIPTION

"""
from enum import Enum

from sendkeys.display import KeymapDisplay
from sendkeys import stoken
from sendkeys.analyze import Analyzer



class GeoFlag(Enum):
    r"""SUMMARY
    """
    NONE = 0
    X = 1
    Y = 2


class Tokenize(KeymapDisplay):
    r"""SUMMARY
    """

    def __init__(self, replacer, display=None):
        r"""

        @Arguments:
        - `line`:
        - `display`:
        """
        KeymapDisplay.__init__(self, display)
        self.replacer = replacer
        self._iter = None
        self._buttonflag = False

    def get_analyze(self, ):
        r"""SUMMARY

        analyze()

        @Return:
        """
        return Analyzer(self, self.display)

    def listtokens(self, ):
        r"""SUMMARY

        listtokens()

        @Return:
        """
        return list(self.itertokenize())

    def itertokenize(self, ):
        r"""SUMMARY

        tokenize()

        @Return:
        """
        self._iter = iter(self.replacer)
        while 1:
            char = self._iter.next()
            if '{' == char:
                yield stoken.TokenCurlystart(char)
                for token in self._parse_curly():
                    yield token
            else:
                if char in ('^', '+',  '!', '#'):
                    yield stoken.TokenModifier(char)
                else:
                    yield stoken.TokenKey(char)

    def _getcurly_token(self, token):
        r"""SUMMARY

        _dispatch_curly_token()

        @Return:
        """
        if token.isdigit():
            if self._buttonflag == GeoFlag.X:
                self._buttonflag = GeoFlag.Y
                return stoken.TokenGeoX(token, self.display)
            elif self._buttonflag == GeoFlag.Y:
                self._buttonflag = GeoFlag.NONE
                return stoken.TokenGeoY(token, self.display)
            return stoken.TokenRepeat(token, self.display)
        elif 'down' == token:
            return stoken.TokenKeydown(token, self.display)
        elif 'up' == token:
            return stoken.TokenKeyup(token, self.display)
        # elif: unicode
            # return stoken.TokenUnicode(token)
        # elif: keycode
            # return stoken.TokenKeycode(token)
        elif token in ('LButton', 'LClick', 'RButton', 'RClick', 'MButton',
                       'MClick', 'WheelDown', 'WheelUp'):
            self._buttonflag = GeoFlag.X
            return stoken.TokenButton(token, self.display)
        else:
            self._buttonflag = GeoFlag.NONE
            return stoken.TokenKey(token, self.display)

    def _parse_curly(self, ):
        r"""SUMMARY

        _parse_into_curly()

        @Return:
        """
        string = ''
        while 1:
            char = self._iter.next()
            if char in ('}', ' '):
                yield self._getcurly_token(string)
                string = ''
                if '}' == char:
                    yield stoken.TokenCurlyend(char, self.display)
                    break
            else:
                string += char
        raise StopIteration()

    def __iter__(self, ):
        return iter(self.itertokenize())

    def __repr__(self, ):
        return "{0.__class__.__name__}('{0.replacer}')".format(self)

    def __str__(self, ):
        return self.replacer()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# tokens.py ends here
