#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" mypsutil -- DESCRIPTION


"""
from time import sleep
import sys
import time as _time
import psutil as _psutil
if sys.version_info < (2, 4):
    from sets import Set as set

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')

__version__ = '0.1.0'


class PsChecker(object):
    """
    """

    def __init__(self):
        """

        Arguments:
        - `names`:
        """
        self._ps = _psutil.get_process_list()

    def name_exists(self, name):
        """SUMMARY

        @Arguments:

        - `name`:

        @Return:
        """
        for ps in self._ps:
            if name == ps.name():
                return True
        return False

## check process name exists
#
def psexists(name):
    """Check process name exists

    @Arguments:
    - `name`:

    @Return:
    """
    for ps in _psutil.get_process_list():
        if name == ps.name():
            return ps
    return None

def waitclose(psname, interval=1):
    r"""SUMMARY

    waitclose(interval=1)

    @Arguments:
    - `interval`:

    @Return:
    """
    try:
        while psexists(psname):
            sleep(interval)
    except _psutil.NoSuchProcess:
        return
    except KeyboardInterrupt:
        pass


def get_running_time():
    """SUMMARY

    @Return:
    """
    return _time.time() - _psutil.boot_time()

def isless_running_time(sec):
    """SUMMARY

    @Arguments:
    - `sec`: epoc time

    @Return:
    """
    return get_running_time() < sec

def get_connects_samba():
    """SUMMARY

    @Return:
    """
    # smb_ps = []
    # for ps in _psutil.get_process_list():
        # if ps.name == 'smbd':
            # smb_ps.append(ps)
    # ip = []
    # for ps in smb_ps:
        # for con in ps.get_connections():
           # if con.raddr:
               # ip.append(con.raddr)
    # return list(set(ip))
    # ip = []
    # for ps in (ps for ps in _psutil.get_process_list() if ps.name == 'smbd'):
        # for con in ps.get_connections():
           # if con.raddr:
               # ip.append(con.raddr)
    # return list(set(ip))
    return list({con.raddr for ps in
                (ps for ps in _psutil.get_process_list() if ps.name() == 'smbd')
                for con in ps.get_connections() if con.raddr})


def waitbusy(percent=20.0, interval=1):
    r"""SUMMARY

    waitbusy(percent=20.0, interval=1)

    @Arguments:
    - `percent`:
    - `interval`:

    @Return:
    """
    try:
        while 1:
            if _psutil.cpu_percent(interval=1, percpu=False) < percent:
                break
            sleep(interval)
    except KeyboardInterrupt:
        print('KeyboardInterrupted!!')


def test():
    pass


if __name__ == '__main__':
    test()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mypsutil.py ends here
