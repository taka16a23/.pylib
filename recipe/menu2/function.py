#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: function.py 455 2015-08-08 06:39:21Z t1 $
# $Revision: 455 $
# $Date: 2015-08-08 15:39:21 +0900 (Sat, 08 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-08 15:39:21 +0900 (Sat, 08 Aug 2015) $

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
