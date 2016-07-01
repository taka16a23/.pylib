#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""account -- DESCRIPTION

"""
from getpass import getpass


class Account(object):
    """Account

    Account is a object.
    Responsibility:
    """
    def __init__(self, user, password=''):
        """

        @Arguments:
        - `user`:
        - `password`:
        """
        self.user = user
        self.password = password

    def get_user(self, ):
        r"""SUMMARY

        get_user()

        @Return:

        @Error:
        """
        return self.user

    def set_user(self, user):
        r"""SUMMARY

        set_user(user)

        @Arguments:
        - `user`:

        @Return:

        @Error:
        """
        self.user = user

    def get_password(self, ):
        """SUMMARY

        get_password()

        @Return:

        @Error:
        """
        return self.password

    def set_password(self, password):
        """SUMMARY

        set_password(password)

        @Arguments:
        - `password`:

        @Return:

        @Error:
        """
        self.password = password

    def input_password(self, ):
        """SUMMARY

        input_password()

        @Return:

        @Error:
        """
        self.password = getpass('Enter password: ')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# account.py ends here
