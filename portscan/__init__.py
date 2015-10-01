#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""

2012-07-18-161158knock.py

"""


import socket as _socket
import sys as _sys
from types import IntType as _IntType
from contextlib import closing as _closing


__version__ = "0.1.0"

__all__ = [ '' ]



def scan(host, port, timeout=0.5):
    """Send packet.

    """
    s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    timeout = float(timeout)
    s.settimeout(timeout)
    try:
        status = s.connect_ex((host, port))
    except:
        print "Cannot connect", host
        s.close()
        _sys.exit(1)
    s.close()
    return (0 == status)

def tcpscan(host, port, timeout=0.5):
    """Simple tcp scan.

    """
    if (not type(port) is _IntType) or (not (1 <= port <= 65535)):
        raise ValueError('port must be int. and range of 1~65535.')
    with _closing(_socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)) as sock:
        timeout = float(timeout)
        sock.settimeout(timeout)
        try:
            status = sock.connect_ex((host, port))
            return (0 == status)
        except sock.error, why:
            print why


class TcpScan(object):
    r"""
    """

    def __init__(self, host, port):
        r"""

        @Arguments:
        - `host`: (str) host address.
        - `port`: (int) port number.
        """
        self.host = host
        self.port = port

    def isopen(self, ):
        r"""SUMMARY

        isopen()

        @Return:
        """
        return tcpscan(self.host, self.port)

    def __call__(self, ):
        return self.isopen()

    def __nonzero__(self, ):
        return self.isopen()





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
