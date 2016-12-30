#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""backup_bi_remote -- DESCRIPTION

"""
# for debug
# import cgitb
# cgitb.enable(format='text')

import argparse
import os
import sys
import logging
import subprocess as sbp
import shutil

from RsyncBackup import LinkDestRemoteBackup
import DiskUsage

__version__ = '0.1.0'

# TODO: (Atami) [2015/09/21]

###############################################################################
## PREVENT
#
# check platform
if 'nt' == os.name:
    sys.exit('Not support WindowsNT.')

# check root
if not os.geteuid() == 0:
    sys.exit('Script must be run as root.')


###############################################################################
## PREDEFINE
#
# define log file name
log_name = 'backup_bi.log'
log_base_dir = '/var/log'
log_path = os.path.join(log_base_dir, log_name)
logging.basicConfig(filename=log_path, level=logging.DEBUG, filemode='a',
                    format='%(asctime)s %(message)s')

# define backup directory name
backup_base_dir = '/data/.backup'
backup_name = 'bishop_remote'
backup_path = os.path.join(backup_base_dir, backup_name)

# define Max incremental backup
MAX = 30

# define message
MSG = {'start': '{0:*^30}'.format('Started Remote Backup'),
       'kidead': 'Failed: king server not active.',
       'notdecrypted': 'Failed: not decrypted disk on king server.',
       'err_runlevel': 'Runlevel Errors:'
       ' Could not execute this script on this runnlevel.\n{} revel only',
       }

CLEANLIST = ['/root/.local/share/Trash/',
             '/data/.Trash-0/',
             '/media/Data/.Trash-0/']

BACKUP_EXCLUDES = ['/data/*',
                   '/cdata',
                   '/backup/*',
                   '/var/cache/apt/archive/*',
                   '/home/*/.mozilla/firefox/*.default/Cache/*',
                   '/home/*/.cache/google-chrome/Default/*',
                   '/root/.mozilla/firefox/*.default/Cache/*',
                   '/root/.cache/google-chrome/Default/*',
                   '/root/.local/share/Trash/files/*',
                   '/root/.local/share/Trash/info/*',
                   '/root/homedata',
                   '/root/work/*',
                   '/root/Downloads/*',
                   '/root/VIDEO/*',
                   '/usr/src/*',
                   ]

RESTORE_EXCLUDES = ['/data/*',
                    '/cdata',
                    '/backup/*',
                    '/var/cache/apt/archive/*',
                    '/home/*/.mozilla/firefox/*.default/Cache/*',
                    '/home/*/.cache/google-chrome/Default/*',
                    '/root/.mozilla/firefox/*.default/Cache/*',
                    '/root/.cache/google-chrome/Default/*',
                    '/root/.local/share/Trash/files/*',
                    '/root/.local/share/Trash/info/*',
                    '/etc/fstab',
                    '/etc/crypttab',
                    '/root/homedata',
                    '/root/work/*',
                    '/root/Downloads/*',
                    '/root/VIDEO/*',
                    '/usr/src/*',
                    ]

###############################################################################
## Functions
#
## clean up
#
def cleanup():
    """SUMMARY

    @Return:
    """
    exists, rmtree = os.path.exists, shutil.rmtree
    for dir_ in CLEANLIST:
        if exists(dir_):
            rmtree(dir_)

## check backup dir or decrypt disk
#
def pave_king():
    """SUMMARY

    @Return:
    """
    sbp.check_call(('wol', '--silent'))
    # with king.King() as ki:
    #     ki.wol()
    #     ki.pavedisk()
    #     if not ki.isactive():
    #         logging.log(10, MSG.get('kidead'))
    #         sys.exit(MSG.get('kidead'))
    #     if not ki.ismount():
    #         logging.log(10, MSG.get('notdecrypted'))
    #         sys.exit(MSG.get('notdecrypted'))

## check disk usage
#
def disk_usage(path):
    """SUMMARY

    @Return:
    """
    usage = DiskUsage.disk_usage(path)
    msg = ('total: {0}, free: {1}, used: {2}'
          .format(DiskUsage.bytes2human(usage.total),
                  DiskUsage.bytes2human(usage.free),
                  DiskUsage.bytes2human(usage.used)))
    print(msg)
    logging.log(10, msg)

## backup
#
def backup():
    """SUMMARY

    @Return:
    """

    ## Start Backup message
    print(MSG.get('start'))
    logging.log(10, MSG.get('start'))
    cleanup()
    pave_king()
    bk = LinkDestRemoteBackup(src='/', bkupdir=backup_path,
                              rname='ki', logname=log_name)
    bk.add_exclude(BACKUP_EXCLUDES)
    bk.add_opt(['--rsync-path="sudo rsync"', '-z'])
    bk.backup()
    disk_usage(bk._mntpoint)

## restore
#
def restore():
    """SUMMARY

    @Return:
    """
    pave_king()
    bk = LinkDestRemoteBackup(src='/', bkupdir=backup_path,
                              rname='ki', logname=log_name)
    bk.add_exclude(RESTORE_EXCLUDES)
    bk.add_opt(['--rsync-path="sudo rsync"', '-z'])
    bk.restore()
    sbp.check_call(['/usr/sbin/update-initramfs', '-u'])
    sbp.check_call(['/usr/sbin/update-grub2'])

def getoptions():
    """Option function."""
    parser = argparse.ArgumentParser(description="""Backup bishop""")
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

    parser.add_argument('-b', '--backup',
                        dest='backup',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Do backup')

    parser.add_argument('-r', '--restore',
                        dest='restore',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Do restore')

    # (yas/expand-link "argparse_add_argument" t)
    return parser.parse_args()

def _main():
    """SUMMARY

    @Return:
    """
    opt = getoptions()

    if opt.backup:
        backup()
        return
    elif opt.restore:
        restore()
        return
    else:
        backup()

if __name__ == '__main__':
    _main()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# backup_bi_remote.py ends here
