#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""\
Name: backup_ni_local.py
"""
import os
import sys
import logging
import pwd

import pshandler
from RsyncBackup import LinkDestLocalBackup
from logging.handlers import RotatingFileHandler
from runlevel import RunLevel

__version__ = '0.1.1'


## Define Variables
###############################################################################
# define backup directory name
BACKUP_NAME = 'queen_local'
BACKUP_BASE_DIR = '/backup'
BACKUP_PATH = os.path.join(BACKUP_BASE_DIR, BACKUP_NAME)
# define Max incremental backup
MAX = 30
###############################################################################


###############################################################################
# output log file
LOGNAME = 'backup_qu_local.log'
LOGDIR = '/var/log'
LOGPATH = os.path.join(LOGDIR, LOGNAME)
_RH = RotatingFileHandler(LOGPATH, 'a', 1024*50, 3)
_RH.setLevel(logging.INFO)
_RH.setFormatter(logging.Formatter(
    '%(asctime)s;%(name)s;%(module)s %(funcName)s(%(lineno)d);%(levelname)s;'
    '\n   %(message)s'))

# console
_CH = logging.StreamHandler()
_CH.setLevel(logging.ERROR)

LOG = logging.getLogger('backup_qu_local')
LOG.setLevel(logging.INFO)
LOG.addHandler(_RH)
LOG.addHandler(_CH)

# exception
def logging_handle_exceptions(excls, value, trcbck):
    r"""Handling exception hook.

    sys.excepthook = logging_handle_exceptions
    """
    import traceback
    if issubclass(excls, KeyboardInterrupt):
        sys.__excepthook__(excls, value, trcbck)
        return
    errortype = 'Error type: {}'.format(excls)
    valuetxt = 'Uncaught exception: {0}'.format(str(value))
    trcbcktxt = ''.join(traceback.format_tb(trcbck))
    LOG.exception('\n'.join([errortype, valuetxt, trcbcktxt]))

sys.excepthook = logging_handle_exceptions
###############################################################################


## Start Backup message
#
LOG.info('{0:*^30}'.format('Started Ni Local Backup'))


for ps in pshandler.list_process():
    if 'sshfs' == ps.get_name() and '/data' in ps.get_cmdline():
        LOG.error('Failed: sshfs mounting /data')
        sys.exit(1)

# if not os.path.exists(BACKUP_PATH):
#     LOG.warning('Warnings: Not exists {0}. Will create'.format(BACKUP_PATH))
#     os.mkdir(BACKUP_PATH)

## Main
#
LOG.info('Execute Backup.')
BK = LinkDestLocalBackup(src='/', bkupdir=BACKUP_PATH,
                         lotate=True, logname=LOGNAME)
EXCLUDES = ['/data/*',
            '/cdata',
            '/backup/*',
            '/etc/fstab',
            '/etc/crypttab',
            '/var/cache/apt/archive/*',
            '/home/*/.mozilla/firefox/*.default/Cache/*',
            '/home/*/.cache/google-chrome/Default/*',
            '/root/.mozilla/firefox/*.default/Cache/*',
            '/root/.cache/google-chrome/Default/*',
            '/root/.local/share/Trash/files/*',
            '/root/.local/share/Trash/info/*',
            '/root/work/*',
            '/root/Downloads/*',
            '/root/VIDEO/*',
            '/usr/src/*',
            '/mnt/*',
            '/media/*',
            ]
BK.add_exclude(EXCLUDES)
BK.backup()

sys.exit(0)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# backup_ni_local.py ends here
