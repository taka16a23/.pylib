#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: display.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

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
