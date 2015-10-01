#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _halt.py 483 2015-09-19 22:10:00Z t1 $
# $Revision: 483 $
# $Date: 2015-09-20 07:10:00 +0900 (Sun, 20 Sep 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-09-20 07:10:00 +0900 (Sun, 20 Sep 2015) $

r"""_halt -- DESCRIPTION

"""
from mypcs.scripts._script import Script


class HaltScript(Script):
    r"""RebootScript

    HaltScript is a Script.
    Responsibility:
    """
    def __init__(self, sudo=False):
        r"""

        @Arguments:
        - `sudo`:
        """
        self._sudo = sudo
        self._success = None

    def execute_script(self, shell):
        r"""SUMMARY

        execute_script(shell)

        @Arguments:
        - `shell`:

        @Return:

        @Error:
        """
        cmd = '/sbin/poweroff'
        if self.is_sudo():
            cmd = ' '.join(['/usr/bin/sudo', cmd])
        stdstream = shell.execute_command(cmd)
        self._success = stdstream.returncode

    def is_successed(self, ):
        r"""SUMMARY

        is_successed()

        @Return:

        @Error:
        """
        return self._success

    def set_sudo(self, ):
        r"""SUMMARY

        set_sudo()

        @Return:

        @Error:
        """
        self._sudo = True

    def unset_sudo(self, ):
        r"""SUMMARY

        unset_sudo()

        @Return:

        @Error:
        """
        self._sudo = False

    def is_sudo(self, ):
        r"""SUMMARY

        is_sudo()

        @Return:

        @Error:
        """
        return self._sudo



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _halt.py ends here
