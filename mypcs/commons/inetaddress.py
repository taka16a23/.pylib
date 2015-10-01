#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""inetaddress -- DESCRIPTION

"""
import re
import socket


class HostName(object):
    r"""HostName

    HostName is a object.
    Responsibility:
    """
    # TODO: (Atami) [2015/08/16]
    _address_regex = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]'
                               r'|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}'
                               r'|2[0-4][0-9]|25[0-5])$')
    _name_regex = re.compile(r'^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]'
                            r'*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9]'
                            r'[A-Za-z0-9\-]*[A-Za-z0-9])$')

    def __init__(self, host):
        r"""

        @Arguments:
        - `host`:
        """
        self._host = None
        self.set_hostname(host)

    def get_hostname(self, ):
        r"""SUMMARY

        get_hostname()

        @Return:

        @Error:
        """
        return self._host

    def set_hostname(self, hostname):
        r"""SUMMARY

        set_hostname(hostname)

        @Arguments:
        - `hostname`:

        @Return:

        @Error:
        """
        host = str(hostname)
        self._host = host

    hostname = property(get_hostname, set_hostname)

    def get_hostbyname(self, ):
        r"""SUMMARY

        get_hostbyname()

        @Return:

        @Error:
        """
        return socket.gethostbyname(self._host)

    ipv4 = property(get_hostbyname)

    def get_fqdn(self, ):
        r"""SUMMARY

        get_fqdn()

        @Return:

        @Error:
        """
        return socket.getfqdn(self._host)

    def __repr__(self):
        return self._host

    def __str__(self):
        return self._host

    def __eq__(self, other):
        return other in (self._host, self.ipv4)

    def __ne__(self, other):
        return not self == other

    def __hash__(self, ):
        return hash(self._host)


class InetAddress(object):
    r"""InetAddress

    InetAddress is a object.
    Responsibility:
    """
    def __init__(self, host, port):
        r"""

        @Arguments:
        - `host`:
        - `port`:
        """
        self._host = HostName(host)
        self._port = port

    def get_host(self, ):
        r"""SUMMARY

        get_host()

        @Return:

        @Error:
        """
        return self._host

    def set_host(self, host):
        r"""SUMMARY

        set_host(host)

        @Arguments:
        - `host`:

        @Return:

        @Error:
        """
        self._host.set_hostname(host)

    host = property(get_host, set_host)

    def get_port(self, ):
        r"""SUMMARY

        get_port()

        @Return:

        @Error:
        """
        return self._port

    def set_port(self, port):
        r"""SUMMARY

        set_port(port)

        @Arguments:
        - `port`:

        @Return:

        @Error:
        """
        self._port = port

    port = property(get_port, set_port)

    def __eq__(self, other):
        if isinstance(other, (InetAddress, )):
            return (self.host, self.port) == (other.host, other.port)
        return (self.host, self.port) == other

    def __ne__(self, other):
        return not self == other

    def __hash__(self, ):
        return hash((self.host, self.port))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# inetaddress.py ends here
