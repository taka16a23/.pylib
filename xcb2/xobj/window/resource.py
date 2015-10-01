#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: resource.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""resource -- DESCRIPTION

"""
from xcb2.abstract import ConnectionAbstract


class Resource(ConnectionAbstract):
    r"""SUMMARY
    """

    def __init__(self, connection, rid):
        r"""

        @Arguments:
        - `connection`:
        - `rid`:

        """
        ConnectionAbstract.__init__(self, connection)
        self.id = int(rid)

    @property
    def core(self, ):
        r"""Alias Connection.core

        core()

        @Return:
        """
        return self.connection.core

    def __int__(self, ):
        return self.id

    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            if self.connection == other.connection:
                return cmp(self.id, other.id)
            else:
                return cmp(self.connection, other.connection)
        else:
            return cmp(id(self), id(other))

    def __hash__(self, ):
        return int(self.id)

    def __repr__(self, ):
        return '<{0.__class__.__name__} {0.id}>'.format(self, id(self))

    def __str__(self, ):
        return '{0.__class__.__name__}(id={0.id})'.format(self)

    def kill_client(self, ):
        r"""SUMMARY

        kill_client()

        @Return:
        """
        return self.connection.core.KillClient(self.id)

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:
        """
        self.connection.flush()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# resource.py ends here
