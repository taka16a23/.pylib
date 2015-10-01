#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$
""" env -- Setting environment for windows

$Revision$

"""


__revision__ = "$Revision$"
__version__ = "0.1.0"

import sys
import os as _os

import win32con
from win32gui import SendMessage

from _winreg import (
    CloseKey, OpenKey, DeleteValue, QueryValueEx, SetValueEx,
    HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE,
    KEY_ALL_ACCESS, KEY_READ, REG_SZ, REG_EXPAND_SZ
    )

if sys.version_info < (2, 4):
    from sets import Set as set

__all__ = ['env_keys', 'update_env', 'get_env', 'set_env', 'del_env',
           'remove', 'unique', 'prepend_env', 'prepend_env_pathext',
           'chg_drive']


def env_keys(user=True):
    # if user:
    #     root = HKEY_CURRENT_USER
    #     subkey = 'Environment'
    # else:
    #     root = HKEY_LOCAL_MACHINE
    #     subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    # return root, subkey
    return (user and
            (HKEY_CURRENT_USER, 'Environment') or
            (HKEY_LOCAL_MACHINE,
             r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'))


def update_env():
    """Update Environment."""
    SendMessage(
        win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')


def get_env(name, user=True):
    root, subkey = env_keys(user)
    key = OpenKey(root, subkey, 0, KEY_READ)
    try:
        value, _ = QueryValueEx(key, name)
    except WindowsError:
        return ''
    return value


def set_env(name, value, REG=REG_SZ, update=False):
    key = OpenKey(HKEY_CURRENT_USER, 'Environment', 0, KEY_ALL_ACCESS)
    SetValueEx(key, name, 0, REG, value)
    CloseKey(key)
    if update:
        update_env()


def del_env(name, update=False):
    if get_env(name) is '':
        return False
    key = OpenKey(HKEY_CURRENT_USER, 'Environment', 0, KEY_ALL_ACCESS)
    DeleteValue(key, name)
    CloseKey(key)
    if update:
        update_env()
    return True


def remove(paths, value):
    while value in paths:
        paths.remove(value)


def unique(paths):
    # unique = []
    # for value in paths:
        # if value not in unique:
            # unique.append(value)
    return list(set([value for value in paths]))
    # return unique


def prepend_env(name, values):
    for value in values:
        paths = get_env(name).split(';')
        remove(paths, '')
        paths = unique(paths)
        remove(paths, value)
        paths.insert(0, value)
        set_env(name, ';'.join(paths))


def prepend_env_pathext(values):
    prepend_env('PathExt_User', values)
    pathext = ';'.join([
        get_env('PathExt_User'),
        get_env('PathExt', user=False)
    ])
    set_env('PathExt', pathext)


def chg_drive(drive, name, value):
    join = _os.path.join
    newenv = []
    for item in get_env(name).split(';'):
        # if value in item:
        #     newenv.append(_os.path.join(drive, value))
        # else:
        #     newenv.append(item)
        newenv += (value in item and join(drive, value) or item)
    set_env(name, ';'.join(newenv))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# env.py ends here
