#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""shell -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from paramiko.channel import Channel


class Shell(object):
    """
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, line):
        pass


class PexShell(Shell):
    """
    """
    def __init__(self, pex):
        self.shell = pex

    def read(self):
        pass

    def write(self, line):
        pass


class SSHShell(Shell):
    """
    """
    def __init__(self, shell):
        if not isinstance(shell, Channel):
            # TODO: (Atami) [2014/12/02]
            raise TypeError(shell)
        self._shell = shell
        self.settimeout(0.0)

    def read(self):
        """SUMMARY

        @Return:

        @Error:
            timeout:
        """
        recvd = ''
        while self._shell.recv_ready():
            recvd += self._shell.recv(1024)
        return recvd

    def write(self, line):
        if not line.endswith('\r\n'):
            line += '\r\n'
        self._shell.send(line)

    def settimeout(self, time):
        r"""SUMMARY

        settimeout(time)

        @Arguments:
        - `time`:

        @Return:

        @Error:
        """
        self._shell.settimeout(time)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# shell.py ends here
