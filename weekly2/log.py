#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: log.py 351 2015-08-05 21:00:40Z t1 $
# $Revision: 351 $
# $Date: 2015-08-06 06:00:40 +0900 (Thu, 06 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-06 06:00:40 +0900 (Thu, 06 Aug 2015) $

r"""log -- DESCRIPTION

"""
import sys
import logging
from path import Path
from logging.handlers import RotatingFileHandler
###############################################################################
LOG = logging.getLogger('weekly2')
LOG.setLevel(logging.ERROR)

# output log file
LOGPATH = Path('/var/log/weekly2.log')
_RH = RotatingFileHandler(unicode(LOGPATH), 'a', 1024*50, 1)
_RH.setLevel(logging.ERROR)
_RH.setFormatter(logging.Formatter(
    '%(asctime)s;%(name)s;%(module)s %(funcName)s(%(lineno)d);%(levelname)s;'
    '\n   %(message)s'))
LOG.addHandler(_RH)

# console
if sys.stdout.isatty():
    _CH = logging.StreamHandler()
    _CH.setLevel(logging.INFO)
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








# For Emacs
# Local Variables:
# coding: utf-8
# End:
# log.py ends here
