#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""abstract -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class Holiday(object):
    """Class Holiday
    """
    __metaclass__ = ABCMeta

    # Attributes:
    def __init__(self, name):
        r"""

        @Arguments:
        - `start`:
        - `end`:
        - `name`:
        """
        self._name = name

    # Operations
    @abstractmethod
    def is_match_date(self, date):
        """function is_match_date

        date:

        returns
        """

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
# abstract.py ends here
