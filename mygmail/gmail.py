#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" gmail -- my gmail info

$Revision: 405 $

"""

import sys as _sys
import smtplib
from getpass import getpass


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class GmailAddressConst(object):
    r"""GmailAddressConst

    GmailAddressConst is a object.
    Responsibility:
    """
    TAKA16 = 'taka16a23@gmail.com'
    TAKAHIRO = 'takahiroatsumi0517@gmail.com'
    DAILY = 'taka16daily@gmail.com'


class MyGmail(object):
    r"""
    """

    def __init__(self, from_=None, to=None, passwd=None):
        r"""

        @Arguments:
        - `passwd`:
        """
        self.FROM = from_
        self.TO = to
        self._passwd = passwd
        self._server = smtplib.SMTP('smtp.gmail.com', 587)
        self._server.ehlo()
        self._server.starttls()

    def login(self, user, passwd=None, delpass=True):
        r"""SUMMARY

        login(passwd=None)

        @Arguments:
        - `passwd`:

        @Return:
        """
        if passwd:
            self._passwd = passwd
        if not self._passwd:
            self._passwd = getpass('Input password: ')
        self._server.login(user, self._passwd)
        if delpass:
            self.delpassword()

    def delpassword(self, ):
        r"""SUMMARY

        delpassword()

        @Return:
        """
        self._passwd = None

    def setfrom(self, from_):
        r"""SUMMARY

        setfrom(from_)

        @Arguments:
        - `from_`:

        @Return:
        """
        self.FROM = from_

    def setto(self, to):
        r"""SUMMARY

        setto(to)

        @Arguments:
        - `to`:

        @Return:
        """
        self.TO = to

    def send(self, msg, from_=None, to=None):
        r"""SUMMARY

        send()

        @Return:
        """
        if from_:
            self.setfrom(from_)
        if to:
            self.setto(to)
        self._server.sendmail(self.FROM, self.TO, msg)



def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# gmail.py ends here
