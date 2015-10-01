#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _factory.py 460 2015-08-10 16:51:55Z t1 $
# $Revision: 460 $
# $Date: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $

r"""_factory -- DESCRIPTION

"""
from datetime import timedelta


class HolidayFactory(object):
    """Class HolidayFactory
    """
    # Attributes:
    def __init__(self, ):
        r"""
        """
        self.candidates = []

    # Operations
    def add_candidate(self, candidate):
        """function add_candidate

        candidate:

        returns
        """
        self.candidates.append(candidate)

    def remove_candidate(self, candidate):
        """function remove_candidate

        candidate:

        returns
        """
        self.candidates.remove(candidate)

    def has_candidate(self, candidate):
        """function has_candidate

        candidate:

        returns
        """
        return candidate in self.candidates

    def _elect_candidate(self, date, result):
        r"""SUMMARY

        _elect_candidate(date, result)

        @Arguments:
        - `date`:
        - `result`:

        @Return:

        @Error:
        """
        for candidate in self.candidates:
            if candidate.is_match_date(date):
                result[date] = candidate.get_name()

    def between_holidays(self, period):
        """function between_holidays

        start: date
        end:

        returns dict
        """
        start, end = period.get_start(), period.get_end()
        date, oneday = start, timedelta(1)
        result = {}
        while date < end:
            self._elect_candidate(date, result)
            date += oneday
        return result



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _factory.py ends here
