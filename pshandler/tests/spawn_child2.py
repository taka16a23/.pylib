#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: spawn_child2.py 307 2015-02-07 03:48:46Z t1 $
# $Revision: 307 $
# $Date: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $

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
