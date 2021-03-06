#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""log -- DESCRIPTION

"""
import sys
import logging
from path import Path
from logging.handlers import RotatingFileHandler
###############################################################################
LOG = logging.getLogger('xahk')
LOG.setLevel(logging.DEBUG)

# output log file
LOGPATH = Path('/var/log/xahk')
_RH = RotatingFileHandler(unicode(LOGPATH), 'w', 1024*50, 3)
_RH.setLevel(logging.WARNING)
_RH.setFormatter(logging.Formatter(
    '%(asctime)s;%(name)s;%(module)s %(funcName)s(%(lineno)d);%(levelname)s;'
    '\n   %(message)s'))
LOG.addHandler(_RH)

# console
if sys.stdout.isatty():
    _CH = logging.StreamHandler()
    _CH.setLevel(logging.DEBUG)
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
