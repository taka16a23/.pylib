#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_wol -- DESCRIPTION

"""
from mypcs.scripts._script import Script


class WOLScript(Script):
    r"""WOLScript

    WOLScript is a Script.
    Responsibility:
    """
    def __init__(self, macaddress):
        r"""

        @Arguments:
        - `macaddress`:
        """
        self._macaddress = macaddress
        self._successed = None

    def execute_script(self, shell):
        r"""SUMMARY

        execute_script(shell)

        @Arguments:
        - `shell`:

        @Return:

        @Error:
        """
        stdstream = shell.execute_command(
            '/usr/sbin/wol -i 192.168.1.255 {0}'.format(self._macaddress))
        if stdstream.returncode == 0:
            self._successed = True
            return
        self._successed = False

    def get_macaddress(self, ):
        r"""SUMMARY

        get_macaddress()

        @Return:

        @Error:
        """
        return self._macaddress

    def set_macaddress(self, macaddr):
        r"""SUMMARY

        set_macaddress(macaddr)

        @Arguments:
        - `macaddr`:

        @Return:

        @Error:
        """
        self._macaddress = macaddr

    def is_successed(self, ):
        r"""SUMMARY

        is_successed()

        @Return:

        @Error:
        """
        return self._successed



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _wol.py ends here
