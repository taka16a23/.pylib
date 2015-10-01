#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
