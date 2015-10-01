#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _lanip.py 464 2015-08-17 07:02:48Z t1 $
# $Revision: 464 $
# $Date: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $

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
