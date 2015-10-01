#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""database_client -- DESCRIPTION

"""
import re
from datetime import datetime
from calendar import Calendar

from diary.gmail_database import GmailDiaryDatabase as DiaryDatabase


class DiaryDatabaseClient(object):
    """Class DiaryDatabaseClient
    """
    # Attributes:
    def __init__(self, ):
        r"""
        """
        self.database = DiaryDatabase()

    # Operations
    def list_notes(self):
        """function iter_notes

        returns
        """
        return self.database.list_notes()

    def list_by_date(self, year=None, month=None, day=None):
        """function list_by_date

        year:
        month:
        day:

        returns
        """
        if year and month is None and day is None:
            return self.list_by_date_range(
                datetime(year, 1, 1), datetime(year, 12, 31))
        elif month and year is None and day is None:
            return self.database.list_by_month(month)
        elif day and year is None and month is None:
            return self.database.list_by_day(day)
        elif year is None and None not in (month, day):
            months = self.database.list_by_month(month)
            return [n for n in months if n.date.day == day]
        elif month is None and None not in (year, day):
            years = self.list_by_date_range(
                datetime(year, 1, 1), datetime(year, 12, 31))
            return [n for n in years if n.date.day == day]
        elif day is None and None not in (year, month):
            cal = Calendar()
            days = list(cal.itermonthdays(year, month))
            while 0 in days:
                days.remove(0)
            return self.list_by_date_range(
                datetime(year, month, 1), datetime(year, month, days[-1]))
        elif None not in (year, month, day):
            return self.database.list_by_date(datetime(year, month, day))
        else:
            # TODO: (Atami) [2015/08/02]
            raise ValueError('all None')

    def list_by_date_range(self, start, end):
        """function list_by_date_range

        start:
        end:

        returns
        """
        return self.database.list_by_date_range(start, end)

    def list_by_search_text(self, regexp=''):
        """function list_by_search_text

        regexp: str

        returns
        """
        return self.database.list_by_search_text(re.compile(regexp))

    def close(self):
        """function close

        returns
        """
        self.database.close()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# database_client.py ends here
