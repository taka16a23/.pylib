#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""account -- DESCRIPTION

"""


class Account(object):
    r"""Account

    Account is a object.
    Responsibility:
    """
    def __init__(self, user, password):
        r"""

        @Arguments:
        - `user`:
        - `password`:
        """
        self._user = user
        self._password = password

    def get_user(self, ):
        r"""SUMMARY

        get_user()

        @Return:

        @Error:
        """
        return self._user

    def set_user(self, user):
        r"""SUMMARY

        set_user()

        @Return:

        @Error:
        """
        self._user = user

    def get_password(self, ):
        r"""SUMMARY

        get_password()

        @Return:

        @Error:
        """
        return self._password

    def set_password(self, passwd):
        r"""SUMMARY

        set_password()

        @Return:

        @Error:
        """
        self._password = passwd



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# account.py ends here
