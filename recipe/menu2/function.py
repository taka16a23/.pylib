#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""function -- DESCRIPTION

"""
from datetime import datetime


from recipe.menu2.manager import MenuManager
from recipe.menu2.common import DEFAULT_DIR


def get_today():
    r"""SUMMARY

    get_today()

    @Return:

    @Error:
    """
    man = MenuManager(DEFAULT_DIR)
    return man.get_menu(datetime.now())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# function.py ends here
