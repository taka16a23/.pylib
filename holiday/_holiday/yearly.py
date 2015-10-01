#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: yearly.py 460 2015-08-10 16:51:55Z t1 $
# $Revision: 460 $
# $Date: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $

r"""yearly -- DESCRIPTION

"""
from holiday._holiday.abstract import Holiday


class YearlyHoliday(Holiday):
    """Class YearlyHoliday
    """
    # Attributes:
    def __init__(self, period, month, day, name):
        r"""

        @Arguments:
        - `start`:
        - `end`:
        - `month`:
        - `day`:
        - `name`:
        """
        Holiday.__init__(self, name)
        self._period = period
        self._month = month
        self._day = day

    # Operations
    def is_match_date(self, date):
        """function is_match_date

        date:

        returns
        """
        if not self._period.is_within(date):
            return False
        return (self._month, self._day) == (date.month, date.day)

    def get_start(self, ):
        r"""SUMMARY

        get_start()

        @Return:

        @Error:
        """
        return self._period.get_start()

    def get_end(self, ):
        r"""SUMMARY

        get_end()

        @Return:

        @Error:
        """
        return self._period.get_end()

    def get_month(self):
        """function get_month

        returns
        """
        return self._month

    def get_day(self):
        """function get_day

        returns
        """
        return self._day



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# yearly.py ends here
