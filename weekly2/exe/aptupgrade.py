#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: aptupgrade.py 482 2015-08-29 03:36:29Z t1 $
# $Revision: 482 $
# $Date: 2015-08-29 12:36:29 +0900 (Sat, 29 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-29 12:36:29 +0900 (Sat, 29 Aug 2015) $

r"""Name: aptupgrade.py

"""
import sys
import os
import argparse
import subprocess as sbp

import sh

# for debug
import cgitb
cgitb.enable(format='text')


__revision__ = '$Revision: 482 $'
__version__ = '0.0.1'


def _predef_options():
    parser = argparse.ArgumentParser(description="""""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')
    # (yas/expand-link "argparse_add_argument" t)
    return parser

def _main():
    r"""Main function."""
    parser = _predef_options()
    opts = parser.parse_args()
    # parser.print_usage()
    sbp.check_call(['/usr/bin/apt-get', 'update'])
    for line in sh.apt_get('-y', '-f', 'upgrade', _iter=True):
        self._result.write(line)
        sys.stdout.write(line)
        sys.stdout.flush()
    sbp.Popen(('apt-get', 'clean'))

    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# aptupgrade.py ends here
