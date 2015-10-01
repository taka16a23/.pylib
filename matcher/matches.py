#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: matches.py 307 2015-02-07 03:48:46Z t1 $
# $Revision: 307 $
# $Date: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $

r"""matches -- DESCRIPTION

"""
from re import _pattern_type, compile as recompile
from abc import ABCMeta, abstractmethod


class MatchAbstract(object):
    r"""MatchAbstract

    MatchAbstract is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_string(self, ):
        pass

    @abstractmethod
    def match(self, string):
        pass


class _StringMatch(MatchAbstract):
    r"""_StringMatch

    _StringMatch is a MatchAbstract.
    Responsibility:
    """
    def __init__(self, string):
        r"""

        @Arguments:
        - `string`:
        """
        self._string = None
        self.set_string(string)

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
        self._string = str(string)

    string = property(get_string, set_string)


class StartswithMatch(_StringMatch):
    r"""StartsWithMatch

    StartswithMatch is a MatchAbstract.
    Responsibility:

    前方一致
    """
    def match(self, string):
        r"""SUMMARY

        match(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        return str(string).startswith((self.string, ))


class EndswithMatch(_StringMatch):
    r"""EndswithMatch

    EndswithMatch is a MatchAbstract.
    Responsibility:

    後方一致
    """
    def match(self, string):
        r"""SUMMARY

        match(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        return str(string).endswith((self.string))


class Search(_StringMatch):
    r"""Search

    Search is a MatchAbstract.
    Responsibility:

    部分一致
    """
    def match(self, string):
        r"""SUMMARY

        match(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        return self.string in str(string)


class EqualMatch(_StringMatch):
    r"""EqualMatch

    EqualMatch is a MatchAbstract.
    Responsibility:

    完全一致
    """
    def match(self, string):
        r"""SUMMARY

        match(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        return self.string == str(string)


class RegexpMatch(MatchAbstract):
    r"""RegexpMatch

    RegexpMatch is a MatchAbstract.
    Responsibility:

    正規表現
    """
    def __init__(self, string):
        r"""

        @Arguments:
        - `string`:
        """
        self._regexp = None
        self.set_string(string)

    def get_string(self, ):
        r"""SUMMARY

        get_string()

        @Return:

        @Error:
        """
        return self._regexp.pattern

    def set_string(self, string):
        r"""SUMMARY

        set_string(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        self._regexp = recompile(string)

    string = property(get_string, set_string)

    def get_regexp(self, ):
        r"""SUMMARY

        get_regexp()

        @Return:

        @Error:
        """
        return self._regexp

    def set_regexp(self, regexp):
        r"""SUMMARY

        set_regexp(regexp)

        @Arguments:
        - `regexp`:

        @Return:

        @Error:
        """
        if not isinstance(regexp, (_pattern_type, )):
            # TODO: (Atami) [2015/01/29]
            raise TypeError()
        self._regexp = regexp

    regexp = property(get_regexp, set_regexp)

    def match(self, string):
        r"""SUMMARY

        match(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        return self._regexp.match(string) is not None



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# matches.py ends here
