#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: ssh_param.py 464 2015-08-17 07:02:48Z t1 $
# $Revision: 464 $
# $Date: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $

r"""ssh_param -- DESCRIPTION

"""
from mypcs.commons.inetaddress import InetAddress


class SSHParameter(object):
    """Class SSHParameter
    """
    # Attributes:
    def __init__(self, host, port=22, user=None, keyfile=None, pkey=None,
                 compress=False, password=None, conntimeout=None,
                 readtimeout=None):
        r"""

        @Arguments:
        - `hostname`:
        - `port`:
        - `user`:
        - `keyfile`:
        - `compress`:
        - `password`:
        - `conntimeout`:
        - `readtimeout`:
        """
        self._inetaddress = InetAddress(host, port)
        self._username = user
        self._keyfile = keyfile
        self._pkey = None
        self._is_compress = compress
        self._password = password
        self._conntimeout = conntimeout
        self._readtimeout = readtimeout

    # Operations
    def get_hostname(self):
        """function get_hostname

        returns str
        """
        return self._inetaddress.get_host()

    def set_hostname(self, hostname):
        """function set_hostname

        hostname: str

        returns
        """
        self._inetaddress.set_host(hostname)

    hostname = property(get_hostname, set_hostname)

    def get_port(self):
        """function get_port

        returns int
        """
        return self._inetaddress.get_port()

    def set_port(self, port=22):
        """function set_port

        port: int

        returns
        """
        self._inetaddress.set_port(port)

    port = property(get_port, set_port)

    def get_username(self, ):
        r"""SUMMARY

        get_username()

        @Return:

        @Error:
        """
        return self._username

    def set_username(self, username):
        r"""SUMMARY

        set_username(username)

        @Arguments:
        - `username`:

        @Return:

        @Error:
        """
        self._username = username

    username = property(get_username, set_username)

    def get_keyfile(self):
        """function get_keyfile

        returns str
        """
        return self._keyfile

    def set_keyfile(self, keyfile):
        """function set_keyfile

        keyfile: str

        returns
        """
        self._keyfile = keyfile

    keyfile = property(get_keyfile, set_keyfile)

    def get_pkey(self):
        """function get_pkey

        returns PKey
        """
        return self._pkey

    def set_pkey(self, pkey):
        """function set_pkey

        pkey:

        returns
        """
        self._pkey = pkey

    def delete_pkey(self, ):
        r"""SUMMARY

        delete_pkey()

        @Return:

        @Error:
        """
        self._pkey = None

    pkey = property(get_pkey, set_pkey, delete_pkey)

    def is_compress(self):
        """function is_compress

        returns bool
        """
        return self._is_compress

    def set_compress(self, compress=True):
        """function set_compress

        compress: bool

        returns
        """
        self._is_compress = compress

    def get_password(self):
        """function get_password

        returns str
        """
        return self._password

    def set_password(self, passwd):
        """function set_password

        passwd: str

        returns
        """
        self._password = passwd

    def get_connection_timeout(self):
        """function get_connection_timeout

        returns int
        """
        return self._conntimeout

    def set_connection_timeout(self, timeout):
        """function set_connection_timeout

        timeout: int

        returns
        """
        self._conntimeout = timeout

    connection_timeout = property(
        get_connection_timeout, set_connection_timeout)

    def get_reading_timeout(self):
        """function get_reading_timeout

        returns
        """
        return self._readtimeout

    def set_reading_timeout(self, timeout):
        """function set_reading_timeout

        timeout: int

        returns
        """
        self._readtimeout = timeout

    reading_timeout = property(get_reading_timeout, set_reading_timeout)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ssh_param.py ends here
