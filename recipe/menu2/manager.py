#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: manager.py 454 2015-08-08 06:21:36Z t1 $
# $Revision: 454 $
# $Date: 2015-08-08 15:21:36 +0900 (Sat, 08 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-08 15:21:36 +0900 (Sat, 08 Aug 2015) $

r"""manager -- DESCRIPTION

"""
from datetime import datetime, timedelta, MINYEAR, MAXYEAR

from pathhandler import PathHandler

from recipe.menu2.menu import Menu


MINDATE = datetime(MINYEAR, 1, 1)
MAXDATE = datetime(MAXYEAR, 12, 31)


class MenuManager(object):
    """Class MenuOrganizer
    """
    # Attributes:
    def __init__(self, basedir):
        r"""

        @Arguments:
        - `directory`:
        """
        self._basedir = PathHandler(basedir)

    # Operations
    def get_menu(self, date):
        """function get_menu

        date:

        returns
        """
        dirname = date.strftime('%Y_%m_%d')
        return Menu(self._basedir.join(dirname))

    def iter_menus(self, start_date, end_date):
        """function list_menus

        start_date:
        end_date:

        returns
        """
        if end_date < start_date:
            start_date, end_date = end_date, start_date
        if 5000 < (end_date - start_date).days:
            # TODO: (Atami) [2015/04/06]
            raise StandardError()
        oneday = timedelta(1)
        date = start_date
        while date < end_date:
            yield self.get_menu(date)
            date = date + oneday

    def list_exists_menus(self):
        """function list_exists_menus

        returns
        """
        return [Menu(dirs) for dirs in self._basedir.listdir()]

    def remove_between_date(self, start, end):
        """function remove_between_date

        start:
        end:

        returns
        """
        for menu in self.list_exists_menus():
            if start <= menu.get_date() <= end:
                menu.remove()

    def remove_empty_menus(self):
        """function remove_empty_menus

        returns
        """
        for menu in self.list_exists_menus():
            if not menu.has_recipes():
                menu.remove()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# manager.py ends here
