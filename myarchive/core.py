#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""core -- DESCRIPTION

"""
from time import sleep
import os

from sh import mount, umount
from pathhandler import PathHandler
from counter import Counter

from . import cryptdisk
from myarchive import inputpass


class PasswordError(StandardError):
    r"""SUMMARY
    """


class MyArchive(object):
    r"""MyArchive

    MyArchive is a object.
    Responsibility:
    """
    disk = cryptdisk.DecryptDisk(
        '/dev/disk/by-uuid/9016a4ca-f21a-4591-bc24-447ec4989340', 'data')
    directory = PathHandler('/data')

    def __init__(self, passinputer=None):
        r"""

        @Arguments:
        - `passinputer`:
        """
        self._passinputer = passinputer or inputpass.CmdlineInputPass()

    def set_passinputer(self, passinputer):
        r"""SUMMARY

        set_passinputer(passinputer)

        @Arguments:
        - `passinputer`:

        @Return:

        @Error:
        """
        if not isinstance(passinputer, inputpass.InputPass):
            # TODO: (Atami) [2014/11/25]
            raise TypeError()
        self._passinputer = passinputer

    def getpath(self, ):
        r"""SUMMARY

        getpath()

        @Return:

        @Error:
        """
        return self.directory.join('archive')

    def isexists(self, ):
        r"""SUMMARY

        isexists()

        @Return:

        @Error:
        """
        return os.path.exists(self.getpath())

    def _getpassword(self, ):
        r"""SUMMARY

        getpassword()

        @Return:

        @Error:
        """
        self._passinputer.set_prompt(
            'Enter passphrase for {0}: '.format(self.disk.get_disk()))
        return self._passinputer.input()

    def ismounted(self, ):
        r"""SUMMARY

        ismounted()

        @Return:

        @Error:
        """
        allmounts = mount()
        line = '{} on {}'.format(self.disk.mapper_path(), self.directory)
        return line in allmounts

    def _decrypt(self, times=4):
        r"""SUMMARY

        _decrypt()

        @Return:

        @Error:
        """
        count = Counter(times, exceptclass=PasswordError)
        while not self.disk.isexists():
            count() # raise error if times called
            self.disk.decrypt(self._getpassword())
            sleep(2)

    def mount(self, ):
        r"""SUMMARY

        mount()

        @Return:

        @Error:
        """
        if self.ismounted():
            return
        if self.directory.isfile():
            raise StandardError('already exists file')
        # create directory if not exists
        if not self.directory.exists():
            self.directory.mkdir()
        # decrypt
        self._decrypt()
        mount(self.disk.mapper_path(), self.directory)

    def umount(self, ):
        r"""SUMMARY

        umount()

        @Return:

        @Error:
        """
        umount(self.directory)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# core.py ends here
