#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _ping.py 464 2015-08-17 07:02:48Z t1 $
# $Revision: 464 $
# $Date: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $

r"""_ping -- DESCRIPTION

"""
from mypcs.scripts._script import Script


class PingScript(Script):
    r"""PingScript

    PingScript is a Script.
    Responsibility:
    """
    def __init__(self, host, count=1, wait=None, size=None):
        r"""

        @Arguments:
        - `wait`:
        """
        self._host = host
        self._wait = wait
        self._count = count
        self._size = size
        self._stdstream = None

    def execute_script(self, shell):
        r"""SUMMARY

        execute_script(shell)

        @Arguments:
        - `shell`:

        @Return:

        @Error:
        """
        cmds = ['/bin/ping', ]
        cmds.extend(['-c', str(self._count)])
        if not self._wait is None:
            cmds.extend(['-w', str(self._wait)])
        if not self._size is None:
            cmds.extend(['-s', str(self._size)])
        # at last
        cmds.append(self._host)
        self._stdstream = shell.execute_command(' '.join(cmds))

    def get_host(self, ):
        r"""SUMMARY

        get_host()

        @Return:

        @Error:
        """
        return self._host

    def set_host(self, host):
        r"""SUMMARY

        set_host(host)

        @Arguments:
        - `host`:

        @Return:

        @Error:
        """
        self._host = host

    host = property(get_host, set_host)

    def get_wait(self, ):
        r"""SUMMARY

        get_wait()

        @Return:

        @Error:
        """
        return self._wait

    def set_wait(self, wait):
        r"""SUMMARY

        set_wait(wait)

        @Arguments:
        - `wait`:

        @Return:

        @Error:
        """
        self._wait = wait

    def get_count(self, ):
        r"""SUMMARY

        get_count()

        @Return:

        @Error:
        """
        return self._wait

    def set_count(self, counts):
        r"""SUMMARY

        set_count(counts)

        @Arguments:
        - `counts`:

        @Return:

        @Error:
        """
        self._count = counts

    def get_size(self, ):
        r"""SUMMARY

        get_size()

        @Return:

        @Error:
        """
        return self._size

    def set_size(self, size):
        r"""SUMMARY

        set_size(size)

        @Arguments:
        - `size`:

        @Return:

        @Error:
        """
        self._size = size

    size = property(get_size, set_size)

    def get_stdstream(self, ):
        r"""SUMMARY

        get_stdstream()

        @Return:

        @Error:
        """
        return self._stdstream

    def is_successed(self, ):
        r"""SUMMARY

        is_successed()

        @Return:

        @Error:
        """
        if self._stdstream is None:
            return False
        return self._stdstream.returncode == 0



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _ping.py ends here
