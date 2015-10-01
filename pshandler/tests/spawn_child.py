#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""spawn_child -- DESCRIPTION

for 'Process.list_children'
"""
import tempfile
from time import sleep
import subprocess
import socket

subprocess.Popen(["python", "spawn_child2.py"], stdout=subprocess.PIPE)
# subprocess.Popen(["python", "server.py"], stdout=subprocess.PIPE)


# for Process.open_files
with tempfile.TemporaryFile() as f:
    # for Process.list_connections
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('', 50000))
    sleep(30)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# spawn_child.py ends here
