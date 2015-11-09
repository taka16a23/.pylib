#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: weekly.py

* Prepare
  - Pave My Server
    = Wake up My Server
    = Descrypt Disk

* Archive Downloads and MYTEMP

* CleanupFiles
  - Cleanup Downloads
  - Clean Trash

* Bookmarks Organize

* Subversion Update
  - .pylib
  - .emacs.d

* package update
  - apt-get update
  - apt-get upgrade
  - apt-get clean

* Backup
  - ntp update Qu and Ki: need before rsync
  - Qu backup to Ki
  - Ki backup to qu

* Mirroring Data
  - push to ki
  - pull from ki

* Mirror Ni
  - vmware

* Finishing
  - Ki halt
  - show result

"""
from time import sleep, time
import sys
import os
import argparse
import tempfile
import subprocess as sbp
from datetime import datetime
import easygui

from getpasswd import getpasswd
import sh
from confirm import yesnodialog
from mypcs.king import King, KingDisk
from pathhandler import PathHandler
from task import Task, TaskManager
import backup_ni_remote
import backup_ki_pull
import mirror
from StringIO import StringIO

from weekly2.log import LOG
from weekly2 import exe
from weekly2.debug import LoggingTaskManager


__version__ = '0.0.1'


EXE_PATH = PathHandler(exe.__file__).get_dirname()


class Prepare(Task):
    r"""Prepare

    Prepare is a Task.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        Task.__init__(self)
        self._started = None

    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        with King() as ki:
            ki.wakeup()
            # ki.pavedisk()
            # if not ki.ismount():
            #     LOG.fatal('Not mounted remote /data.')
            #     raise StandardError('Not mounted remote /data.')
        self._started = time()

    def get_started(self, ):
        r"""SUMMARY

        get_started()

        @Return:

        @Error:
        """
        return self._started


class Archiving(Task):
    r"""Archiving

    Archiving is a Task.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        sbp.check_call((sys.executable, EXE_PATH.join('archiving.py')))


class CleanupFiles(Task):
    r"""CleanupFiles

    CleanupFiles is a Task.
    Responsibility:
    """
    tmpdir = PathHandler(tempfile.gettempdir())
    download_dir = PathHandler('~/Downloads').expanduser()
    trash_dirs = [PathHandler('~/.local/share/Trash').expanduser(),
                  PathHandler('/data/.Trash-0'),
                  PathHandler('/media/Data/.Trash-0')]

    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        for fpath in self.tmpdir.listdir(r'.+\.torrent'):
            fpath.remove()
        for dir_ in self.trash_dirs:
            if dir_.exists() and dir_.isdir():
                try:
                    dir_.remove()
                except TypeError:
                    pass


class BookmarksOrganize(Task):
    r"""BookmarksOrganize

    BookmarksOrganize is a Task.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        os.system(u'{} {}'.format(
            sys.executable, EXE_PATH.join('open_chrome_bookmarks.py')))


class PackageUpdate(Task):
    r"""PackageUpdate

    PackageUpdate is a Task.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._result = StringIO()

    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        sbp.Popen(('/usr/bin/xfce4-terminal', '--hold', '--command={} {}'
                   .format(sys.executable, EXE_PATH.join('aptupgrade.py'))))
        sleep(150)


# class DiskSetup(Task):
#     r"""DiskSetup

#     DiskSetup is a Task.
#     Responsibility:
#     """
#     def __init__(self, prepare):
#         r"""

#         @Arguments:
#         - `prepare`:
#         """
#         Task.__init__(self)
#         self._prepare = prepare

#     def is_ready(self, ):
#         r"""SUMMARY

#         is_ready()

#         @Return:

#         @Error:
#         """
#         return True

#     def execute(self, ):
#         r"""SUMMARY

#         execute()

#         @Return:

#         @Error:
#         """
#         # wait wakeup
#         while time() - self._prepare.get_started() < 80:
#             sleep(1)

