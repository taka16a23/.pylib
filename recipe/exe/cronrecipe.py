#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: cronrecipe.py 448 2015-08-07 02:54:21Z t1 $
# $Revision: 448 $
# $Date: 2015-08-07 11:54:21 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 11:54:21 +0900 (Fri, 07 Aug 2015) $

r"""cronrecipe -- DESCRIPTION

"""
from time import sleep
import sys
import os
from datetime import datetime

import logging
from logging.handlers import RotatingFileHandler

from recipe.menu2 import MenuManager
from recipe.menu2.common import DEFAULT_DIR
from recipe._recipe import show_recipe_schedule

# for debug
import cgitb
cgitb.enable(format='text')


__revision__ = '$Revision: 448 $'
__version__ = '0.1.1'

# Change Log
# 0.1.1 Show Recipe Schedule by chrome from thunar


###############################################################################
# output log file
LOGNAME = 'recipe'
LOGDIR = '/var/log'
LOGPATH = os.path.join(LOGDIR, LOGNAME)
_RH = RotatingFileHandler(LOGPATH, 'w', 1024*50, 1)
_RH.setLevel(logging.DEBUG)
_RH.setFormatter(logging.Formatter(
    '%(asctime)s;%(name)s;%(module)s %(funcName)s(%(lineno)d);%(levelname)s;'
    '\n   %(message)s'))

# console
_CH = logging.StreamHandler()
_CH.setLevel(logging.DEBUG)

LOG = logging.getLogger('recipe')
LOG.setLevel(logging.DEBUG)
LOG.addHandler(_RH)
LOG.addHandler(_CH)

# exception
def logging_handle_exceptions(excls, value, trcbck):
    r"""Handling exception hook.

    sys.excepthook = logging_handle_exceptions
    """
    import traceback
    if issubclass(excls, KeyboardInterrupt):
        sys.__excepthook__(excls, value, trcbck)
        return
    errortype = 'Error type: {}'.format(excls)
    valuetxt = 'Uncaught exception: {0}'.format(str(value))
    trcbcktxt = ''.join(traceback.format_tb(trcbck))
    LOG.exception('\n'.join([errortype, valuetxt, trcbcktxt]))

sys.excepthook = logging_handle_exceptions
###############################################################################

MANAGER = MenuManager(DEFAULT_DIR)
TODAY_MENU = MANAGER.get_menu(datetime.now())

# show today's recipe
TODAY_MENU.show_recipes()

# open thunar
LOG.debug('in recipe latest path')
show_recipe_schedule()

sleep(20)

sys.exit(os.EX_OK)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cronrecipe.py ends here
