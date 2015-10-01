#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""log -- DESCRIPTION

"""
import sys
import logging
###############################################################################
# console
_CH = logging.StreamHandler()
_CH.setLevel(logging.WARN)

LOG = logging.getLogger('getpasswd')
LOG.setLevel(logging.WARN)
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
