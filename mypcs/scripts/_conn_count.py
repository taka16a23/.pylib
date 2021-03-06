#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_conn_count -- DESCRIPTION

"""
from mypcs.scripts._script import Script


class ConnectionCount(Script):
    r"""ConnectinonCount

    ConnectinonCount is a Script.
    Responsibility:
    """
    def __init__(self, ips):
        r"""

        @Arguments:
        - `ips`:
        """
        self._ips = ips
        self._results = {}

    def execute_script(self, shell):
        r"""SUMMARY

        execute_script(shell)

        @Arguments:
        - `shell`:

        @Return:

        @Error:
        """
        for ip in self._ips:
            stream = shell.execute_command(
                'grep -c {} /proc/net/ip_conntrack'.format(ip))
            if stream.returncode != 0:
                continue
            self._results[ip] = int(stream.read_stdout().replace('\n', ''))

    def get_result(self, ):
        r"""SUMMARY

        get_result()

        @Return:

        @Error:
        """
        return self._results



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _conn_count.py ends here
