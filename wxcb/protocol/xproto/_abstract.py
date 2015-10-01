#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _abstract.py 280 2015-01-29 00:05:31Z t1 $
# $Revision: 280 $
# $Date: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $

r"""_abstract -- DESCRIPTION

"""


class WrapReplyAbstract(object):
    r"""WrapReplyAbstract

    WrapReplyAbstract is a object.
    Responsibility:
    """
    def __init__(self, rawreply):
        r"""

        @Arguments:
        - `rawreply`:
        """
        self._rawreply = rawreply


class WrapCookieAbstract(object):
    r"""WrapCookieAbstract

    WrapCookieAbstract is a object.
    Responsibility:
    """
    def __init__(self, rawcookie):
        r"""

        @Arguments:
        - `rawcookie`:
        """
        self._rawcookie = rawcookie

    def check(self, ):
        r"""SUMMARY

        check()

        @Return:

        @Error:
        """
        return self._rawcookie.check()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _abstract.py ends here
