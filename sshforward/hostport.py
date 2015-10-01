#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: hostport.py 259 2014-12-21 05:20:44Z t1 $
# $Revision: 259 $
# $Date: 2014-12-21 14:20:44 +0900 (Sun, 21 Dec 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-12-21 14:20:44 +0900 (Sun, 21 Dec 2014) $

from t1.socketutil import HostName
from port import TCPPort


class HostPort(object):
    """Class HostPort
    """
    # Attributes:
    def __init__(self, host, port=22):
        r"""

        @Arguments:
        - `host`:
        - `port`:
        """
        self._host = None
        self._port = None
        self.sethost(host)
        self.setport(port)

    # Operations
    def gethost(self):
        """function gethost

        returns
        """
        return self._host

    def sethost(self, hostname):
        """function sethost

        hostname:

        returns
        """
        self._host = HostName(hostname)

    def getport(self):
        """function getport

        returns
        """
        return self._port

    def setport(self, port):
        """function setport

        port:

        returns
        """
        self._port = TCPPort(port)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# hostport.py ends here
