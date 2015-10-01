#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Posix_tunnel -- portforwarding for posix


"""

import subprocess as _subp
from time import sleep as _sleep

from ref.myinfo import KAGI, king, rook

__version__ = "0.1.1"


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
        netstat = _subp.Popen(['/bin/netstat', '-ltn'], stdout=_subp.PIPE)
        self.tunneling_flag = ('127.0.0.1:12316' in netstat.stdout.read())
        return self.tunneling_flag

    def gettunnel(self):
        """Create port forwarding ssh."""
        cmd = ('/usr/bin/ssh', '-f', '-N', '-i', KAGI, '-p', str(rook.PORT),
               '-L', '12316:' + king.IP + ':' + str(king.PORT),
               rook.USER + '@' + rook.HOST)
        try:
            _subp.Popen(cmd)
            _sleep(3)
            return self.hastunnel()
        except:
            raise TunnelError()


class Tunnel(object):
    """SSH Tunnel Object."""

    _tunneling_flag = False

    def __init__(self, kagi, port, local_door):
        r"""SUMMARY

        __init__(local_door)

        @Arguments:
        - `local_door`:

        @Return:
        """
        self.kagi = kagi
        self.local_door = local_door or '127.0.0.1:12316'
        self.rookport = port

    def hastunnel(self):
        """Check tunneling now.

        If listen port 12316 then return True.
        Else return False.
        """
        netstat = _subp.Popen(('/bin/netstat', '-ltn'), stdout=_subp.PIPE)
        self.tunneling_flag = (self.local_door in netstat.stdout.read())
        return self.tunneling_flag

    def gettunnel(self):
        """Create port forwarding ssh."""
        cmd = ('/usr/bin/ssh', '-f', '-N', '-i', self.kagi, '-p',
               str(self.rookport),
               '-L', '12316:' + king.IP + ':' + str(king.PORT),
               rook.USER + '@' + rook.HOST)
        try:
            _subp.Popen(cmd)
            _sleep(3)
            return self.hastunnel()
        except:
            raise TunnelError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# posix_tunnel.py ends here
