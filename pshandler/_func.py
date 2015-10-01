#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
