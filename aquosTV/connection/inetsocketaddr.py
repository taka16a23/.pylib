#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""inetsocketaddr -- DESCRIPTION

"""


class InetSocketAddress(object):
    """InetSocketAddress

    InetSocketAddress is a object.
    Responsibility:
    """
    def __init__(self, host, port):
        """

        @Arguments:
        - `ip`:
        - `port`:
        """
        self.host = host
        self.port = port

    def get_host(self, ):
        """SUMMARY

        get_host()

        @Return:

        @Error:
        """
        return self.host

    def set_host(self, host):
        """SUMMARY

        set_host(host)

        @Arguments:
        - `host`:

        @Return:

        @Error:
        """
        self.host = host

    def get_port(self, ):
        """SUMMARY

        get_port()

        @Return:

        @Error:
        """
        return self.port

    def set_port(self, port):
        """SUMMARY

        set_port(port)

        @Arguments:
        - `port`:

        @Return:

        @Error:
        """
        self.port = port



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# inetsocketaddr.py ends here
