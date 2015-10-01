#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: token.py 389 2015-08-06 15:46:41Z t1 $
# $Revision: 389 $
# $Date: 2015-08-07 00:46:41 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 00:46:41 +0900 (Fri, 07 Aug 2015) $

r"""token -- DESCRIPTION

"""

from enumutil import AutoNumber


class TokenType(AutoNumber):
    r"""TokenType

    TokenType is a AutoNumber.
    Responsibility:
    """
    endmarker = () # '\0'
    name = ()
    char = ()
    button = ()
    repeat = ()
    code = ()
    sym = ()
    unicode = ()
    modifier = ()
    behave = ()
    point = ()


class Token(object):
    r"""Token

    Token is a object.
    Responsibility:
    """
    __slots__ = ('types', 'value')

    def __init__(self, types, value=None):
        r"""

        @Arguments:
        - `types`:
        - `value`:
        """
        self.types = types
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
        return self.value

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
        return self.types == other

    def __ne__(self, other):
        return not self == other

    def __nonzero__(self):
        return self.hasvalue()

    def __repr__(self):
        return ('{0.__class__.__name__}(type={1}, value="{0.value}")'
                .format(self, str(self.types).split('.')[-1]))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# token.py ends here
