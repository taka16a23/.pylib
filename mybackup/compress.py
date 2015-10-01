#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
$Revision: 441 $
$LastChangedRevision: 441 $
$LastChangedDate: 2015-08-07 10:25:43 +0900 (Fri, 07 Aug 2015) $

compress.py

backup windows files or folder
"""

import sys
import os

from portable import DRIVE
from time import strftime
import tempfile

class SevenBackup:
    """
    """

    def __init__(self):
        """

        Arguments:
        - `passwd`: compress password
        """
        self.sevenzpath = DRIVE + "\\Office\\7-ZipPortable\\App\\7-Zip\\7z.exe"
        self.passwd = " -p"
        self.name = None
        self.date = None
        self.dir = tempfile.gettempdir()
        self.exclude = ""
        self.compressedname = None
        self.cmd = ""

    def sevenbackup(self, path):
        """
        Set path sevenz bin

        """
        self.sevenzpath = path


    def compress2exe(self, target, name, passwd):
        """compress to exe archive like example.exe

        Arguments:
        - `target`:
        """
        if not os.path.exists(self.sevenzpath):
            print "Not detect " + self.sevenpath
            sys.exit(1)
        self.name = name
        self.passwd += '"'+ passwd +'"'
        self.compressedname = self.dir + self.name + self.date + ".exe "
        self.cmd = self.sevenzpath + ' a ' + '-sfx ' + self.compressedname +\
            target + self.passwd + self.exclude

        if os.path.exists(self.compressedname):
            os.remove(self.compressedname)

        print self.cmd
        try:
            os.system(self.cmd)
        except:
            sys.exit(1)

    def changepasswd(self, passwd=''):
        """
        change passwd
        get password if not set it


        Arguments:
        - `passwd`:
        """

        if not passwd:
            from getpasswd import confirm_passwd
            self.passwd = confirm_passwd()
        else:
            self.passwd = passwd

    def setdate(self, strf):
        """
        Set date string for compless name.

        """
        self.date = strftime(strf)

    def zexclude(self, exclude):
        self.exclude += ' -xr!'+exclude
