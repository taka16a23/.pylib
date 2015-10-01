#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""logger -- DESCRIPTION

"""
import sys
import logging
from logging.handlers import RotatingFileHandler

from path import Path

LOG = logging.getLogger('xahk')
LOG.setLevel(logging.INFO)

# output log file
LOGPATH = Path('/var/log/xahk.log')
_RH = RotatingFileHandler(unicode(LOGPATH), 'w', 1024*50, 1)
_RH.setLevel(logging.DEBUG)
_RH.setFormatter(logging.Formatter(
    '%(asctime)s;%(name)s;%(module)s %(funcName)s(%(lineno)d);%(levelname)s;'
    '\n   %(message)s'))
LOG.addHandler(_RH)

# console
if sys.stdout.isatty():
    _CH = logging.StreamHandler()
    _CH.setLevel(logging.DEBUG)
    LOG.addHandler(_CH)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# logger.py ends here
