#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: sshportforward.py 305 2015-02-07 03:47:58Z t1 $
# $Revision: 305 $
# $Date: 2015-02-07 12:47:58 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:47:58 +0900 (Sat, 07 Feb 2015) $

from subprocess import Popen, PIPE

import paramiko
from pshandler import list_process
from t1.socketutil import HostName
from port import TCPPort

import sshforwarder
from sshforward.sshhost import SSHHost
from sshforward.server import forward_tunnel
from sshforward.err import BindingPortError


class PortForward(object):
    """Class PortForward
    """
    # Attributes:
    exepath = sshforwarder.__file__

    def __init__(self, sshhost, target, sshport=22, user=None, key=None):
        r"""

        @Arguments:
        - `sshhost`:
        - `target`:
        - `sshport`:
        - `user`:
        - `key`:
        """
        self._sshhost = SSHHost(sshhost, port=sshport, user=user, key=key)
        self._target = HostName(target)

    # Operations
    def _getcmdlines(self, lport, tport):
        r"""SUMMARY

        _getcmdlines()

        @Return:

        @Error:
        """
        cmds = []
        cmds.append('python')
        cmds.append(self.exepath)
        cmds.append('-p')
        cmds.append(str(lport))
        cmds.append('-u')
        cmds.append(str(self.get_sshuser()))
        key = self.get_sshkey()
        if key:
            cmds.append('-k')
            cmds.append(str(self.get_sshkey()))
        cmds.append('-r')
        cmds.append('{}:{}'.format(self.get_target(), tport))
        cmds.append('{}:{}'.format(self.get_sshhost(), self.get_sshport()))
        return cmds

    def spawn(self, localport, targetport):
        """function spawn

        localport:
        targetport:

        returns Process
        """
        result = TCPPort(localport).connect_ex('localhost')
        if result == 0:
            raise BindingPortError('using local {} port'.format(localport))
        cmdlines = self._getcmdlines(localport, targetport)
        return Popen(cmdlines, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    def serve_forever(self, localport, targetport, look_for_keys=True,
                      passwd=None):
        """function serve_forever

        localport:
        targetport:

        returns
        """
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.RejectPolicy())
        client.connect(
                self.get_sshhost(), self.get_sshport(),
                username=self.get_sshuser(), key_filename=self.get_sshkey(),
                look_for_keys=look_for_keys, password=passwd)
        forward_tunnel(localport, self.get_target(), str(targetport), client)

    def list_process(self):
        """function list_process

        returns
        """
        pyps = [p for p in list_process()
                if p.get_name() == 'python' and self.exepath in p.get_cmdline()]
        return pyps

    def get_sshhost(self):
        """function get_sshhost

        returns SSHHost
        """
        return self._sshhost.gethost()

    def set_sshhost(self, host):
        """function set_sshhost

        host:

        returns
        """
        self._sshhost.sethost(host)

    def get_target(self):
        """function get_target

        returns HostName
        """
        return self._target

    def set_target(self, host):
        """function set_target

        host:

        returns
        """
        self._target = HostName(host)

    def get_sshuser(self):
        """function get_sshuser

        returns
        """
        return self._sshhost.getuser()

    def set_sshuser(self, user=None):
        """function set_sshuser

        user:

        returns
        """
        self._sshhost.setuser(user)

    def get_sshport(self):
        """function get_sshport

        returns
        """
        return self._sshhost.getport()

    def set_sshport(self, port=22):
        """function set_sshport

        port:

        returns
        """
        self._sshhost.setport(port)

    def get_sshkey(self):
        """function get_sshkey

        returns
        """
        return self._sshhost.getkey()

    def set_sshkey(self, keypath=None):
        """function set_sshkey

        keypath:

        returns
        """
        self._sshhost.setkey(keypath)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# portforward.py ends here
