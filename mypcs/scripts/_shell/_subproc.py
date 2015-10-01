#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _subproc.py 464 2015-08-17 07:02:48Z t1 $
# $Revision: 464 $
# $Date: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $

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
