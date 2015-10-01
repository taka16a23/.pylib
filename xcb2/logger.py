#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: logger.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""logger -- logging

"""

import sys as _sys
import os as _os

import logging
from logging.handlers import RotatingFileHandler
###############################################################################
# +-----------------------+
# | Level  |Numeric value |
# |--------+--------------|
# |CRITICAL|50            |
# |--------+--------------|
# |ERROR   |40            |
# |--------+--------------|
# |WARNING |30            |
# |--------+--------------|
# |INFO    |20            |
# |--------+--------------|
# |DEBUG   |10            |
# |--------+--------------|
# |NOTSET  |0             |
# +-----------------------+
# output log file
LOGNAME = 'xahk.log'
LOGDIR = '/var/log/'
LOGPATH = _os.path.join(LOGDIR, LOGNAME)
_RH = RotatingFileHandler(LOGPATH, 'w', 1024*50, 1)
_RH.setLevel(logging.ERROR)
_RH.setFormatter(logging.Formatter(
    '%(asctime)s;%(name)s;%(module)s %(funcName)s(%(lineno)d);%(levelname)s;'
    '\n   %(message)s'))

# console
_CH = logging.StreamHandler()
_CH.setLevel(logging.DEBUG)

LOG = logging.getLogger('xcb2')
LOG.addHandler(_CH)
LOG.addHandler(_RH)
LOG.setLevel(logging.DEBUG)

# exception
def logging_handle_exceptions(excls, value, trcbck):
    r"""Handling exception hook.

    sys.excepthook = logging_handle_exceptions
    """
    import traceback
    if issubclass(excls, KeyboardInterrupt):
        _sys.__excepthook__(excls, value, trcbck)
        return
    errortype = 'Error type: {}'.format(excls)
    valuetxt = 'Uncaught exception: {0}'.format(str(value))
    trcbcktxt = ''.join(traceback.format_tb(trcbck))
    LOG.exception('\n'.join([errortype, valuetxt, trcbcktxt]))

_sys.excepthook = logging_handle_exceptions
###############################################################################



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# logger.py ends here
