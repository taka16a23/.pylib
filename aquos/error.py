#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" error -- Error for aquos


"""


class LoginError(StandardError):
    r"""
    """

    def __init__(self, user, passwd):
        r"""

        Arguments:
        - `user`:
        - `passwd`:
        """
        self._user = user
        self._passwd = passwd



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# error.py ends here
