#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_subprocess -- DESCRIPTION

"""
from subprocess import Popen, PIPE

from mypcs.scripts._shell._shell import Shell
from mypcs.commons.stdstream import StandardStream


class Subprocess(Shell):
    r"""Subprocess

    Subprocess is a Shell.
    Responsibility:
    """
    def execute_command(self, cmdline):
        r"""SUMMARY

        execute_command(cmdline)

        @Arguments:
        - `cmdline`:

        @Return:

        @Error:
        """
        # TODO: (Atami) [2015/08/16]
        # many buffer will deadlock
        proc = Popen(
            cmdline, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        returncode = proc.wait()
        return StandardStream(proc.stdin, proc.stdout, proc.stderr, returncode)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _subprocess.py ends here
