#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: abstract.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

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
