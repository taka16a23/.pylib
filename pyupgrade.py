#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: pyupgrade.py 89 2013-12-07 10:11:49Z t1 $
# $Revision: 89 $
# $Date: 2013-12-07 19:11:49 +0900 (Sat, 07 Dec 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-12-07 19:11:49 +0900 (Sat, 07 Dec 2013) $

r"""Name: __init__.py


"""
import argparse
import os
import sys
import xmlrpclib
import subprocess as _sbp
import threading
from distutils.version import LooseVersion


import argparse

try:
    import pip
except ImportError, err:
    print(err)


__revision__ = "$Revision: 89 $"
__version__ = "0.1.0"

__all__ = [ '' ]


# for thread
OUTOFDATES = []


class OutofDate(object):
    r"""
    """

    def __init__(self, name, current, latest):
        r"""

        @Arguments:
        - `name`:
        - `latest`:
        - `current`:

        """
        self.name = name
        self.current = current
        self.latest = latest


def upgrade(name):
    r"""SUMMARY

    upgrade(name)

    @Arguments:
    - `name`:

    @Return:
    """
    try:
        _sbp.check_call(['pip', 'install', '--upgrade', name])
        return True
    except _sbp.CalledProcessError, err:
        return False
    # pip.main(['install', '--upgrade', name])

def get_outofdates():
    r"""SUMMARY

    get_outofdates()

    @Return:
    """
    mainthread = threading.currentThread()
    for pkg in pip.get_installed_distributions():
        thrd = threading.Thread(target=comfirm_version, args=(pkg, ))
        thrd.start()
    for thd in threading.enumerate():
        if mainthread != thd:
            thd.join()
    sys.stdout.flush()
    print '\n'


def comfirm_version(pkg):
    r"""SUMMARY

    comfirm_version(current, latest)

    @Arguments:
    - `current`:
    - `latest`:

    @Return:
    """
    # FIXME: (Atami) [2013/12/03]
    # freezing print by wxpython
    global OUTOFDATES # for thread
    project_name = pkg.project_name
    os.write(1, '\rChecking {0:40}'.format(project_name))
    current = pkg.version
    pypi = xmlrpclib.ServerProxy("http://pypi.python.org/pypi")
    latest = pypi.package_releases(project_name)
    # TODO: (Atami) [2013/12/03]
    # true compare version
    if latest and LooseVersion(current) < LooseVersion(latest[0]):
        OUTOFDATES.append(OutofDate(project_name, current, latest[0]))


def cli():
    r"""SUMMARY

    cli()

    @Return:
    """
    # TODO: (Atami) [2013/12/03]
    # choose by name
    global OUTOFDATES
    get_outofdates()
    try:
        numfmt = '{0:>{1}}) '
        leftfmt = '{0:<{1}} '
        centerfmt = '{0:<{1}}'
        while 1:
            listlen = len(OUTOFDATES)
            leftmax = max([len(x.name) for x in OUTOFDATES])
            centermax = max([len(x.current) for x in OUTOFDATES])
            numwide = len(str(listlen)) + 2 # digit len
            for i, pkg in enumerate(OUTOFDATES, start=1):
                stream = (numfmt.format(i, numwide) +
                          leftfmt.format(pkg.name, leftmax) +
                          centerfmt.format(pkg.current, centermax) +
                          '{0:^4}'.format('=>') +
                          pkg.latest)
                print(stream)
            print('\n' + numfmt.format('0', numwide) + ' exit')
            print(numfmt.format('00', numwide) + ' reflesh\n')
            menu_num = raw_input('input number >')
            if menu_num in ('0', 'exit'):
                sys.exit(os.EX_OK)
            if menu_num == '00':
                # FIXME: (Atami) [2013/12/03]
                OUTOFDATES = []
                reload(pip)
                get_outofdates()
                continue
            if not menu_num:
                continue
            if listlen < int(menu_num):
                print('\nout of range {}\n'.format(menu_num))
                continue
            try:
                target = OUTOFDATES.pop(int(menu_num) - 1)
                print('upgrading {}'.format(target.name))
                upgrade(target.name)
            except KeyboardInterrupt:
                pass
            except:
                print('Fatal error')

    except KeyboardInterrupt:
        sys.exit(os.EX_OK)


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
    parser = _predef_options()
    opts = parser.parse_args()
    # parser.print_usage()
    cli()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
