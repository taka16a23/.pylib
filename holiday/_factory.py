#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        date, oneday = period.get_start(), timedelta(1)
        result = {}
        while date < period.get_end():
            self._elect_candidate(date, result)
            date += oneday
        return result



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _factory.py ends here
