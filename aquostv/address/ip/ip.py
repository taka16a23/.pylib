#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: ip.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

r"""ip -- DESCRIPTION

"""
from .IPAbstract import IPAbstract


class IP(IPAbstract):
    """Class IP
    """
    # Attributes:
    def __init__(self, ip):
        r"""

        @Arguments:
        - `ip`:
        """
        self._ip = ip

    # Operations
    def get(self):
        """function get

        returns
        """
        return self._ip

    def set(self, ip):
        """function set

        returns
        """
        self._ip = ip

    def __str__(self):
        """function __str__

        returns
        """
        return self.get()

    def get_whois(self):
        """function get_whois

        returns
        """
        raise NotImplementedError()

    def get_location(self):
        """function get_location

        returns
        """
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ip.py ends here
