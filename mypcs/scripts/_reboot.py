#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _reboot.py 464 2015-08-17 07:02:48Z t1 $
# $Revision: 464 $
# $Date: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $

r"""_reboot -- DESCRIPTION

"""
from mypcs.scripts._script import Script


class RebootScript(Script):
    r"""RebootScript

    RebootScript is a Script.
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
        cmd = '/sbin/reboot'
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
# _reboot.py ends here
