#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""yearly_week_nth -- DESCRIPTION

"""
import calendar

from holiday._holiday.abstract import Holiday


def get_weeknth(year, month, nth, weekday):
    r"""SUMMARY

    get_weeknth(year, month, nth, weekday)

    @Arguments:
    - `year`:
    - `month`:
    - `nth`:
    - `weekday`:

    @Return:

    @Error:
    """
    cal = calendar.Calendar(calendar.MONDAY).monthdatescalendar(year, month)
    nthed = nth
    # calc first week has weekday
    for day in cal[0]:
        if day.month == month and day.weekday() == weekday:
            nthed -= 1
            break
    return cal[nthed][weekday]


class YearlyWeekNthHoliday(Holiday):
    """Class YearlyWeekNthHoliday
    """
    # Attributes:
    def __init__(self, period, month, weekday, nth, name):
        r"""

        @Arguments:
        - `start`:
        - `end`:
        - `month`:
        - `weekday`:
        - `nth`:
        - `name`:
        """
        Holiday.__init__(self, name)
        self._period = period
        self._month = month
        self._weekday = weekday
        self._nth = nth

    # Operations
    def is_match_date(self, date):
        """function is_match_date

        date:

        returns
        """
        if not self._period.is_within(date):
            return False
        expect_day = get_weeknth(
            date.year, self._month, self._nth, self._weekday)
        return expect_day == date

    def get_month(self):
        """function get_month

        returns
        """
        return self._month

    def get_weekday(self):
        """function get_weekday

        returns
        """
        return self._weekday

    def get_week_nth(self):
        """function get_week_nth

        returns
        """
        return self._nth



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# yearly_week_nth.py ends here
