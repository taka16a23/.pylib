#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from t1.dateutil.nthweekday import NthWeekDay

from calendar import (MONDAY, TUESDAY, WEDNESDAY, THURSDAY,
                      FRIDAY, SATURDAY, SUNDAY)
from datetime import *

from enum import IntEnum


__version__ = "0.1.0"

__all__ = [ '' ]


WEEKDAY_JDIC = {MONDAY: u'月',
               TUESDAY: u'火',
               WEDNESDAY: u'水',
               THURSDAY: u'木',
               FRIDAY: u'金',
               SATURDAY: u'土',
               SUNDAY: u'日'}


MON = MONDAY
TUE = TUESDAY
WED = WEDNESDAY
THU = THURSDAY
FRI = FRIDAY
SAT = SATURDAY
SUN = SUNDAY


class Weekdays(IntEnum):
    r"""Enum of Weekdays."""

    Monday    = MONDAY
    Tuesday   = TUESDAY
    Wednesday = WEDNESDAY
    Thursday  = THURSDAY
    Friday    = FRIDAY
    Saturday  = SATURDAY
    Sunday    = SUNDAY


class ISOWeekdays(IntEnum):
    r"""Enum of Weekdays."""

    Monday    = 1
    Tuesday   = 2
    Wednesday = 3
    Thursday  = 4
    Friday    = 5
    Saturday  = 6
    Sunday    = 7


class Weekday(object):
    r"""SUMMARY
    """
    _enums = Weekdays

    def __init__(self, weekday):
        r"""

        @Arguments:
        - `weekday`:
        - `*args`:
        - `**kwargs`:
        """
        self.weekday = weekday

    def is_monday(self, ):
        r"""SUMMARY

        is_monday()

        @Return:
        """
        return self.weekday == self._enums.Monday

    def is_tuesday(self, ):
        r"""SUMMARY

        is_tuesday()

        @Return:
        """
        return self.weekday == self._enums.Tuesday

    def is_wednesday(self, ):
        r"""SUMMARY

        is_wednesday()

        @Return:
        """
        return self.weekday == self._enums.Wednesday

    def is_thursday(self, ):
        r"""SUMMARY

        is_thursday()

        @Return:
        """
        return self.weekday == self._enums.Thursday

    def is_friday(self, ):
        r"""SUMMARY

        is_friday()

        @Return:
        """
        return self.weekday == self._enums.Friday

    def is_saturday(self, ):
        r"""SUMMARY

        is_stua()

        @Return:
        """
        return self.weekday == self._enums.Saturday

    def is_sunday(self, ):
        r"""SUMMARY

        is_sunday()

        @Return:
        """
        return self.weekday == self._enums.Sunday

    def __int__(self, ):
        return self.weekday

    def __str__(self, ):
        return self._enums(self.weekday).name

    def __repr__(self, ):
        return '{}: {}'.format(str(self), self.weekday)


class ISOWeekday(Weekday):
    r"""SUMMARY
    """

    _enums = ISOWeekdays



class WeekDay(IntEnum):
    r"""WeekDay

    WeekDay is a enum.Enum.
    Responsibility:
    """
    Monday = MONDAY
    Tuesday = TUESDAY
    Wednesday = WEDNESDAY
    Thursday = THURSDAY
    Friday = FRIDAY
    Saturday = SATURDAY
    Sunday = SUNDAY

    def weekday(self, ):
        r"""SUMMARY

        weekday()

        @Return:

        @Error:
        """
        return self.value

    def iso_weekday(self, ):
        r"""SUMMARY

        iso_weekday()

        @Return:

        @Error:
        """
        return self.value + 1

    def to_japanese(self, ):
        r"""SUMMARY

        to_japanese()

        @Return:

        @Error:
        """
        return u'月火水木金土日'[self.value]

    @property
    def shortname(self):
        return self.name[:3]

    @classmethod
    def from_date(cls, d):
        return cls(d.weekday())

    def __str__(self):
        return self.name


def now_weekday():
    r"""SUMMARY

    now_weekday()

    @Return:
    """
    return Weekday(datetime.now().weekday())


def tomorrow():
    r"""SUMMARY

    tomorrow()

    @Return:

    @Error:
    """
    return datetime.now() + timedelta(1)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
