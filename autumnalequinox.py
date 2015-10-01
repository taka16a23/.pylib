#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: autumnalequinox.py 283 2015-01-29 00:10:24Z t1 $
# $Revision: 283 $
# $Date: 2015-01-29 09:10:24 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:10:24 +0900 (Thu, 29 Jan 2015) $

r"""autumnalequinox -- DESCRIPTION

"""
from abc import ABCMeta as _ABCMeta, abstractmethod as _abstractmethod
from datetime import date


__all__ = ['CalcAutumnalEquinox']


class Longitude(object):
    r"""SUMMARY
    """
    __metaclass__ = _ABCMeta
    _month = 9

    @_abstractmethod
    def _getmonth(self, ):
        raise NotImplementedError()

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
        return date(year, self._getmonth(), day)


class Before1980_0Longitude(Longitude):
    r"""SUMMARY
    AutumnalEquinox
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
        day = int(23.2588 + 0.242194 * (year - 1980) - int((year - 1980) // 4))
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
        day = int(23.2488 + 0.242194 * (year - 1980) - int((year - 1980) // 4))
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
        day = int(24.2488 + 0.242194 * (year - 1980) - int((year - 1980) // 4))
        return self._getday(year, day)


class CalcAutumnalEquinox(object):
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
# autumnalequinox.py ends here
