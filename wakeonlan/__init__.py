#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: __init__.py


"""
from contextlib import closing as _closing
import struct as _struct
import socket as _socket

from macaddr import EUI


__version__ = '0.1.1'

__all__ = [ '' ]


def wakeonlan(mac_addr):
    """Send magic packet.

    @Arguments:
    - `mac_address`: like '00:00:00:00:00:00'
    """
    packet = '\xff' * 6 + EUI(mac_addr).pack() * 16
    with _closing(_socket.socket(_socket.AF_INET, _socket.SOCK_DGRAM)) as sock:
        sock.setsockopt(_socket.SOL_SOCKET, _socket.SO_BROADCAST, 1)
        sock.sendto(packet, ('192.168.1.255', 9))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
