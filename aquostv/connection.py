#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: connection.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
from . import socketbuilder
from . import director
from . import authenticator
from . import account


class Connection(object):
    """Class Connection
    """
    # Attributes:
    def __init__(self, ip, port, user, password):
        r"""

        @Arguments:
        - `socket`:
        - `account`:
        """
        socketdirector = director.SocketDirector(
            socketbuilder.AquosSocketBuilder(ip, port))
        self._socket = socketdirector.direct()
        print(self._socket.recv(1024))
        self._account = account.Account(user, password)
        self._login()

    # Operations
    def send(self, order):
        """function send

        order:

        returns Reciever
        """
        self._socket.send(order.get_orderline())
        return order.receive(self._socket.recv(1024))

    def close(self):
        """function close

        returns
        """
        self._socket.close()

    def get_socket(self):
        """function get_socket

        returns
        """
        return self._socket

    def set_socket(self, sock):
        """function set_socket

        returns
        """
        self._socket = sock

    def get_account(self):
        """function get_account

        returns
        """
        return self._account

    def set_account(self, accnt):
        """function set_account

        returns
        """
        self._account = accnt

    def _login(self, ):
        """function login

        account:

        returns
        """
        logindirector = director.LoginDirector(
            authenticator.AquosAuthenticator(self))
        logindirector.direct()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# connection.py ends here
