#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: err.py 277 2015-01-28 23:57:11Z t1 $
# $Revision: 277 $
# $Date: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $

r"""err -- DESCRIPTION

"""

class XSKError(Exception):
    r"""XSKError

    XSKError is a Exception.
    Responsibility:
    """


class XSKSyntaxError(XSKError):
    r"""XSKSyntaxError

    XSKSyntaxError is a XSKError.
    Responsibility:
    """


class XSKScanError(XSKError):
    r"""XSKScanError

    XSKScanError is a XSKError.
    Responsibility:
    """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# err.py ends here
