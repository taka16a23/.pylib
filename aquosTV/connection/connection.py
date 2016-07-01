#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""connection -- DESCRIPTION

"""


class Connection(object):
    """Connection

    Connection is a object.
    Responsibility:
    """
    def __init__(self, socket):
        """

        @Arguments:
        """
        self._socket = socket

    def send(self, line):
        """SUMMARY

        send(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        self._socket.send(line + '\n')
        return self._socket.recv(1024)

    def disconnect(self, ):
        """SUMMARY

        disconnect()

        @Return:

        @Error:
        """
        self._socket.close()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# connection.py ends here
