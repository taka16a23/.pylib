#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import re
import socket


__version__ = "0.1.0"

__all__ = [ '' ]


class HostName(str):
    r"""
    """
    # TODO: (Atami) [2014/12/11]
    # check hostname by regexp
    address_regex = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]'
                               r'|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}'
                               r'|2[0-4][0-9]|25[0-5])$')
    name_regex = re.compile(r'^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]'
                            r'*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9]'
                            r'[A-Za-z0-9\-]*[A-Za-z0-9])$')

    def __init__(self, name):
        r"""

        @Arguments:
        - `name`:
        """
        super(HostName, self).__init__(name)
        if not (self.address_regex.match(self) or self.name_regex.match(self)):
            # TODO: (Atami) [2014/12/11]
            raise StandardError('"{}" is not hostname.'.format(self))

    @property
    def ipv4(self, ):
        r"""SUMMARY

        ipv4()

        @Return:
        """
        return self.gethostbyname()

    @property
    def fqdn(self, ):
        r"""SUMMARY

        fqdn()

        @Return:
        """
        return self.getfqdn()

    def gethostbyname(self, ):
        r"""SUMMARY

        gethostbyname()

        @Return:
        """
        return socket.gethostbyname(self)

    def getfqdn(self, ):
        r"""SUMMARY

        getfqdn()

        @Return:
        """
        return socket.getfqdn(self)

    def __repr__(self):
        return '{0.__class__.__name__}("{1}")'.format(self, self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
