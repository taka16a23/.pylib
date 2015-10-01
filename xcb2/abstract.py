#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""abstract -- DESCRIPTION

"""


class ConnectionAbstract(object):
    r"""SUMMARY
    """

    def __init__(self, connection):
        r"""

        @Arguments:
        - `connection`:
        """
        self.connection = connection

    @property
    def rawconnection(self, ):
        r"""SUMMARY

        base_connection()

        @Return:
        """
        return self.connection.rawconnection



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# abstract.py ends here
