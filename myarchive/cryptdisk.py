#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""cryptdisk -- DESCRIPTION

"""
import os
import subprocess as sbp
import pexpect
from pathhandler import PathHandler


class DecryptDisk(object):
    r"""CryptDisk

    DecryptDisk is a object.
    Responsibility:
    """
    def __init__(self, disk, mapped_name):
        r"""

        @Arguments:
        - `uuid`:
        - `name`:
        """
        self._disk = disk
        self._mapped_name = mapped_name

    def get_disk(self, ):
        r"""SUMMARY

        get_uuid()

        @Return:

        @Error:
        """
        return self._disk

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._mapped_name

    def set_name(self, name):
        r"""SUMMARY

        set_name(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        self._mapped_name = name

    def mapper_path(self, ):
        r"""SUMMARY

        mapper_path()

        @Return:

        @Error:
        """
        # PathHandler('/dev/mapper').join(self.get_name())
        return os.path.join('/dev/mapper', self.get_name())

    def isexists(self, ):
        r"""SUMMARY

        isdecrypted()

        @Return:

        @Error:
        """
        return os.path.exists(self.mapper_path())

    def decrypt(self, password):
        r"""SUMMARY

        decrypt(password)

        @Arguments:
        - `password`:

        @Return:

        @Error:
        """
        if self.isexists():
            raise StandardError('Device already exists')

        pex = pexpect.spawn(
            'cryptsetup open {} {}'.format(self._disk, self._mapped_name),
            maxread=4000)
        pex.sendline(password)
        ret = pex.expect(['No key available with this passphrase.', r'[#\$]',
                          'already exists', pexpect.EOF])
        if ret in (1, 2, 3):
            return True
        if ret == 0:
            return False
        raise StandardError()

    def close(self, ):
        r"""SUMMARY

        close()

        @Return:

        @Error:
        """
        ret = sbp.call(('cryptsetup', 'close', self.get_name()))
        if 0 == ret:
            return True
        return False



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cryptdisk.py ends here
