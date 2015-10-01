#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _connections.py 464 2015-08-17 07:02:48Z t1 $
# $Revision: 464 $
# $Date: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $

r"""_connections -- DESCRIPTION

"""
from mypcs.scripts._script import Script
from mypcs.scripts._arptable import ArpTable
from mypcs.scripts._conn_count import ConnectionCount

from collections import namedtuple


ConnectionResult = namedtuple('ConnectionResult', ('ip', 'macaddr', 'count'))


class LocalConnections(Script):
    r"""LocalConnections

    LocalConnections is a Script.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._results = []

    def get_result(self, ):
        r"""SUMMARY

        get_result()

        @Return:

        @Error:
        """
        return self._results

    def execute_script(self, shell):
        r"""SUMMARY

        execute_script(shell)

        @Arguments:
        - `shell`:

        @Return:

        @Error:
        """
        arp = ArpTable()
        arp.execute_script(shell)
        ips = [x[0] for x in arp.get_result()]
        conncount = ConnectionCount(ips)
        conncount.execute_script(shell)
        countdic = conncount.get_result()
        for ip, _, _, mac, _, _ in arp.get_result():
            self._results.append(ConnectionResult(
                ip=ip, macaddr=mac, count=countdic.get(ip, 0)))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _connections.py ends here
