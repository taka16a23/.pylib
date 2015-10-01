#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
mybackup.py


"""

import sys
import os
import compress
import tempfile

from time import sleep
from optparse import OptionParser
from getpasswd import confirm_passwd
from winutils import find_process
from portable import DRIVE
from pywinauto import application

import king

prog_name = sys.argv[0]
PASSWD = None
TMPDIR = tempfile.gettempdir()

def ParserSetup():
    """Get options


    """
    usage = 'Usage: ' + prog_name + '-t <target> -n <compressed name> [options]'
    parser = OptionParser(usage)

    parser.add_option(
        "-t", "--target",
        action="store",
        type="string",
        dest="target",
        help="Target of compress. Set full path file or directory."
    )
    parser.add_option(
        "-z", "--sevenzip-path",
        action="store",
        type="string",
        dest="sevenz",
        help="Set and Change default 7z.exe path."
    )
    parser.add_option(
        "-n", "--name",
        action="store",
        type="string",
        dest="name",
        help="Set complessed name"
    )
    parser.add_option(
        "-d", "--date",
        action="store",
        type="string",
        dest="datestr",
        default="",
        help="Set date string to extention complessed name. ex. %Y%m%d"
    )
    parser.add_option(
        "-p", "--password",
        action="store",
        type="string",
        dest="passwd",
        help="Set password"
    )
    parser.add_option(
        "--chrome",
        action="store_true",
        default=False,
        dest="chrome",
        help='Backup chrome "default" directory'
    )
    parser.add_option(
        "--outlook",
        action="store_true",
        default=False,
        dest="outlook",
        help="Backup outlook directory that contain .pst"
    )
    parser.add_option(
        "--rss",
        action="store_true",
        default=False,
        dest="rss",
        help="Backup RSS headlinereader.dat"
    )
    parser.add_option(
        "--atok", "--ATOK",
        action="store_true",
        default=False,
        dest="atok",
        help="ATOK backup")
    return parser

def waitclose(process, name):
    """Wait close program.

    Arguments:
    - `process`: Set exe name. "example.exe"
    - `name`: Set string. This will show in prompt.
    """
    while find_process(process):
        sys.stdout.write("\rClose %s" % name)
        sys.stdout.flush()
        sleep(5)

class CHROMEBACKUP():
    """Chrome Browser Backup.

    Compress Default folder.
    """
    def __init__(self):
        self.name = 'chrome'
        self.process_name = 'chrome.exe'
        self.backup_target = (
            '"C:\\Documents and Settings\\qua\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\Default"')
        self.compressedname = None

    def compress(self):
        """Compress to 7z excutable '.exe' extension.

        """
        waitclose(self.process_name, self.name)
        b = compress.SevenBackup()
        b.setdate("_%Y_%m_%d")
        b.zexclude('"Default\\Cache\\*"')
        b.zexclude('"Default\\Media Cache\\*"')
        b.compress2exe(self.backup_target, self.name, PASSWD)
        self.compressedname = b.compressedname

    def upload(self, ssh):
        """
        """
        targetdir = '/data/archive/windows/appdata/chrome/'
        source = self.compressedname
        target = os.path.join(targetdir, os.path.basename(source))
        print source +" => "+ target
        ssh.upload(source, target)

class OUTLOOKBACKUP():
    """Outlook folder Backup.
    """

    def __init__(self):
        """
        """
        self.name = "OUTLOOK"
        self.process_name = "OUTLOOK.exe"
        self.backup_target = (
            '"C:\\Documents and Settings\\qua\\Local Settings\\Application Data\\Microsoft\\Outlook\\"')
        self.compressedname = None

    def compress(self):
        """Compress to 7z excutable '.exe' extension.

        """
        waitclose(self.process_name, self.name)
        b = compress.SevenBackup()
        b.setdate("_%Y_%m_%d")
        b.compress2exe(self.backup_target, self.name, PASSWD)
        self.compressedname = b.compressedname

    def upload(self, ssh):
        """
        """
        targetdir = '/data/archive/windows/appdata/outlook/'
        source = self.compressedname
        target = os.path.join(targetdir, os.path.basename(source))
        print source +" => "+ target
        ssh.upload(source, target)

class RSSBACKUP():
    """Backup RSS headlinereader.dat
    """

    def __init__(self):
        """

        Arguments:
        - `headlinereader_dat`:
        """
        self.name = "RSS"
        self.window_name = "sleipnir"
        self.process_name = "sleipnir.exe"
        self.backup_target = (
            '"'+ DRIVE + '\\Internet\\Sleipnir\\settings\\All Users\\headlinereader\\headlinereader.dat' +'"')
        self.compressedname = None

    def compress(self):
        """
        """
        waitclose(self.process_name, self.window_name)
        b = compress.SevenBackup()
        b.setdate("_%Y_%m_%d")
        b.compress2exe(self.backup_target, self.name, PASSWD)
        self.compressedname = b.compressedname

    def upload(self, ssh):
        """
        """
        targetdir = '/data/archive/rss/'
        source = self.compressedname
        target = os.path.join(targetdir, os.path.basename(source))
        print source +" => "+ target
        ssh.upload(source, target)

class ATOKBACKUP(object):
    """
    """
    def __init__(self):
        """
        """
        self.name = "ATOK"
        self.backup_target = TMPDIR + "\\ATOK_backupdat"
        self.backup_execute = "C:\\Program Files\\JustSystems\\ATOK22\\ATOK22BU.EXE"
        self.window_name = u"ATOK バックアップツール"
        self.pre_backuped_file = TMPDIR + '\\ATOK_backuptmp\\BACKUP.DAT'
        self.compressedname = None

    def compress(self):
        """
        """
        self.pre_backup()
        b = compress.SevenBackup()
        b.setdate("_%Y_%m_%d")
        b.compress2exe(self.backup_target, self.name, PASSWD)
        self.compressedname = b.compressedname

    def pre_backup(self):
        """ATOK backup tools execute.


        """
        if os.path.exists(self.pre_backuped_file):
            os.removedirs(os.path.dirname(self.pre_backuped_file))
        app = application.Application.start(self.backup_execute)
        app.Dialog.Edit1.SetEditText(TMPDIR) # ATOKBACKUP
        app.Dialog[u'実行'].Click()
        app.Dialog1[u'はい'].Click()
        while not os.path.exists(self.pre_backuped_file):
            sleep(10)
        sleep(10)

        app.Dialog3[u'閉じる'].Click()
        try:
            app.Dialog3[u'閉じる'].Click()
        except:
            pass
        app.Dialog3[u'終了'].Click()
        sleep(1) # wait rename ATOK_backuptmp => ATOK_backupdat

    def upload(self, ssh):
        """
        """
        sleep(5)
        targetdir = '/data/archive/windows/appdata/ATOK/'
        source = self.compressedname
        target = os.path.join(targetdir, os.path.basename(source))
        print source +" => "+ target
        ssh.upload(source, target)

def main():
    """Main


    """
    global PASSWD
    parser = ParserSetup()
    (options, args) = parser.parse_args()
    PASSWD = (options.passwd or confirm_passwd('Compress Password: ', 1))
    ki = king.King()
    ki.wakeup()
    ki.pavedisk()

    backuplist = []
    if options.chrome:
        backuplist.append(CHROMEBACKUP)
    if options.outlook:
        backuplist.append(OUTLOOKBACKUP)
    if options.rss:
        backuplist.append(RSSBACKUP)
    if options.atok:
        backuplist.append(ATOKBACKUP)

    if not backuplist:
        parser.parse_args()
    for i in range(len(backuplist)):
        backup = backuplist[i]()
        backup.compress()
        backup.upload(ki)

    del PASSWD
    sys.exit(0)



if __name__ == '__main__':
    main()
