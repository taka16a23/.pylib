#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
