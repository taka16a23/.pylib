#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: backup_ki_local.py 485 2015-09-29 03:10:26Z t1 $
# $Revision: 485 $
# $Date: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $

"""\
Name: backup_ki_local.py
"""

# for debug
# import cgitb
# cgitb.enable(format='text')

import sys
sys.path.append('/root/.pylib')

import argparse
import os
import logging
from time import sleep

import DiskUsage
from RsyncBackup import LinkDestLocalBackup

__revision__ = '$Revision: 485 $'
__version__ = '0.1.0'

## Define Variables
#
# define log file name
log_name = 'backup_ki.log'
log_base_dir = '/var/log'
log_path = os.path.join(log_base_dir, log_name)
logging.basicConfig(filename=log_path, level=logging.DEBUG, filemode='a',
                    format='%(asctime)s %(message)s')

# define backup directory name
backup_name = 'king_local'
backup_base_dir = '/data/.backup'
backup_path = os.path.join(backup_base_dir, backup_name)

# define Max incremental backup
MAX = 30

MSG = {'start': '{0:*^30}'.format('Started Local Backup'),
       'nodecrypt': 'Failed: Not decrypted /dev/mapper/data. Will Exit.',
       'notmounted': 'Failed: Not mounted {0}'.format(backup_base_dir),
       'nobkuppath': 'Warnings: Not exists {0}. Will create'.format(backup_path),
       'sshfs_mounting': 'Failed: sshfs mounting /data',
       }


## Main
#
def dobackup():
    """SUMMARY

    @Return:
    """
    bk = LinkDestLocalBackup(src='/', bkupdir=backup_path,
                             lotate=True, logname=log_path)
    excludes = ['/backup',
                '/share/*',
                '/data/*',
                '/lost+found',
                '/sys/*',
                '/dev/*',
                '/media/*',
                '/proc/*',
                '/tmp/*',
                '/run/*',
                '/mnt',
                '/lib/udev/devices/console',
                '/lib/udev/devices/loop0',
                '/lib/udev/devices/null',
                '/lib/udev/devices/ppp',
                '/lib/udev/devices/net/tun',
                '/etc/fstab',
                '/etc/crypttab',
                '/var/run/*',
                '/var/lock/*',
                '/lib/modules/*/volatile/.mounted',
                '/var/cache/apt/archive/*',
                '/home/*/.mozilla/firefox/*.default/Cache/*',
                '/home/*/.cache/google-chrome/Default/*',
                '/root/.mozilla/firefox/*.default/Cache/*',
                '/root/.cache/google-chrome/Default/*',]

    bk.add_exclude(excludes)
    bk.backup()
    print_disk_usage(bk.bkupdir)


## check disk usage
#
def print_disk_usage(dir_):
    """SUMMARY

    @Return:
    """
    usage = DiskUsage.disk_usage(dir_)
    ms = 'total: {0}, free: {1}, used: {2}'.format(
        DiskUsage.bytes2human(usage.total),
        DiskUsage.bytes2human(usage.free),
        DiskUsage.bytes2human(usage.used))
    print(ms)
    logging.log(10, ms)

def _predef_options():
    parser = argparse.ArgumentParser(description="""Backup king server.""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')
    parser.add_argument('-f', '--force',
                        dest='force',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Force Backup.')
    parser.add_argument('-d', '--debug',
                        dest='debug',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Run as debug mode.')
    # (yas/expand-link "argparse_add_argument" t)
    return parser


def _main():
    parser = _predef_options()
    opts = parser.parse_args()
    # parser.print_usage()
    # check platform
    if 'nt' == os.name:
        sys.exit('Not support WindowsNT.')
    # check root
    if not 0 == os.geteuid():
        sys.exit('Script must be run as root.')
    # wait decrypt
    # if not opts.debug:
        # sleep(600)

    # Start Backup message
    print(MSG.get('start'))
    logging.log(10, MSG.get('start'))

    # check disk exists
    # if not os.path.exists('/dev/mapper/data_crypt'):
    #     logging.log(10, MSG.get('nodecrypt'))
    #     sys.exit(MSG.get('nodecrypt'))

    if not os.path.exists(backup_base_dir):
        logging.log(10, MSG.get('notmounted'))
        sys.exit(MSG.get('notmounted'))

    if not os.path.exists(backup_path):
        logging.log(10, MSG.get('nobkuppath'))
        print(MSG.get('nobkuppath'))
        os.mkdir(backup_path)
    dobackup()



if __name__ == '__main__':
    _main()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# backup_ki_local.py ends here
