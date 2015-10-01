#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: changehosts.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""changehost -- a parts of xcb2

ChangeHosts

mode: { Insert, Delete}
host: HOST

Errors: Access, Value

This request adds or removes the specified host from the access control
list. When the access control mechanism is enabled and a client attempts to
establish a connection to the server, the host on which the client resides must
be in the access control list, or the client must have been granted permission
by a server-dependent method, or the server will refuse the connection.

The client must reside on the same host as the server and/or have been granted
permission by a server-dependent method to execute this request (or an Access
error results).

An initial access control list can usually be specified, typically by naming a
file that the server reads at startup and reset.

The following address families are defined. A server is not required to support
these families and may support families not listed here. Use of an unsupported
family, an improper address format, or an improper address length within a
supported family results in a Value error.

For the Internet family, the address must be four bytes long. The address bytes
are in standard IP order; the server performs no automatic swapping on the
address bytes. The Internet family supports IP version 4 addresses only.

For the InternetV6 family, the address must be sixteen bytes long. The address
bytes are in standard IP order; the server performs no automatic swapping on the
address bytes. The InternetV6 family supports IP version 6 addresses only.

For the DECnet family, the server performs no automatic swapping on the address
bytes. A Phase IV address is two bytes long: the first byte contains the least
significant eight bits of the node number, and the second byte contains the most
significant two bits of the node number in the least significant two bits of the
byte and the area in the most significant six bits of the byte.

For the Chaos family, the address must be two bytes long. The host number is
always the first byte in the address, and the subnet number is always the second
byte. The server performs no automatic swapping on the address bytes.

For the ServerInterpreted family, the address may be of any length up to 65535
bytes. The address consists of two strings of ASCII characters, separated by a
byte with a value of 0. The first string represents the type of address, and the
second string contains the address value. Address types and the syntax for their
associated values will be registered via the X.Org Registry. Implementors who
wish to add implementation specific types may register a unique prefix with the
X.Org registry to prevent namespace collisions.

Use of a host address in the ChangeHosts request is deprecated. It is only
useful when a host has a unique, constant address, a requirement that is
increasingly unmet as sites adopt dynamically assigned addresses, network
address translation gateways, IPv6 link local addresses, and various other
technologies. It also assumes all users of a host share equivalent access
rights, and as such has never been suitable for many multi-user machine
environments. Instead, more secure forms of authentication, such as those based
on shared secrets or public key encryption, are recommended.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ChangeHosts', 'ChangeHostsChecked', ]


class ChangeHostsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xBxH'
    code = 109

    def _getbinary(self, mode, family, address_len, address):
        buf = _StringIO()
        buf.write(_pack(self.fmt, mode, family, address_len))
        buf.write(str(buffer(_array('B', address))))
        return buf.getvalue()

    def __call__(self, mode, family, address_len, address):
        """Request ChangeHosts X protocol.

        @Arguments:
        - `mode`:
        - `family`:
        - `address_len`:
        - `address`:

        @Return:
        VoidCookie

        @Error:
        BadAccess, BadValue
        """
        return self.request(self._getbinary(mode, family, address_len, address))


class ChangeHosts(ChangeHostsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode, family, address_len, address)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ChangeHostsChecked(ChangeHostsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(mode, family, address_len, address)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# changehost.py ends here
