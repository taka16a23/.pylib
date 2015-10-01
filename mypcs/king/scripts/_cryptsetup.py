#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _cryptsetup.py 468 2015-08-19 05:49:01Z t1 $
# $Revision: 468 $
# $Date: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $

r"""_cryptsetup -- DESCRIPTION

"""
from mypcs.scripts._script import Script


class LuksOpen(Script):
    r"""LuksOpen

    LuksOpen is a Script.
    Responsibility:
    """
    def __init__(self, crypted_path, disk_name,
                 sudopasswd=None, cryptpasswd=None):
        r"""

        @Arguments:
        - `disk_name`:
        - `sudopasswd`:
        - `cryptpasswd`:
        """
        self._crypted_disk_path = crypted_path
        self._disk_name = disk_name
        self._sudopasswd = sudopasswd
        self._cryptpasswd = cryptpasswd

    def execute_script(self, shell):
        r"""SUMMARY

        execute_script(shell)

        @Arguments:
        - `shell`:

        @Return:

        @Error:
        """
        streams = shell.execute_command(
            '/usr/bin/sudo -S /sbin/cryptsetup luksOpen {} {}'
            .format(self._crypted_disk_path, self._disk_name))
        streams.stdin.write(self._sudopasswd + '\n')
        streams.stdin.write(self._cryptpasswd + '\n')


class LuksClose(Script):
    r"""LuksClose

    LuksClose is a Script.
    Responsibility:
    """
    def __init__(self, disk_path, sudopasswd=None):
        r"""

        @Arguments:
        - `sudopasswd`:
        """
        self.disk_path = disk_path
        self._sudopasswd = sudopasswd

    def execute_script(self, shell):
        r"""SUMMARY

        execute_script(shell)

        @Arguments:
        - `shell`:

        @Return:

        @Error:
        """
        streams = shell.execute_command(
            '/usr/bin/sudo -S /sbin/cryptsetup luksClose {}'
            .format(self.disk_path))
        streams.stdin.write(self._sudopasswd + '\n')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _cryptsetup.py ends here
