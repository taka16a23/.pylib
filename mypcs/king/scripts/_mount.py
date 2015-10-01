#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _mount.py 469 2015-08-19 05:49:17Z t1 $
# $Revision: 469 $
# $Date: 2015-08-19 14:49:17 +0900 (Wed, 19 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-19 14:49:17 +0900 (Wed, 19 Aug 2015) $

r"""_mount -- DESCRIPTION

"""
from mypcs.scripts._script import Script


class MountScript(Script):
    r"""MountScript

    MountScript is a Script.
    Responsibility:
    """
    def __init__(self, something, somewere):
        r"""

        @Arguments:
        - `something`:
        - `somewere`:
        - `sudopasswd`:
        """
        self._something = something
        self._somewere = somewere

    def execute_script(self, shell):
        r"""SUMMARY

        execute_script(shell)

        @Arguments:
        - `shell`:

        @Return:

        @Error:
        """
        cmds = []
        cmds.extend(['/usr/bin/sudo', '-S'])
        cmds.extend(['/bin/mount', self._something, self._somewere])
        stream = shell.execute_command(' '.join(cmds))


class UmountScript(Script):
    r"""UmountScript

    UmountScript is a Script.
    Responsibility:
    """
    def __init__(self, somewere, passwd):
        r"""

        @Arguments:
        - `something`:
        - `somewere`:
        - `sudopasswd`:
        """
        self._somewere = somewere
        self._passwd = passwd

    def execute_script(self, shell):
        r"""SUMMARY

        execute_script(shell)

        @Arguments:
        - `shell`:

        @Return:

        @Error:
        """
        cmds = []
        cmds.extend(['/usr/bin/sudo', '-S'])
        cmds.extend(['/bin/umount', self._somewere])
        stream = shell.execute_command(' '.join(cmds))
        stream.stdin.write(self._passwd + '\n')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _mount.py ends here
