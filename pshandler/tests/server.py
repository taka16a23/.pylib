#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""server -- DESCRIPTION

"""
# for Process.list_connections
import socket

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        client.send(data)
    client.close()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# server.py ends here