#         kidisk = KingDisk()
#         if kidisk.is_mounted():
#             return True
#         counter = 0
#         while not kidisk.is_decrypted() and counter < 3:
#             counter += 1
#             sudopass = getpasswd(
#                 '[Sudo] password for {}: '.format(kidisk.username))
#             cryptpasswd = getpasswd(
#                 'Enter passphrase for {}: '.format(kidisk.disk_name))
#             kidisk.decrypt(sudopass, cryptpasswd)
#             sleep(2)
#         if not kidisk.is_decrypted():
#             raise StandardError()
#         kidisk.mount()
#         if not kidisk.is_mounted():
#             raise StandardError()
#         return True


# class SubversionCommit(Task):
#     r"""SubversionCommit

#     SubversionCommit is a Task.
#     Responsibility:
#     """
#     def is_ready(self, ):
#         r"""SUMMARY

#         is_ready()

#         @Return:

#         @Error:
#         """
#         return True

#     def execute(self, ):
#         r"""SUMMARY

#         execute()

#         @Return:

#         @Error:
#         """
#         sbp.Popen(('emacs', '-f', 'svn-status-pylib'))
#         sleep(300)
#         sbp.Popen(('emacs', '-f', 'svn-status-emacsd'))
#         sleep(300)
#         sbp.check_call(('emacs', '-f', 'svn-status-zsh'))


class MirroringData(Task):
    r"""MirroringData

    MirroringData is a Task.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        sbp.check_call(('/usr/sbin/ntpdate', 'ntp.nict.jp'))
        mrr = mirror.DataMirror(verbose=True)
        mrr.push()
        # mrr.pull()


class BackupQueen(Task):
    r"""BackupQueen Night

    BackupQueen is a Task.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return True

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        sbp.check_call(('/usr/sbin/ntpdate', 'ntp.nict.jp'))
        backup_ni_remote.backup()


class BackupKing(Task):
    r"""BackupKing

    BackupKing is a Task.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        latest_path = PathHandler('/data/.backup/king_remote/latest')
        if not latest_path.exists():
            return False
        realpath = latest_path.readlink()
        fymonth = datetime.fromtimestamp(realpath.get_ctime()).strftime('%Y%m')
        nowymonth = datetime.now().strftime('%Y%m')
        if fymonth < nowymonth:
            return True
        return False

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        sbp.check_call(('/usr/sbin/ntpdate', 'ntp.nict.jp'))
        backup_ki_pull.backup()


# class MirroringNight(Task):
#     r"""MirroringNight

#     MirroringNight is a Task.
#     Responsibility:
#     """
#     def is_ready(self, ):
#         r"""SUMMARY

#         is_ready()

#         @Return:

#         @Error:
#         """
#         return True

#     def execute(self, ):
#         r"""SUMMARY

#         execute()

#         @Return:

#         @Error:
#         """
#         def vmware_service(action):
#             r"""SUMMARY

#             vmware_service(action)

#             @Arguments:
#             - `action`:

#             @Return:
#             """
#             try:
#                 sbp.check_call(('/usr/sbin/service', 'vmware', action))
#             except sbp.CalledProcessError as prcss:
#                 msg = str(prcss)
#                 if prcss.output:
#                     msg += '\n\n' + prcss.output
#                 easygui.msgbox(msg, 'Failed')
#                 return
#         vmware_service('start')
#         sbp.call('/usr/bin/vmware')
#         vmware_service('stop')



class Finishing(Task):
    r"""Finishing

    Finishing is a Task.
    Responsibility:
    """
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """
        return yesnodialog('Prompt', 'king halt?')

    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """
        with King() as ki:
            ki.halt()


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
    tmanager = TaskManager('/tmp/weekly2.pickle')
    tmanager.add_observer(LoggingTaskManager())
    if not sys.stdout.isatty:
        from weekly2.notifier import Notifier
        tmanager.add_observer(Notifier(3000))
    if not tmanager.is_pickled():
        prepare = Prepare()
        tmanager.add_task(prepare)
        tmanager.add_task(Archiving())
        tmanager.add_task(CleanupFiles())
        # tmanager.add_task(BookmarksOrganize())
        tmanager.add_task(PackageUpdate())
        tmanager.add_task(MirroringData())
        # tmanager.add_task(DiskSetup(prepare))
        # tmanager.add_task(SubversionCommit())
        tmanager.add_task(BackupKing())
        tmanager.add_task(BackupQueen())
        # tmanager.add_task(MirroringNight())
        tmanager.add_task(Finishing())
    tmanager.start()
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# weekly.py ends here
