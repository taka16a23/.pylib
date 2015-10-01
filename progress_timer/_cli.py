#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _cli.py 467 2015-08-17 16:32:37Z t1 $
# $Revision: 467 $
# $Date: 2015-08-18 01:32:37 +0900 (Tue, 18 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-18 01:32:37 +0900 (Tue, 18 Aug 2015) $

r"""_cli -- DESCRIPTION

"""
from time import sleep
import sys


class ProgressTimerCLI(object):
    r"""ProgressTimerCLI

    ProgressTimerCLI is a object.
    Responsibility:
    """
    def progress(self, sec, msg='Waiting'):
        r"""SUMMARY

        progress(sec, msg='Waiting')

        @Arguments:
        - `sec`:
        - `msg`:

        @Return:

        @Error:
        """
        secounds = abs(sec) # convert to integer if sec is negative
        count = 0
        while count < sec:
            count += 1
            sleep(1)
            sys.stdout.write('\r')
            sys.stdout.write(msg + ': ')
            sys.stdout.write('{}/{}s'.format(count, sec))
            sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()

    def __call__(self, sec, msg='Waiting'):
        self.progress(sec, msg)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _cli.py ends here
