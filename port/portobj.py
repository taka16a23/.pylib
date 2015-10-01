#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: portobj.py 290 2015-01-29 00:19:07Z t1 $
# $Revision: 290 $
# $Date: 2015-01-29 09:19:07 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:19:07 +0900 (Thu, 29 Jan 2015) $

r"""portobj -- DESCRIPTION

"""
import socket

from . import wellknownport


__revision__ = '$Revision: 290 $'
__version__ = '0.1.0'


class Port(int):
    r"""Port

    Port is a int.
    Responsibility:
    """
    # Attributes:
    min = 0
    max = 65535

    def __init__(self, port):
        r"""

        @Arguments:
        - `port`:
        """
        int.__init__(self, port)
        self._check_range(self)

    # Operations
    def _check_range(self, port):
        """function check_range

        port:

        returns
        """
        if port < self.min or self.max < port:
            # TODO: (Atami) [2014/12/03]
            raise StandardError(port)

    def __repr__(self):
        """function __repr__

        returns
        """
        return '{0.__class__.__name__}({0})'.format(self)

    def __add__(self, other):
        """function __add__

        port:

        returns
        """
        return self.__class__(super(Port, self).__add__(int(other)))

    def __radd__(self, other):
        """function __radd__

        other:

        returns
        """
        return self.__class__(super(Port, self).__radd__(int(other)))

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        """function __sub__

        other:

        returns
        """
        return self.__class__(super(Port, self).__sub__(int(other)))

    def __rsub__(self, other):
        """function __rsub__

        other:

        returns
        """
        return self.__class__(super(Port, self).__rsub__(int(other)))

    def __isub__(self, other):
        return self + other

    def __mul__(self, other):
        """function __mul__

        other:

        returns
        """
        return self.__class__(super(Port, self).__mul__(int(other)))

    def __rmul__(self, other):
        """function __rmul__

        other:

        returns
        """
        return self.__class__(super(Port, self).__rmul__(int(other)))

    def __imul__(self, other):
        return self * other

    def __div__(self, other):
        """function __div__

        other:

        returns
        """
        return self.__class__(super(Port, self).__div__(int(other)))

    def __rdiv__(self, other):
        """function __rdiv__

        other:

        returns
        """
        return self.__class__(super(Port, self).__rdiv__(int(other)))

    def __idiv__(self, other):
        return self / other

    def __mod__(self, other):
        """function __divmod__

        other:

        returns
        """
        return self.__class__(super(Port, self).__mod__(int(other)))

    def __rmod__(self, other):
        """function __rdivmod__

        other:

        returns
        """
        return self.__class__(super(Port, self).__rmod__(int(other)))

    def __imod__(self, other):
        r"""SUMMARY

        __idivmod__(other)

        @Arguments:
        - `other`:

        @Return:

        @Error:
        """
        return self % other

    def __pow__(self, other):
        """function __pow__

        other:

        returns
        """
        return self.__class__(super(Port, self).__pow__(int(other)))

    def __rpow__(self, other):
        """function __rpow__

        other:

        returns
        """
        return self.__class__(super(Port, self).__rpow__(int(other)))

    def __ipow__(self, other):
        return self ** other

    def __and__(self, other):
        """function __and__

        other:

        returns
        """
        return self.__class__(super(Port, self).__and__(int(other)))

    def __rand__(self, other):
        """function __rand__

        other:

        returns
        """
        return self.__class__(super(Port, self).__rand__(int(other)))

    def __iand__(self, other):
        return self & other

    def __or__(self, other):
        """function __or__

        other:

        returns
        """
        return self.__class__(super(Port, self).__or__(int(other)))

    def __ror__(self, other):
        """function __ror__

        other:

        returns
        """
        return self.__class__(super(Port, self).__ror__(int(other)))

    def __ior__(self, other):
        return self | other

    def __xor__(self, other):
        """function __xor__

        other:

        returns
        """
        return self.__class__(super(Port, self).__xor__(int(other)))

    def __rxor__(self, other):
        """function __rxor__

        other:

        returns
        """
        return self.__class__(super(Port, self).__rxor__(int(other)))

    def __ixor__(self, other):
        r"""SUMMARY

        __ixor__(other)

        @Arguments:
        - `other`:

        @Return:

        @Error:
        """
        return self ^ other

    def __lshift__(self, other):
        """function __lshift__

        other:

        returns
        """
        return self.__class__(super(Port, self).__lshift__(int(other)))

    def __rlshift__(self, other):
        """function __rlshift__

        other:

        returns
        """
        return self.__class__(super(Port, self).__rlshift__(int(other)))

    def __ilshift__(self, other):
        return self << other

    def __rshift__(self, other):
        """function __rshift__

        other:

        returns
        """
        return self.__class__(super(Port, self).__rshift__(int(other)))

    def __rrshift__(self, other):
        """function __rrshift__

        other:

        returns
        """
        return self.__class__(super(Port, self).__rrshift__(int(other)))

    def __irshift__(self, other):
        return self >> other


class TCPPort(Port):
    r"""TCPPort

    TCPPort is a Port.
    Responsibility:
    """
    wellknown = wellknownport.TCP

    def wellknownservice(self, ):
        r"""SUMMARY

        wellknownservice()

        @Return:

        @Error:
        """
        return self.wellknown.get(self, None)

    def connect(self, host):
        r"""SUMMARY

        connect()

        @Return:

        @Error:
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, self))
        return sock

    def connect_ex(self, host, timeout=None):
        r"""SUMMARY

        connect_ex(host)

        @Arguments:
        - `host`:

        @Return:

        @Error:
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if timeout:
            sock.settimeout(timeout)
        return sock.connect_ex((host, self))


class UDPPort(Port):
    r"""UDPPort

    UDPPort is a Port.
    Responsibility:
    """
    wellknown = wellknownport.UDP

    def wellknownservice(self, ):
        r"""SUMMARY

        wellknownservice()

        @Return:

        @Error:
        """
        return self.wellknown.get(self, None)

    def connect(self, host):
        r"""SUMMARY

        connect(host)

        @Arguments:
        - `host`:

        @Return:

        @Error:
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((host, self))
        return sock

    def connect_ex(self, host, timeout=None):
        r"""SUMMARY

        connect_ex(host)

        @Arguments:
        - `host`:

        @Return:

        @Error:
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if timeout:
            sock.settimeout(timeout)
        return sock.connect_ex((host, self))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# portobj.py ends here
