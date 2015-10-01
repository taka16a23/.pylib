#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: backup_ki_pull.py
"""


import os
import argparse
import logging
# import king
import sys
from RsyncBackup import LinkDestLocalBackup
import subprocess as sbp

# for debug
import cgitb
cgitb.enable(format='text')


__version__ = '0.1.0'


log_name = 'backup_king.log'
log_base_dir = '/var/log'
log_path = os.path.join(log_base_dir, log_name)
logging.basicConfig(filename=log_path, level=logging.DEBUG, filemode='w',
                    format='%(asctime)s %(message)s')

# define backup directory name
backup_base_dir = '/data/.backup'
backup_name = 'king_remote'
backup_path = os.path.join(backup_base_dir, backup_name)


BACKUP_EXCLUDES = ['/data/*',
                   '/var/cache/apt/archive/*',
                   ]

# define message
MSG = {'start': '{0:*^30}'.format('Started Remote Backup'),
       'kidead': 'Failed: king server not active.',
       'notdecrypted': 'Failed: not decrypted disk on king server.',
       'err_runlevel': 'Runlevel Errors: Could not execute this script on this runnlevel.\n{} revel only',
       }

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


def backup():
    r"""SUMMARY

    @Return:
    """
    pave_king()
    bk = LinkDestLocalBackup(src='ki:/', bkupdir=backup_path, lotate=True,
                             logname=log_name)
    bk.add_exclude(BACKUP_EXCLUDES)
    bk.add_opt(['--rsync-path="sudo rsync"', '-z'])
    bk.backup()


def _predef_options():
    parser = argparse.ArgumentParser(description=""" """)
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
    backup()

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# backup_ki_pull.py ends here
