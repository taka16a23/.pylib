#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""wrapcookie -- DESCRIPTION

"""
from xcb2.xproto import wreply


class WrapCookieAbstract(object):
    r"""SUMMARY
    """

    def __init__(self, connection, cookie):
        r"""

        @Arguments:
        - `connection`:
        - `cookie`:
        """
        self._connection = connection
        self._cookie = cookie


class WrapGetKeyboardMappingCookie(WrapCookieAbstract):
    r"""WrapGetKeyboardMappingCookie

    WrapGetKeyboardMappingCookie is a WrapCookieAbstract.
    Responsibility:
    """

    def check(self, ):
        r"""SUMMARY

        check()

        @Return:
        """
        return self._cookie.check()

    def reply(self, ):
        r"""SUMMARY

        reply()

        @Return:
        """
        return wreply.WrapGetKeyboardMappingReply(
            self._connection, self._cookie.reply())


class WrapGetPropertyCookie(WrapCookieAbstract):
    r"""SUMMARY
    """

    def check(self, ):
        r"""SUMMARY

        check()

        @Return:
        """
        return self._cookie.check()

    def reply(self, ):
        r"""SUMMARY

        reply()

        @Return:
        """
        rep = self._cookie.reply()
        rep.window = self._cookie.window
        rep.property = self._connection.core.atomidentify(
            self._cookie.property)
        return rep.property.gettype()(self._connection, rep)


class WrapGetAtomNameCookie(WrapCookieAbstract):
    r"""SUMMARY
    """

    def check(self, ):
        r"""SUMMARY

        check()

        @Return:
        """
        return self._cookie.check()

    def reply(self, ):
        r"""SUMMARY

        reply()

        @Return:
        """
        reply = self._cookie.reply()
        reply.atom = self._cookie.atom
        return wreply.WrapGetAtomNameReply(self._connection, reply)


class WrapGetInputFocusCookie(WrapCookieAbstract):
    r"""SUMMARY
    """

    def check(self, ):
        r"""SUMMARY

        check()

        @Return:
        """
        return self._cookie.check()

    def reply(self, ):
        r"""SUMMARY

        reply()

        @Return:
        """
        return wreply.WrapGetInputFocusReply(
            self._connection, self._cookie.reply())


class WrapInternAtomCookie(WrapCookieAbstract):
    r"""SUMMARY
    """

    def check(self, ):
        r"""SUMMARY

        check()

        @Return:
        """
        return self._cookie.check()

    def reply(self, ):
        r"""SUMMARY

        reply()

        @Return:
        """
        reply = self._cookie.reply()
        reply.name = self._cookie.name
        return wreply.WrapInternAtomReply(self._connection, reply)


class WrapQueryTreeCookie(WrapCookieAbstract):
    r"""SUMMARY
    """

    def check(self, ):
        r"""SUMMARY

        check()

        @Return:
        """
        return self._cookie.check()

    def reply(self, ):
        r"""SUMMARY

        reply()

        @Return:
        """
        return wreply.WrapQueryTreeReply(
            self._connection, self._cookie.reply())


class WrapGetGeometryCookie(WrapCookieAbstract):
    r"""SUMMARY
    """
    def check(self, ):
        r"""SUMMARY

        check()

        @Return:
        """
        return self._cookie.check()

    def reply(self, ):
        r"""SUMMARY

        reply()

        @Return:
        """
        return wreply.WrapGetGeometryReply(
            self._connection, self._cookie.reply())


class WrapListPropertyCookie(WrapCookieAbstract):
    r"""SUMMARY
    """

    def check(self, ):
        r"""SUMMARY

        check()

        @Return:
        """
        return self._cookie.check()

    def reply(self, ):
        r"""SUMMARY

        reply()

        @Return:
        """
        return wreply.WrapListPropertyReply(
            self._connection, self._cookie.reply())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# wrapcookie.py ends here
