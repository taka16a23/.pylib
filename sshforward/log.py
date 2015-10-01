#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: log.py 259 2014-12-21 05:20:44Z t1 $
# $Revision: 259 $
# $Date: 2014-12-21 14:20:44 +0900 (Sun, 21 Dec 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-12-21 14:20:44 +0900 (Sun, 21 Dec 2014) $

r"""log -- DESCRIPTION

"""
import sys
import logging


###############################################################################
# console
_CH = logging.StreamHandler()
_CH.setLevel(logging.INFO)

LOG = logging.getLogger('sshforward')
LOG.setLevel(logging.INFO)
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
