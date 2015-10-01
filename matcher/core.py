#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: core.py 307 2015-02-07 03:48:46Z t1 $
# $Revision: 307 $
# $Date: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $

r"""core -- DESCRIPTION

"""
from matcher import matches


class Matcher(object):
    r"""Matcher

    Matcher is a object.
    Responsibility:
    """
    matchers = {'startswith': matches.StartswithMatch,
                'endswith': matches.EndswithMatch,
                'search': matches.Search,
                'equal': matches.EqualMatch,
                'regexp': matches.RegexpMatch,
                }
    method = 'search' # default

    def __init__(self, string):
        r"""

        @Arguments:
        - `string`:
        """
        self._matcher = None
        self._set_matcher(string)

    @classmethod
    def set_method(cls, method):
        r"""SUMMARY

        set_method(method)

        @Arguments:
        - `method`:

        @Return:

        @Error:
        """
        if not method in cls.matchers:
            # TODO: (Atami) [2015/01/29]
            raise StandardError()
        cls.method = method

    def get_string(self, ):
        r"""SUMMARY

        get_string()

        @Return:

        @Error:
        """
        return self._matcher.get_string()

    def set_string(self, string):
        r"""SUMMARY

        set_string(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        self._matcher.set_string(string)

    string = property(get_string, set_string)

    def _set_matcher(self, string):
        r"""SUMMARY

        _set_matcher(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        self._matcher = self.matchers[self.method](string)

    def change_method(self, method):
        r"""SUMMARY

        change_method(method)

        @Arguments:
        - `method`:

        @Return:

        @Error:
        """
        Matcher.set_method(method)
        self._set_matcher(self.string)

    def match(self, string):
        r"""SUMMARY

        match(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        return self._matcher.match(string)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# core.py ends here
