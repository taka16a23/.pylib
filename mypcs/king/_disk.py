#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_disk -- DESCRIPTION

"""
from time import sleep

from progress_timer.functions import progress
from pathhandler import PathHandler

from mypcs.king._king import King, KING_STARTUP_TIME
from mypcs.king.scripts._cryptsetup import LuksClose, LuksOpen
from mypcs.king.scripts._mount import MountScript, UmountScript


class KingDisk(object):
    """Class KingDisk
    """
    disk_path = PathHandler('/data')
    archive_path = disk_path.join('archive')
    disk_name = 'data_crypt'

    # Attributes:
    def __init__(self, ):
        r"""
        """
        self._king = King()

    # Operations
    @property
    def hostname(self, ):
        r"""SUMMARY

        hostname()

        @Return:

        @Error:
        """
        return self._king.hostname

    @property
    def keyfile(self, ):
        r"""SUMMARY

        keyfile()

        @Return:

        @Error:
        """
        return self._king.keyfile

    @property
    def port(self, ):
        r"""SUMMARY

        port()

        @Return:

        @Error:
        """
        return self._king.port

    @property
    def username(self, ):
        r"""SUMMARY

        username()

        @Return:

        @Error:
        """
        return self._king.username

    @property
    def localip(self, ):
        r"""SUMMARY

        localip()

        @Return:

        @Error:
        """
        return self._king.localip

    @property
    def macaddr(self, ):
        r"""SUMMARY

        macaddr()

        @Return:

        @Error:
        """
        return self._king.macaddr

    def _connect_king(self, ):
        r"""SUMMARY

        _connect_king()

        @Return:

        @Error:
        """
        if self._king.has_connection():
            return
        if not self._king.is_active():
            self._king.wakeup()
            progress(KING_STARTUP_TIME, msg='Waking King')
        count = 0
        while not self._king.is_active() and count < 10:
            sleep(1)
            count += 1
        if not self._king.is_active():
            # TODO: (Atami) [2015/08/18]
            raise StandardError()
        self._king.connect()

    def is_decrypted(self):
        """function is_decrypted

        returns
        """
        if not self._king.is_active():
            return False
        self._connect_king()
        return self._king.test_command('test -b /dev/mapper/data_crypt') == 0

    def decrypt(self, sudopasswd, cryptpasswd):
        """function decrypt

        returns
        """
        self._connect_king()
        self._king.execute_script(LuksOpen(
            '/dev/mapper/VG-data', self.disk_name, sudopasswd, cryptpasswd))
        sleep(1)
        return self.is_decrypted()

    def crypt(self, sudopasswd):
        """function crypt

        returns
        """
        self._connect_king()
        diskpath = PathHandler('/dev/mapper').join(self.disk_name)
        self._king.execute_script(LuksClose(diskpath, sudopasswd))
        return not self.is_decrypted()

    def is_mounted(self):
        """function is_mounted

        returns
        """
        if not self._king.is_active():
            return False
        self._connect_king()
        return self._king.test_command(
            'test -d {}'.format(self.archive_path)) == 0

    def mount(self, ):
        """function mount

        returns
        """
        self._connect_king()
        diskpath = PathHandler('/dev/mapper').join(self.disk_name)
        mount = MountScript(diskpath, '/data')
        self._king.execute_script(mount)
        return self.is_mounted()

    def umount(self, password):
        r"""SUMMARY

        umount(sudopasswd)

        @Arguments:
        - `sudopasswd`:

        @Return:

        @Error:
        """
        self._connect_king()
        umount = UmountScript('/data', password)
        self._king.execute_script(umount)
        return not self.is_mounted()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _disk.py ends here
