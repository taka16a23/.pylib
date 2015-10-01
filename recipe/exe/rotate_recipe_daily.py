#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: rotate_recipe_daily.py 448 2015-08-07 02:54:21Z t1 $
# $Revision: 448 $
# $Date: 2015-08-07 11:54:21 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 11:54:21 +0900 (Fri, 07 Aug 2015) $

r"""Name: rotate_recipe.py

"""
from t1.dateutil import now_weekday
from datetime import datetime
from recipe.menu2 import MenuManager
from recipe.menu2.common import DEFAULT_DIR


__revision__ = '$Revision: 448 $'
__version__ = '0.0.1'

TODAY = datetime.now()


def empty_remove(menu):
    r"""SUMMARY

    empty_remove(menu)

    @Arguments:
    - `menu`:

    @Return:

    @Error:
    """
    if not menu.has_recipes():
        menu.remove()


def remove_old(menu):
    r"""SUMMARY

    remove_old(menu)

    @Arguments:
    - `menu`:

    @Return:

    @Error:
    """
    if menu.get_date() <= TODAY:
        menu.remove()


if now_weekday().is_wednesday():
    for menu in MenuManager(DEFAULT_DIR).list_exists_menus():
        remove_old(menu)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rotate_recipe.py ends here
