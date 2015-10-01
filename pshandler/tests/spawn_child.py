#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: spawn_child.py 307 2015-02-07 03:48:46Z t1 $
# $Revision: 307 $
# $Date: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $

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
