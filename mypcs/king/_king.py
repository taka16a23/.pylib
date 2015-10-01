#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_king -- DESCRIPTION

"""
from time import sleep
import subprocess as sbp

import psutil
from paramiko import SSHConfig, RejectPolicy

from macaddr import EUI

from mypcs import rook
from mypcs.commons import SSH_CONFIG_PATH
from mypcs.scripts import PingScript, RebootScript, HaltScript
from mypcs._ssh.agent import SSHAgentClientX11 as SSHAgentClient
from mypcs._ssh.sshconnector import SSHConnector


KING_STARTUP_TIME = 60


class King(SSHConnector):
    """Class King
    """
    localip = '192.168.1.123'
    macaddr = EUI('00:1:80:61:d8:47')
    macaddr.set_format('unix')

    # Attributes:
    def __init__(self, compress=False, passwd=None, conntimeout=None,
                 readtimeout=None):
        r"""

        @Arguments:
        - `compress`:
        - `passwd`:
        - `conntimeout`:
        - `readtimeout`:
        """
        self.config = SSHConfig()
        self.config.parse(SSH_CONFIG_PATH.open('r'))
        lkup = self.config.lookup('ki')
        SSHConnector.__init__(self,
                             host=lkup['hostname'],
                             port=int(lkup.get('port', 22)),
                             user=lkup.get('user', None),
                             keyfile=lkup.get('identityfile', [None, ])[0],
                             compress=compress, password=passwd,
                             conntimeout=conntimeout,
                             readtimeout=readtimeout)
        self.router = rook.Rook()

    # Operations
    def _list_tunnel_process(self, ):
        r"""SUMMARY

        _list_tunnel_process()

        @Return:

        @Error:
        """
        arg = '{}:{}:{}'.format(self.port, self.localip, 12316)
        return [x for x in psutil.get_process_list()
                if x.name() == 'ssh' and arg in x.cmdline()]

    def is_opened_tunnel(self, ):
        r"""SUMMARY

        is_opened_tunnel()

        @Return:

        @Error:
        """
        return bool(self._list_tunnel_process())

    def open_tunnel(self, ):
        r"""SUMMARY

        open_tunnel()

        @Return:

        @Error:
        """
        cmds = ['/usr/bin/ssh']
        cmds.extend(['-f', '-N', ])
        cmds.extend(['-i', '{}'.format(self.router.keyfile)])
        cmds.extend(['-p', '{}'.format(self.router.port)])
        cmds.extend(['-L', '{}:{}:{}'.format(self.port, self.localip, 12316)])
        cmds.extend(['{}@{}'.format(
            self.router.username, self.router.hostname)])
        proc = sbp.Popen(cmds, stdout=sbp.PIPE, stderr=sbp.PIPE)
        retcode = proc.wait()
        return retcode == 0

    def connect(self):
        """function connect

        returns
        """
        if not self.is_active():
            return False
        self.sshclient.load_system_host_keys()
        self.sshclient.set_missing_host_key_policy(RejectPolicy())
        # check agent has key if agent has not key, try add key
        agent = SSHAgentClient()
        if not agent.has_key(self.keyfile):
            agent.add_keys([self.keyfile])
        # check tunnel to king if not tunnel exists, try launch tunneling
        if not self.is_opened_tunnel():
            self.open_tunnel()
            count = 0
            while count < 5 and not self.is_opened_tunnel():
                sleep(1)
                count += 1
        self.router.close()
        return super(King, self).connect()

    def is_active(self):
        """function is_active

        returns
        """
        if self.has_connection():
            return True
        if not self.router.has_connection():
            self.router.connect()
        ping = PingScript(self.localip, wait=1, size=1)
        self.router.execute_script(ping)
        if not ping.is_successed():
            return False
        if 'bytes from' in ping.get_stdstream().read_stdout():
            return True
        return False

    def wakeup(self):
        """function wakeup

        returns
        """
        if not self.router.has_connection():
            self.router.connect()
        wol = rook.scripts.WOLScript(self.macaddr)
        self.router.execute_script(wol)
        return wol.is_successed()

    def reboot(self):
        """function reboot

        returns
        """
        if not self.has_connection():
            self.connect()
        reboot = RebootScript(sudo=True)
        self.execute_script(reboot)
        return reboot.is_successed()

    def halt(self):
        """function halt

        returns
        """
        if not self.has_connection():
            self.connect()
        halt = HaltScript(sudo=True)
        self.execute_script(halt)
        return halt.is_successed()

    def __repr__(self):
        return '<{0.__class__.__name__} (connecting={1})>'.format(
            self, self.has_connection())




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _king.py ends here
