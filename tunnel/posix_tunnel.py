#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""posix_tunnel -- DESCRIPTION

"""

import sys as _sys
import os as _os
import subprocess as sbp
from time import sleep as _sleep

from ref.myinfo import KAGI, king, rook


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class TunnelError(StandardError):
    pass


class Tunneling(object):
    """SSH Tunnel Object."""

    _tunneling_flag = False

    def hastunnel(self):
        """Check tunneling now.

        If listen port 12316 then return True.
        Else return False.
        """
        netstat = sbp.Popen(['/bin/netstat', '-ltn'], stdout=sbp.PIPE)
        self.tunneling_flag = ('127.0.0.1:12316' in netstat.stdout.read())
        return self.tunneling_flag

    def gettunnel(self):
        """Create port forwarding ssh."""
        cmd = ('/usr/bin/ssh', '-f', '-N', '-i', KAGI, '-p', str(rook.PORT),
               '-L', '12316:' + king.IP + ':' + str(king.PORT),
               rook.USER + '@' + rook.HOST)
        try:
            sbp.Popen(cmd)
            _sleep(3)
            return self.hastunnel()
        except:
            raise TunnelError()


class Tunnel(object):
    """SSH Tunnel Object."""
    bin = '/usr/bin/ssh'
    options = '-fN'
    cmdline_fmt = ('{0.bin} {0.options} -i{0.kagi} -p{0.port} '
                   '-L{0.bindport}:{0.host}:{0.hostport} '
                   '{0.forwarder_user}@{0.forwarder_host}')

    def __init__(self, kagi, bindport, host, hostport,
                 forwarder_user, forwarder_host, port=22):
        r"""SUMMARY

        __init__(local_door)

        @Arguments:
        - `local_door`:

        @Return:
        """
        self.kagi = kagi
        self.port = port
        self.bindport = bindport
        self.host = host
        self.hostport = hostport
        self.forwarder_user = forwarder_user
        self.forwarder_host = forwarder_host

    def hastunnel(self):
        """Check tunneling now.

        If listen port 12316 then return True.
        Else return False.
        """
        netstat = sbp.Popen(('/bin/netstat', '-ltn'), stdout=sbp.PIPE)
        localbind = '127.0.0.1:{.bindport}'.format(self)
        return localbind in netstat.stdout.read()

    def gettunnel(self):
        """Create port forwarding ssh."""
        try:
            sbp.Popen(self.cmdline, shell=True)
            _sleep(2)
            return self.hastunnel()
        except OSError:
            raise TunnelError()

    @property
    def cmdline(self, ):
        r"""SUMMARY

        cmdline()

        @Return:
        """
        return self.cmdline_fmt.format(self)

    def __call__(self, ):
        self.gettunnel()

    def __nonzero__(self, ):
        return self.hastunnel()


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# posix_tunnel.py ends here
