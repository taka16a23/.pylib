#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""database -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class DiaryDatabase(object):
    """Abstract class DiaryDatabase
    """
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def list_notes(self):
        """function list_notes

        returns
        """
        raise NotImplementedError()

    @abstractmethod
    def list_by_date(self, date):
        """function list_by_date

        date:

        returns
        """
        raise NotImplementedError()

    @abstractmethod
    def list_by_month(self, month):
        """function list_by_month

        month:

        returns
        """
        raise NotImplementedError()

    @abstractmethod
    def list_by_day(self, day):
        """function list_by_day

        day:

        returns
        """
        raise NotImplementedError()

    @abstractmethod
    def list_by_date_range(self, start, end):
        """function list_by_date_range

        start:
        end:

        returns
        """
        raise NotImplementedError()

    @abstractmethod
    def list_by_search_text(self, regexp):
        """function list_by_search_text

        regexp: re.compile

        returns
        """
        raise NotImplementedError()

    @abstractmethod
    def close(self):
        """function close

        returns
        """
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# database.py ends here
