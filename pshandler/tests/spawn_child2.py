#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""spawn_child2 -- DESCRIPTION

for 'Process.recursive_children'

"""
from time import sleep
import subprocess

subprocess.Popen(["python", "-c", "print 'hi'"], stdout=subprocess.PIPE)

sleep(30)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# spawn_child2.py ends here
