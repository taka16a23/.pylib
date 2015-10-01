#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: scripts.py 290 2015-01-29 00:19:07Z t1 $
# $Revision: 290 $
# $Date: 2015-01-29 09:19:07 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:19:07 +0900 (Thu, 29 Jan 2015) $

r"""scripts -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class Script(object):
    """
    """
    __metaclass__ = ABCMeta

    def __init__(self, receiver=None):
        self.receiver = receiver

    @abstractmethod
    def execute(self, shell):
        pass


class GetExitStatus(Script):
    r"""GetExitStatus
    
    GetExitStatus is a Script.
    Responsibility: 
    """
    def __init__(self, receiver):
        r"""
        
        @Arguments:
        - `receiver`:
        """
        Script.__init__(self, receiver)

    def execute(self, shell):
        r"""SUMMARY
        
        execute(shell)
        
        @Arguments:
        - `shell`:
        
        @Return:
        None is Failed.
        int type.

        @Error:
        """
        shell.write('echo exitstatus=$?=')
        status = None
        for line in shell.read().splitlines():
            if line.startswith(('exitstatus')):
                lis = line.split('=')
                lis.remove('exitstatus')
                lis.remove('')
                status = int(lis[0])
        self.receiver.append(status)


class Reboot(Script):
    """
    """
    def execute(self, shell):
        _, out, err = shell.exec_command('/sbin/reboot')
        if out.channel.recv_ready() and self.receiver:
            self.receiver.append(out.readlines())
        elif err.channel.recv_ready():
            raise StandardError(err.read())


class Decrypt(Script):
    """
    """
    def execute(self, shell):
        pass


class AptUpdate(Script):
    """
    """
    def execute(self, shell):
        pass


class TCPDump(Script):
    """
    """
    def execute(self, shell):
        pass


class WakeOnLan(Script):
    """
    """
    def execute(self, shell):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# scripts.py ends here
