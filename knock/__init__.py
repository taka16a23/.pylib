#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
knoc
k.py

"""


import sys
from socket import socket, AF_INET, SOCK_STREAM
from contextlib import closing

from portscan import tcpscan
import os as _os

def scan(host, port, timeout=0.5, verbose=False):
    """Send packet.

    Arguments:
    - ``:
    """
    with closing(socket(AF_INET, SOCK_STREAM)) as sock:
        timeout = float(timeout)
        sock.settimeout(timeout)
        print '[Scanning Ports "%s"]' % host
        try:
            status = sock.connect_ex((host, port))
        except:
            print "Cannot connect %s" % host
            sys.exit(1)
    if 0 == status:
        if verbose:
            print host + " port %d: OPEN" % port
        return True
    if verbose:
        print host + " port %d: CLOSE" % port
    return False

def knock(host, portlist, verbose=False):
    """Send sequential packet.

    Arguments:

    - `host`: target host
    - `portlist`: tuple of port number list
    """
    for port in portlist:
        tcpscan(host, port)
        if verbose:
            _os.write(1, '{0:5}, '.format(port))
    if verbose:
        print('\n')


class PortsKnocker(object):
    r"""
    """

    def __init__(self, host, ports):
        r"""

        @Arguments:
        - `host`:
        - `ports`:
        """
        self.host = host
        self.ports = ports

    def knock(self, verbose=False):
        r"""SUMMARY

        knock()

        @Return:
        """
        knock(self.host, self.ports, verbose=verbose)

    def __call__(self, verbose=False):
        r"""SUMMARY

        __call__()

        @Return:
        """
        self.knock(verbose=verbose)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
