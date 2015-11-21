#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_day -- DESCRIPTION

"""
from dateutil.relativedelta import relativedelta

from holiday._day_interface import DayInterface
from holiday.japan._factory import JapaneseHolidayFactory
from holiday.period import Period


class JapaneseDay(DayInterface):
    r"""JapaneseDay

    JapaneseDay is a DayInterface.
    Responsibility:
    """
    _factory = JapaneseHolidayFactory()

    def between_holidays(self, date):
        r"""SUMMARY

        between_holidays(date)

        @Arguments:
        - `date`:

        @Return:

        @Error:
        """
        days = self._factory.between_holidays(Period(self, date)).keys()
        results = [self.__class__(d.year, d.month, d.day) for d in days]
        results.sort()
        return results

    def is_holiday(self, ):
        r"""SUMMARY

        is_holiday()

        @Return:

        @Error:
        """
        holidays = self._factory.between_holidays(
            Period(self - relativedelta(months=1), self + relativedelta(months=1)))
        return self in holidays

    def next_holiday(self, ):
        """function get_next

        date:

        returns tuple
        """
        dates = self.between_holidays(self + relativedelta(months=3))
        if not dates:
            # TODO: (Atami) [2015/08/10]
            # consider raise error if date not in min max range
            return None, u''
        dates.sort()
        index = 0
        if self == dates[index]:
            index += 1
        return self.__class__(
            dates[index].year, dates[index].month, dates[index].day)

    def previous_holiday(self, ):
        """function get_previous

        date:

        returns tuple
        """
        dates = self.between_holidays(self - relativedelta(months=3))
        if not dates:
            # TODO: (Atami) [2015/08/10]
            # consider raise error if date not in min max range
            return None
        dates.sort()
        index = -1
        if self == dates[index]:
            index -= 1
        return self.__class__(
            dates[index].year, dates[index].month, dates[index].day)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        holidays = self._factory.between_holidays(
            Period(self - relativedelta(months=1), self + relativedelta(months=1)))
        return holidays.get(self, '')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _day.py ends here
