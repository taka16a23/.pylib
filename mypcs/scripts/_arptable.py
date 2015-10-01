#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_arptable -- DESCRIPTION

"""
from mypcs.scripts._script import Script


class ArpTable(Script):
    r"""ArpTable

    ArpTable is a Script.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._result = []

    def execute_script(self, shell):
        r"""SUMMARY

        execute_script(shell)

        @Arguments:
        - `shell`:

        @Return:

        @Error:
        """
        stdstream = shell.execute_command('grep 0x /proc/net/arp')
        if stdstream.returncode != 0:
            return
        lines = stdstream.readlines_stdout()
        for line in lines:
            self._result.append(line.split(' '))
        for results in self._result:
            while '' in results:
                results.remove('')

    def get_result(self, ):
        r"""SUMMARY

        get_result()

        @Return:

        @Error:
        """
        return self._result



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _arptable.py ends here
