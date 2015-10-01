#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: abstract.py 289 2015-01-29 00:17:20Z t1 $
# $Revision: 289 $
# $Date: 2015-01-29 09:17:20 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:17:20 +0900 (Thu, 29 Jan 2015) $

r"""abstract -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from datetime import date


class Longitude(object):
    r"""SUMMARY
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def _getmonth(self, ):
        raise NotImplementedError()

    @abstractmethod
    def ismatch(self, year):
        raise NotImplementedError()

    @abstractmethod
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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# abstract.py ends here
