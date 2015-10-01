#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: rotate_recipe.py

"""
from t1.dateutil import now_weekday
from datetime import datetime
from recipe.menu2 import MenuManager
from recipe.menu2.common import DEFAULT_DIR


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
