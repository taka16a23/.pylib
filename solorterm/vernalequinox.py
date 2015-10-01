#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: vernalequinox.py 289 2015-01-29 00:17:20Z t1 $
# $Revision: 289 $
# $Date: 2015-01-29 09:17:20 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:17:20 +0900 (Thu, 29 Jan 2015) $

r"""vernalequinox -- DESCRIPTION

"""
from solorterm.abstract import Longitude


__all__ = ['CalcVernalEquinox']


class VernalLongitude(Longitude):
    r"""SUMMARY
    """

    def _getmonth(self, ):
        r"""SUMMARY

        _getmonth()

        @Return:
        """
        return 3


class Before1980_0VernalLongitude(VernalLongitude):
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


class From1980To2100_0VernalLongitude(VernalLongitude):
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


class From2100To2150_0VernalLongitude(VernalLongitude):
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
    _spans = [Before1980_0VernalLongitude(),
              From1980To2100_0VernalLongitude(),
              From2100To2150_0VernalLongitude()]

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
# vernalequinox.py ends here
