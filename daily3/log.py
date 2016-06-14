#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""log -- DESCRIPTION

"""
import os
import sys
import logging
from path import Path
from logging.handlers import RotatingFileHandler


__version__ = '0.0.1'


###############################################################################
LOG = logging.getLogger('daily3')
LOG.setLevel(logging.INFO)

# output log file
LOGPATH = Path('/var/log/daily3.log')
_RH = RotatingFileHandler(unicode(LOGPATH), 'a', 1024*50, 1)
_RH.setLevel(logging.INFO)
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


def _test():
    r"""Test function."""
    LOG.debug('debug')
    LOG.info('info')
    LOG.warning('warning')
    LOG.error('error')
    LOG.fatal('fatal')

    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# log.py ends here
