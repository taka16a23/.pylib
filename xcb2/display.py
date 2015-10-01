#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""connection -- DESCRIPTION

"""


class Display(object):
    r"""
    """

    def __init__(self, display=None):
        r"""

        @Arguments:
        - `display`:
        """
        self.display = display or ''

    @property
    def connection(self, ):
        r"""SUMMARY

        connection()

        @Return:
        """
        # KLUDGE: (Atami) [2014/05/15]
        from xcb2.xproto.xconnection import Connection
        return Connection.get_instance(display=self.display)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# connection.py ends here
