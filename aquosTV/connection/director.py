#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""director -- DESCRIPTION

"""


class ConnectionDirector(object):
    """ConnectionDirector

    ConnectionDirector is a object.
    Responsibility:
    """
    def __init__(self, builder):
        """

        @Arguments:
        - `builder`:
        """
        self._builder = builder

    def get_connection(self, ):
        """SUMMARY

        get_connection()

        @Return:

        @Error:
        """
        self._builder.connect()
        self._builder.authenticate()
        return self._builder.get_connection()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# director.py ends here
