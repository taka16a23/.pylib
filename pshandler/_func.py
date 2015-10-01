#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _func.py 307 2015-02-07 03:48:46Z t1 $
# $Revision: 307 $
# $Date: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $

r"""func -- DESCRIPTION

"""
import psutil

from pshandler._handler import ProcessHandler


def list_pids():
    r"""SUMMARY

    list_pids()

    @Return:

    @Error:
    """
    return psutil.pids()


def list_process():
    r"""SUMMARY

    list_process()

    @Return:

    @Error:
    """
    return [ProcessHandler(x) for x in list_pids()]


def get_boot_time():
    r"""SUMMARY

    get_boot_time()

    @Return:

    @Error:
    """
    return psutil.boot_time()


def pid_exists(pid):
    r"""SUMMARY

    pid_exists(pid)

    @Arguments:
    - `pid`:

    @Return:

    @Error:
    """
    return psutil.pid_exists(pid)




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# func.py ends here
