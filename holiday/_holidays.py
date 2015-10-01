#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _holidays.py 460 2015-08-10 16:51:55Z t1 $
# $Revision: 460 $
# $Date: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $

r"""_holidays -- DESCRIPTION

"""
import datetime
from dateutil.relativedelta import relativedelta

from holiday._factory import HolidayFactory
from holiday.period import Period


class Holidays(object):
    """Class Holidays
    """
    # Attributes:
    def __init__(self, lang=None):
        r"""
        """
        self.default_lang = lang or 'en'
        self._factory = HolidayFactory()

    # Operations
    def between_holidays(self, period):
        """function between_holidays

        start: date
        end: date

        returns dict
        """
        return self._factory.between_holidays(period)

    def is_holiday(self, date):
        """function is_holiday

        date:

        returns bool
        """
        start = datetime.date(date.year, date.month, 1)
        end = start + relativedelta(months=1) - relativedelta(days=1)
        return date in self.between_holidays(Period(start, end))

    def a_year_holidays(self, year):
        r"""SUMMARY

        a_year_holidays(year)

        @Arguments:
        - `year`:

        @Return:

        @Error:
        """
        start = datetime.date(year, 1, 1)
        end = datetime.date(year + 1, 1, 1) - datetime.timedelta(1)
        return self.between_holidays(Period(start, end))

    def get_next(self, date):
        """function get_next

        date:

        returns tuple
        """
        start = date
        end = start + relativedelta(years=1)
        holidays = self.between_holidays(Period(start, end))
        dates = holidays.keys()
        if not dates:
            # TODO: (Atami) [2015/08/10]
            # consider raise error if date not in min max range
            return None, u''
        dates.sort()
        index = 0
        if date == dates[index]:
            index += 1
        return dates[index], holidays[dates[index]]

    def get_previous(self, date):
        """function get_previous

        date:

        returns tuple
        """
        start = date - relativedelta(years=1)
        end = date
        holidays = self.between_holidays(Period(start, end))
        dates = holidays.keys()
        if not dates:
            # TODO: (Atami) [2015/08/10]
            # consider raise error if date not in min max range
            return None, u''
        dates.sort()
        index = -1
        if date == dates[index]:
            index -= 1
        return dates[index], holidays[dates[index]]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _holidays.py ends here
