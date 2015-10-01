#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: nthweekday.py 242 2014-12-21 05:14:47Z t1 $
# $Revision: 242 $
# $Date: 2014-12-21 14:14:47 +0900 (Sun, 21 Dec 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-12-21 14:14:47 +0900 (Sun, 21 Dec 2014) $

r"""nthweekday -- DESCRIPTION

"""
from calendar import Calendar, MONDAY


class NthWeekDay(object):
    r"""SUMMARY
    """
    __calendar = Calendar(MONDAY)

    def __init__(self, year, month):
        r"""

        @Arguments:
        - `year`:
        - `month`:
        """
        self.year = year
        self.month = month
        self._calendar = self.__calendar.monthdatescalendar(year, month)

    def _has_first_week(self, weekday):
        r"""SUMMARY

        _has_first_week(weekday)

        @Arguments:
        - `weekday`:

        @Return:
        """
        for cday in self._calendar[0]:
            if cday.month == self.month and cday.weekday() == weekday:
                return True
        return False

    def get(self, weekday, nth):
        r"""SUMMARY

        get(weekday, nth)

        @Arguments:
        - `weekday`:
        - `nth`:

        @Return:
        """
        if self._has_first_week(weekday):
            nth -= 1
        return self._calendar[nth][weekday]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# nthweekday.py ends here
