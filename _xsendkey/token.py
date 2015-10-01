#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: token.py 390 2015-08-06 15:47:02Z t1 $
# $Revision: 390 $
# $Date: 2015-08-07 00:47:02 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 00:47:02 +0900 (Fri, 07 Aug 2015) $

r"""token -- DESCRIPTION

"""
from enumutil import AutoNumber


class TokenType(AutoNumber):
    r"""TokenType

    TokenType is a Enum.
    Responsibility:
    """
    endmarker = () # '\0'
    key       = ()
    button    = ()
    alt       = ()
    shift     = ()
    control   = ()
    hiper     = ()
    integer   = ()
    repeat    = ()
    press     = ()
    release   = ()
    geox      = ()
    geoy      = ()


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
        self._tokentype = TokenType(tokentype)
        self._value = value

    def getvalue(self, ):
        r"""SUMMARY

        getvalue()

        @Return:

        @Error:
        """
        return self._value

    def gettype(self, ):
        r"""SUMMARY

        gettype()

        @Return:

        @Error:
        """
        return self._tokentype

    def hasvalue(self, ):
        r"""SUMMARY

        hasvalue()

        @Return:

        @Error:
        """
        return self._value is not None

    def __contains__(self, elm):
        return elm in TokenType

    def __eq__(self, other):
        return self._tokentype == other

    def __ne__(self, other):
        return not self == other

    def __nonzero__(self):
        return self.hasvalue()

    def __repr__(self):
        return ('{0.__class__.__name__}(type={1}, value={0._value})'
                .format(self, str(self._tokentype)))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# token.py ends here
