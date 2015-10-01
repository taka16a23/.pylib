#!/usr/bin/env python
# -*- coding: utf-8 -*-
from getpass import getuser

from sshforward.hostport import HostPort


class SSHHost(object):
    """Class SSHHost
    """
    # Attributes:
    def __init__(self, host, port=22, user=None, key=None):
        r"""

        @Arguments:
        - `host`:
        - `port`:
        - `user`:
        - `key`:
        """
        self._hostport = HostPort(host, port)
        self._user = None
        self.setuser(user)
        self._key = key

    # Operations
    def getport(self):
        """function getport

        returns
        """
        return self._hostport.getport()

    def setport(self, port=22):
        """function setport

        port:

        returns
        """
        self._hostport.setport(port)

    def gethost(self):
        """function gethost

        returns
        """
        return self._hostport.gethost()

    def sethost(self, hostname):
        """function sethost

        hostname:

        returns
        """
        self._hostport.sethost(hostname)

    def getkey(self):
        """function getkey

        returns
        """
        return self._key

    def setkey(self, keypath):
        """function setkey

        keypath:

        returns
        """
        self._key = keypath

    def getuser(self):
        """function getuser

        returns
        """
        return self._user

    def setuser(self, user=None):
        """function setuser

        user:

        returns
        """
        self._user = user or getuser()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sshhost.py ends here
