#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_lanip -- DESCRIPTION

"""
from mypcs.scripts._script import Script


class LanIPScript(Script):
    r"""LanIPScript

    LanIPScript is a Script.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._result = ''

    def execute_script(self, shell):
        r"""SUMMARY

        execute_script(shell)

        @Arguments:
        - `shell`:

        @Return:

        @Error:
        """
        stdstream = shell.execute_command(
            '/usr/sbin/nvram show | grep lan_ipaddr')
        if stdstream.returncode != 0:
            return
        strings = stdstream.readlines_stdout()
        if not strings:
            return
        results = strings[0].split('=')
        if len(results) < 2:
            return
        self._result = results[1].replace('\n', '')

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
# _lanip.py ends here
