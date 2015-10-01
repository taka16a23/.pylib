#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$
r""" local -- DESCRIPTION

$Revision$

"""


import sys as _sys
import os as _os
import logging as _logging
from datetime import date as _date
import subprocess as _sbp
import shutil as _shutil
from glob import glob as _glob

from ref import CMD

from .utils import add2list

__revision__ = '$Revision$'
__version__ = '0.1.0'

EXCLUDE_DEFALUT = ['/lost+found',
                   '/sys/*',
                   '/dev/*',
                   '/proc/*',
                   '/run/*',
                   '/tmp/*',
                   '/share/*',
                   '/media/*',
                   '/mnt/*',
                   '/var/run/*',
                   '/var/lock/*',
                   '/lib/udev/devices/console',
                   '/lib/udev/devices/loop0',
                   '/lib/udev/devices/null',
                   '/lib/udev/devices/ppp',
                   '/lib/udev/devices/net/tun',
                   '/lib/modules/*/volatile/.mounted',
                   '/data/*',
                   '/var/cache/apt/archive/*',
                   '/home/*/.mozilla/firefox/*.default/Cache/*',
                   '/home/*/.cache/google-chrome/Default/*',
                   '/root/.mozilla/firefox/*.default/Cache/*',
                   '/root/.cache/google-chrome/Default/*',
                   '/root/.local/share/Trash/files/*',
                   '/root/.local/share/Trash/info/*',
                   ]


class LinkDestLocalBackup(object):
    """
    """
    _datefmt = '%Y%m%d'
    _full_ext = '.full'
    _incr_ext = '.incr'
    _opt = ['-a']
    _link_dest = '--link-dest='
    _excludes = EXCLUDE_DEFALUT
    _lotate_max = 30
    _log = _logging
    _bkupname = ''
    _bkupmethod = ''
    _bkupfullpath = ''
    _linkname = 'latest'
    _linkrealpath = ''

    def __init__(self, src, bkupdir, lotate=False, logname=None):
        """

        Arguments:
        - `src`:
        - `dest`:
        """
        if logname:
            self._log.basicConfig(filename=_os.path.join('/var/log', logname),
                                    level=_logging.DEBUG,
                                    format='%(asctime)s %(message)s')
        else:
            self._log = None

        self.src = src
        self.bkupdir = bkupdir
        self._lotate = lotate

    def add_exclude(self, ext):
        """SUMMARY

        @Arguments:

        - `ext`:

        @Return:
        """
        self._excludes = add2list(self._excludes, ext)

    def add_opt(self, opt):
        """SUMMARY

        @Arguments:

        - `opt`:

        @Return:
        """
        self._opt = add2list(self._opt, opt)

    def backup(self):
        """SUMMARY

        @Return:
        """
        if self.bkupmethod == self._incr_ext:
            if self._log:
                self._log.log(10, 'Start: Incremental Backup')
            self.lotate()
            self.incrementalbackup()
        else: # full backup
            if self._log:
                self._log.log(10, 'Start: Full Backup')
            self.fullbackup()
        self.makelink()

    def fullbackup(self):
        """SUMMARY

        @Return:
        """
        self._backup()

    def incrementalbackup(self):
        """SUMMARY

        @Return:
        """
        if -1 == ''.join(self._opt).find('--link-dest='):
            self._opt.append('--link-dest=' + self.linkrealpath)
        self._backup()

    def _backup(self):
        """SUMMARY

        @Return:
        """
        cmdline = self.cmdline
        print(cmdline)
        if self._log:
            self._log.log(10, 'Execute: {}'.format(cmdline))
        try:
            _sbp.check_call(cmdline, shell=True)
        except _sbp.CalledProcessError:
            _sys.exit(1)

    @property
    def cmdline(self):
        """SUMMARY

        @Return:
        """
        return ' '.join([CMD.get('rsync')] + [self.options] +
                        [self.src, self.bkupfullpath])

    @property
    def options(self):
        """SUMMARY

        @Return:
        """
        return ' '.join(self._opt + [self.excludes])

    @property
    def excludes(self):
        """SUMMARY

        @Return:
        """
        return ' '.join(['--exclude=' + x for x in self._excludes])

    @property
    def bkupfullpath(self):
        """SUMMARY

        @Return:
        """
        if not self._bkupfullpath:
            self._bkupfullpath = _os.path.join(self.bkupdir, self.bkupname)
        return self._bkupfullpath

    @property
    def bkupname(self):
        """SUMMARY

        @Return:
        """
        if not self._bkupname:
            self._bkupname = _date.today().strftime(self._datefmt)
            self._bkupname += self.bkupmethod
        return self._bkupname

    @property
    def linkrealpath(self):
        """SUMMARY

        @Return:
        """
        if not self._linkrealpath:
            self._linkrealpath = _os.path.realpath(
                _os.path.join(self.bkupdir, self._linkname))
        return self._linkrealpath

    @property
    def bkupmethod(self):

        """SUMMARY

        @Return:
        """
        if not self._bkupmethod:
            # if self._isfullexists():
            #     self._bkupmethod = self._incr_ext
            # else:
            #     self._bkupmethod = self._full_ext
            self._bkupmethod = (self._isfullexists() and self._incr_ext or
                                                         self._full_ext)
        return self._bkupmethod


    def _isfullexists(self):
        """SUMMARY

        @Return:
        """
        return self._globbkupdir('*' + self._full_ext) != []

    def _globbkupdir(self, str_):
        """SUMMARY

        @Arguments:

        - `str_`:

        @Return:
        """
        return _glob(_os.path.join(self.bkupdir, str_))

    def lotate(self):
        """SUMMARY

        @Return:
        """
        self._log.log(10, 'Lotate:')
        if not self._lotate:
            self._log.log(10, 'Lotate: disabled.')
            return
        globs = self._globbkupdir("*" + self._incr_ext)
        globs.sort()
        while self._lotate_max <= len(globs):
            oldest = globs.pop(0)
            print('will remove ' + oldest)
            if self._log:
                self._log.log(10, 'Lotate: Removed {0}'.format(oldest))
            _shutil.rmtree(oldest)

    def makelink(self):
        """SUMMARY

        @Return:
        """
        latestfullpath = _os.path.join(self.bkupdir, self._linkname)
        if _os.path.islink(latestfullpath):
            _os.unlink(latestfullpath)
        cmdline = [CMD.get('ln'), '-s', self._bkupfullpath, latestfullpath]
        print(' '.join(cmdline))
        if self._log:
            self._log.log(10, 'Link: {0}'.format(' '.join(cmdline)))
        _sbp.call(cmdline)
        if _os.path.islink(latestfullpath) and self._log:
            self._log.log(10, 'Link: {0}'.format('OK exists'))



def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# local.py ends here
