#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
