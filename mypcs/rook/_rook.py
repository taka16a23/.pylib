#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _rook.py 468 2015-08-19 05:49:01Z t1 $
# $Revision: 468 $
# $Date: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $

r"""rook -- DESCRIPTION

"""
from time import sleep

from paramiko import SSHConfig, RejectPolicy
from portscan import tcpscan
from knock import knock

from mypcs.commons import SSH_CONFIG_PATH
from mypcs.scripts._reboot import RebootScript
from mypcs.rook.scripts import LanIPScript
from mypcs._ssh.sshconnector import SSHConnector
from mypcs._ssh.agent import SSHAgentClientX11 as SSHAgentClient


class Rook(SSHConnector):
    """Class Rook
    """
    # Attributes:
    knock_open_ports = [12317, 12318, 12319]
    knock_close_ports = [12313, 12314, 12315]

    def __init__(self, compress=False, passwd=None,
                 conntimeout=None, readtimeout=None):
        r"""

        @Arguments:
        - `compress`:
        - `conntimeout`:
        - `readtimeout`:
        - `passwd`:
        """
        self.config = SSHConfig()
        self.config.parse(SSH_CONFIG_PATH.open('r'))
        lkup = self.config.lookup('ro')
        SSHConnector.__init__(self,
                             host=lkup['hostname'],
                             port=int(lkup.get('port', 22)),
                             user=lkup.get('user', None),
                             keyfile=lkup.get('identityfile', [None, ])[0],
                             compress=compress, password=passwd,
                             conntimeout=conntimeout,
                             readtimeout=readtimeout)

    # Operations
    # override
    def connect(self, ):
        r"""SUMMARY

        connect()

        @Return:

        @Error:
        """
        self.sshclient.load_system_host_keys()
        self.sshclient.set_missing_host_key_policy(RejectPolicy())
        # port check if not opened open port
        if not tcpscan(str(self.hostname), self.port):
            knock(str(self.hostname), self.knock_open_ports)
            # TODO: (Atami) [2015/08/16]
            # might need sleep
            # test from wan
            sleep(2)
        if not tcpscan(str(self.hostname), self.port):
            # TODO: (Atami) [2015/08/16]
            raise StandardError()
        # check agent has key if agent has not key, try add key
        agent = SSHAgentClient()
        if not agent.has_key(self.keyfile):
            agent.add_keys([self.keyfile])
        return super(Rook, self).connect()

    def is_active(self):
        """function is_active

        returns bool
        """
        if self.has_connection():
            return True
        if tcpscan(str(self.hostname), self.port):
            return True
        # TODO: (Atami) [2015/08/16]
        # current rook router reject all packets like icmp
        # try another check method
        return False

    def reboot(self):
        """function reboot

        returns
        """
        script = RebootScript()
        self.execute_script(script)
        return script.is_successed()

    def get_lanip(self):
        """function get_lanip

        returns
        """
        script = LanIPScript()
        self.execute_script(script)
        return script.get_result()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rook.py ends here
