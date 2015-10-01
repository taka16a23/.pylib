#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: data.py 468 2015-08-19 05:49:01Z t1 $
# $Revision: 468 $
# $Date: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $

r"""mydata -- DESCRIPTION

"""
from pathhandler import PathHandler
from sh import mount, umount

from counter import Counter

from . import abstract
from . import cryptdisk
from . import inputpass


class PasswordError(StandardError):
    r"""SUMMARY
    """


class MyData(abstract.MyPath):
    r"""MyData

    MyData is a object.
    Responsibility:
    """
    disk = cryptdisk.DecryptDisk(
        '/dev/disk/by-uuid/9016a4ca-f21a-4591-bc24-447ec4989340', 'data')

    def __init__(self, passinputer=None):
        r"""

        @Arguments:
        - `passinputer`:
        """
        self._passinputer = passinputer or inputpass.CmdlineInputPass()

    def isexists(self, ):
        r"""SUMMARY

        isexists()

        @Return:

        @Error:
        """
        allmounts = mount()
        return ('{} on {}'.format(self.disk.mapper_path(), self.get_path())
                in allmounts)

    def get_path(self, ):
        r"""SUMMARY

        getpath()

        @Return:

        @Error:
        """
        return PathHandler('/data')

    def mkdir(self, ):
        r"""SUMMARY

        mkdir()

        @Return:

        @Error:
        """
        self.get_path().mkdir()

    def _getpassword(self, ):
        r"""SUMMARY

        getpassword()

        @Return:

        @Error:
        """
        self._passinputer.set_prompt(
            'Enter passphrase for {0}: '.format(self.disk.get_disk()))
        return self._passinputer.input()

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

    def mount(self, ):
        r"""SUMMARY

        mount()

        @Return:

        @Error:
        """
        mount(self.disk.mapper_path(), self.get_path())

    def umount(self, ):
        r"""SUMMARY

        umount()

        @Return:

        @Error:
        """
        umount(self.get_path())

    def pave(self, force=False):
        r"""SUMMARY

        pave()

        @Return:

        @Error:
        """
        if self.isexists() and force is False:
            return True
        if not self.get_path().exists():
            self.mkdir()
        self._decrypt()
        self.mount()

    def __str__(self):
        return self.get_path()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mydata.py ends here
