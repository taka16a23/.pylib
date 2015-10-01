#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$
""" nt_tunnel -- portforwarding for windows nt

$Revision$

"""
import subprocess as _subp
from os import path as _ospath
from time import sleep as _sleep

from portable import P_INTERNET
# from winutils import find_process as _find_process


__revision__ = "$Revision$"
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
        netstat = _subp.Popen(['netstat', '-an'], stdout=_subp.PIPE)
        self.tunneling_flag = ('127.0.0.1:12316' in netstat.stdout.read())
        return self.tunneling_flag

    def gettunnel(self):
        """Create port forwarding ssh.
        """
        cmd = [_ospath.join(P_INTERNET, 'portforwarder\\PortForwarder.exe'),
               '-N', 'tunnel']
        try:
            _subp.Popen(cmd)
            _sleep(5)
            return self.hastunnel()
        except:
            raise TunnelError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# nt_tunnel.py ends here
