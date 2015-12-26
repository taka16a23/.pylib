#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""coop_database -- DESCRIPTION

"""
from time import sleep
import sys
import subprocess as sbp
from mygoogle import chrome

def _main():
    sbp.check_call(('wol', '--silent'))
    sleep(10)
    chrome.run('http://192.168.1.123/coop')
    sleep(5)
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# coop_database.py ends here
