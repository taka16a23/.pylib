#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_day_interface -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from datetime import date
from holiday.international_name import InternationalName


class DayInterface(date):
    r"""DayInterface

    DayInterface is a date.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    def __new__(cls, year, month, day):
        return date.__new__(cls, year, month, day)

    def __add__(self, other):
        this = date(self.year, self.month, self.day)
        new = this + other
        if isinstance(new, (date, )):
            return self.__class__(new.year, new.month, new.day)
        return new

    def __radd__(self, other):
        this = date(self.year, self.month, self.day)
        new =  other + this
        if isinstance(new, (date, )):
            return self.__class__(new.year, new.month, new.day)
        return new

    def __sub__(self, other):
        this = date(self.year, self.month, self.day)
        new = this - other
        if isinstance(new, (date, )):
            return self.__class__(new.year, new.month, new.day)
        return new

    def __rsub__(self, other):
        this = date(self.year, self.month, self.day)
        new =  other - this
        if isinstance(new, (date, )):
            return self.__class__(new.year, new.month, new.day)
        return new

    def __repr__(self):
        return u'{0.__class__.__name__}({0.year}, {0.month}, {0.day}, "{1}")'.format(
            self, self.get_name())

    @abstractmethod
    def between_holidays(self, date):
        r"""SUMMARY

        between_holidays(date)

        @Arguments:
        - `date`:

        @Return:

        @Error:
        """

    @abstractmethod
    def is_holiday(self, ):
        r"""SUMMARY

        is_holiday()

        @Return:

        @Error:
        """

    @abstractmethod
    def next_holiday(self, ):
        r"""SUMMARY

        next_holiday()

        @Return:

        @Error:
        """

    @abstractmethod
    def previous_holiday(self, ):
        r"""SUMMARY

        previous_holiday()

        @Return:

        @Error:
        """

    @abstractmethod
    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._name



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _day_interface.py ends here
