#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""vernalequinox -- DESCRIPTION

"""
from abc import ABCMeta as _ABCMeta, abstractmethod as _abstractmethod
from datetime import date


__all__ = ['CalcVernalEquinox']


class Longitude(object):
    r"""SUMMARY
    """
    __metaclass__ = _ABCMeta
    _month = 3

    @_abstractmethod
    def ismatch(self, year):
        raise NotImplementedError()

    @_abstractmethod
    def calc(self, year):
        raise NotImplementedError()

    def _getday(self, year, day):
        r"""SUMMARY

        _getday(day)

        @Arguments:
        - `day`:

        @Return:
        """
        return date(year, self._month, day)


class Before1980_0Longitude(Longitude):
    r"""SUMMARY
    VernalEquinox
    """

    def ismatch(self, year):
        r"""SUMMARY

        ismatch(year)

        @Arguments:
        - `year`:

        @Return:
        """
        return year <= 1979

    def calc(self, year):
        r"""SUMMARY

        calc(year)

        @Arguments:
        - `year`:

        @Return:
        """
        #                   一年のずれ                 閏年のずれ
        day = int(20.8357 + 0.242194 * (year - 1980) - int((year - 1980) // 4))
        return self._getday(year, day)


class From1980To2100_0Longitude(Longitude):
    r"""SUMMARY
    """

    def ismatch(self, year):
        r"""SUMMARY

        ismatch(year)

        @Arguments:
        - `year`:

        @Return:
        """
        return 1980 <= year <= 2099

    def calc(self, year):
        r"""SUMMARY

        calc(year)

        @Arguments:
        - `year`:

        @Return:
        """
        #                   一年のずれ                 閏年のずれ
        day = int(20.8431 + 0.242194 * (year - 1980) - int((year - 1980) // 4))
        return self._getday(year, day)


class From2100To2150_0Longitude(Longitude):
    r"""SUMMARY
    """

    def ismatch(self, year):
        r"""SUMMARY

        ismatch(year)

        @Arguments:
        - `year`:

        @Return:
        """
        return 2100 <= year <= 2150

    def calc(self, year):
        r"""SUMMARY

        calc(year)

        @Arguments:
        - `year`:

        @Return:
        """
        #                   一年のずれ                 閏年のずれ
        day = int(21.8510 + 0.242194 * (year - 1980) - int((year - 1980) // 4))
        return self._getday(year, day)


class CalcVernalEquinox(object):
    r"""SUMMARY
    """
    _spans = [Before1980_0Longitude(),
              From1980To2100_0Longitude(),
              From2100To2150_0Longitude()]

    def calc(self, year):
        r"""SUMMARY

        get_vernal_day(year)

        @Arguments:
        - `year`:

        @Return:
        """
        for span in self._spans:
            if span.ismatch(year):
                return span.calc(year)
        # TODO: (Atami) [2014/06/30]
        raise StandardError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# vernalequinox.py ends here
