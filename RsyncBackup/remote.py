#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" remote -- DESCRIPTION


"""
import sys as _sys
import os as _os
import logging as _logging
import subprocess as _sbp
from glob import glob as _glob

from ref import CMD

from .local import LinkDestLocalBackup


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class LinkDestRemoteBackup(LinkDestLocalBackup):
    """
    """
    _mntpoint = '/mnt/sshfs'

    def __init__(self, src, bkupdir, rname, lotate=False, logname=None):
        """
        """
        self.src = src
        self.rname = rname
        self.bkupdir = bkupdir
        self.lbkupdir = self._mntpoint
        self.rbkupdir = self.rname + ':' + self.bkupdir
        self.linkpath = _os.path.join(self.bkupdir, self._linkname)
        self._lotate = lotate
        if logname:
            self._log = _logging.basicConfig(
                filename=_os.path.join('/var/log', logname),
                level=_logging.DEBUG,
                format='%(asctime)s %(message)s')
        else:
            self._log = None

    def backup(self):
        """SUMMARY

        @Return:
        """
        self._sshfs()
        if self.bkupmethod == self._incr_ext:
            if self._log:
                self._log.log(10, 'Start: Incremental Backup')
            self.lotate()
            self.incrementalbackup()
        else: # full buckup
            if self._log:
                self._log.log(10, 'Start: Full Backup')
            self.fullbackup()
        self.makelink()

    def restore(self):
        """SUMMARY

        @Return:
        """
        self.add_opt(['-z', '-v'])
        cmdline = ' '.join([CMD.get('rsync')] + ['--delete', '--force'] +
                           [self.options] +
                           [self.rname + ':' + self.linkpath + '/'] +
                           ['/'])
        _sbp.check_call(cmdline, shell=True)

    @property
    def linkrealpath(self):
        """SUMMARY

        @Return:
        """
        if not self._linkrealpath:
            realpath, join = _os.path.realpath, _os.path.join
            self._linkrealpath = realpath(join(self.lbkupdir, self._linkname))
        return self._linkrealpath

    @property
    def cmdline(self):
        """SUMMARY

        @Return:
        """
        return ' '.join([CMD.get('rsync')] + [self.options] +
                        [self.src, self.rname + ':' + self.bkupfullpath])

    def _globbkupdir(self, str_):
        """SUMMARY

        @Arguments:

        - `str_`:

        @Return:
        """
        return _glob(_os.path.join(self.lbkupdir, str_))

    def lotate(self):
        """SUMMARY

        @Return:
        """
        pass

    def makelink(self):
        """SUMMARY

        @Return:
        """
        pjoin, islink, unlink = _os.path.join, _os.path.islink, _os.unlink
        # delete link
        linklocalfullpath = pjoin(self.lbkupdir, self._linkname)
        if islink(linklocalfullpath):
            unlink(linklocalfullpath)
        # make link
        cmdline = ['ssh', self.rname, "'" + CMD.get('ln'),
                    '-s', self.bkupfullpath,
                    pjoin(self.bkupdir, self._linkname) + "'"]
        if self._log:
            self._log.log(10, 'Link: {0}'.format(' '.join(cmdline)))
        print(' '.join(cmdline))
        _sbp.check_call([' '.join(cmdline)], shell=True)

    def _sshfs(self):
        """SUMMARY

        @Return:
        """
        ismount, exists, mkdir = _os.path.ismount, _os.path.exists, _os.mkdir
        if ismount('/mnt'):
            _sbp.Popen([CMD.get('umount'), '/mnt'])
        if ismount(self._mntpoint):
            _sbp.Popen([CMD.get('umount'), self._mntpoint])
        if not exists(self._mntpoint):
            mkdir(self._mntpoint)
        _sbp.check_call([CMD.get('sshfs'), self.rbkupdir, self._mntpoint])

    def __exit__(self, type, value, tb):
        """SUMMARY

        @Return:
        """
        for command, location in (('umount', self._mntpoint),
                                  ('rmdir', self._mntpoint)):
            try:
                _sbp.Popen([CMD.get(command), location])
            except:
                pass


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# remote.py ends here
