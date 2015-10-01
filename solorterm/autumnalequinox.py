#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: autumnalequinox.py 289 2015-01-29 00:17:20Z t1 $
# $Revision: 289 $
# $Date: 2015-01-29 09:17:20 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:17:20 +0900 (Thu, 29 Jan 2015) $

r"""autumnalequinox -- DESCRIPTION

"""
from solorterm.abstract import Longitude


__all__ = ['CalcAutumnalEquinox']


class AutumnalLogitude(Longitude):
    r"""SUMMARY
    """

    def _getmonth(self, ):
        r"""SUMMARY

        _get_month()

        @Return:
        """
        return 9


class Before1980_0AutumnalLogitude(AutumnalLogitude):
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


class From1980To2100_0AutumnalLogitude(AutumnalLogitude):
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


class From2100To2150_0AutumnalLogitude(AutumnalLogitude):
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
    _spans = [Before1980_0AutumnalLogitude(),
              From1980To2100_0AutumnalLogitude(),
              From2100To2150_0AutumnalLogitude()]

    def _getspan(self, year):
        r"""SUMMARY

        _getspan(year)

        @Arguments:
        - `year`:

        @Return:
        """
        for span in self._spans:
            if span.ismatch(year):
                return span
        return None

    def ismatch(self, year):
        r"""SUMMARY

        ismatch(year)

        @Arguments:
        - `year`:

        @Return:
        """
        span = self._getspan(year)
        if span is None:
            return False
        return True

    def calc(self, year):
        r"""SUMMARY

        get_vernal_day(year)

        @Arguments:
        - `year`:

        @Return:
        """
        span = self._getspan(year)
        if not span is None:
            return span.calc(year)
        raise StandardError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# autumnalequinox.py ends here
