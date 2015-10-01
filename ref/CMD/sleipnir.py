#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: sleipnir.py 439 2015-08-07 01:25:08Z t1 $
# $Revision: 439 $
# $Date: 2015-08-07 10:25:08 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 10:25:08 +0900 (Fri, 07 Aug 2015) $
""" sleipnir -- for sleipnir's informations.

$Revision: 439 $

2014/05/14 Added: functions "destroy_sleipnir_feedback_dialog",
        "wait_kill_sleipnir_feedback", "wait_close_sleipnir_update_dialog",
        "wait_sleipnir_window", "move_sleipnir", "click_sleipnir_refresh",
"


"""
import os as _os
import subprocess as _sbp
from time import sleep

from ref import CMD
import xcb2
import sendkeys
from xcb2.xobj import WindowDialogType
from junk.mypsutil import psexists as _psexists
import wm

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 439 $'
__version__ = '0.1.1'


NAME = 'sleipnir'
BIN = 'Sleipnir.exe'
BINPATH = '/opt/portable-sleipnir-299/PortableSleipnir/PortableSleipnir.exe'
LAUNCHER = '/root/.zsh/scripts/sleipnir'
PORTABLE_HEADLINEREADER_PATH = ('/media/portable/Internet/sleipnir'
                                '/users/qua/setting/modules/')
LOCAL_HEADLINEREADER_PATH = ('/opt/portable-sleipnir-299/PortableSleipnir'
                             '/settings/"All Users"/headlinereader')


def push_sync_headlinereader():
    """SUMMARY

    @Return:
    """

    if not _os.path.exists(PORTABLE_HEADLINEREADER_PATH):
        print('Does not exists {}'.format(PORTABLE_HEADLINEREADER_PATH))
        return
    if _psexists(BIN):
        print('{} exists'.format(BIN))
        return
    cmd = CMD.get('rsync') + ' -av --delete --force {0} {1}'.format(
        LOCAL_HEADLINEREADER_PATH, LOCAL_HEADLINEREADER_PATH)
    print(cmd)
    _os.system(cmd)


def killdialog():
    r"""SUMMARY

    @Return:
    """
    def spnir_dialog_confirm(win, **args):
        r"""SUMMARY

        @Arguments:
        - `win`:

        @Return:
        """
        return ('Sleipnir' == win.title and 'Dialog' == win.type)

    if wm.exists(confirm=spnir_dialog_confirm):
        win = wm.getwin(confirm=spnir_dialog_confirm)
        win.close()


def run():
    r"""SUMMARY

    @Return:
    """
    if not _psexists(BIN):
        _sbp.Popen((LAUNCHER))


def runmove():
    r"""SUMMARY

    @Return:
    """
    run()
    if wm.WinWait(sec=180).win(title='Sleipnir'):
        win = wm.getwin(title='Sleipnir')
    if win.ismaximize():
        win.reset_maximize()
    win.move(x=1280, y=0)
    win.maximize()
    killdialog()


def destroy_sleipnir_feedback_dialog():
    r"""SUMMARY

    destroy_sleipnir_feedback_dialog()

    @Return:
    """
    print('try close feedback dialog')
    con = xcb2.connect()
    win = con.root.client_list().filter_wmclass('FeedbackAgent.exe')[0]
    sendkeys.SendKeys('{LClick 10 10}').sendkeys(win)
    con.flush()
    sendkeys.SendKeys('!b').sendkeys(win)


def wait_kill_sleipnir_feedback():
    r"""SUMMARY

    wait_sleipnir_window()

    @Return:
    """
    print('** wait sleipnir window or destroy feedback dialog')
    con = xcb2.connect()
    for _ in range(60):
        sleep(1)
        winlis = con.root.client_list().to_types()
        if winlis.filter_wmclass('Sleipnir.exe'):
            return
        if winlis.filter_wmclass('FeedbackAgent.exe'):
            destroy_sleipnir_feedback_dialog()
    raise StandardError()


def wait_close_sleipnir_update_dialog():
    r"""SUMMARY

    wait_sleipnir_update_dialog()

    @Return:
    """
    print('Wait Dialog Window.')
    con = xcb2.connect()
    for _ in range(10):
        sleep(1)
        winlis = con.root.client_list().to_types().filter_wmclass(
            'Sleipnir.exe')
        if winlis <= 1:
            continue
        for win in winlis:
            if isinstance(win, WindowDialogType):
                win.close()
                return


def wait_sleipnir_window():
    r"""SUMMARY

    wait_sleipnir_window()

    @Return:
    """
    print('* Wait for sleipnir window')
    wait_kill_sleipnir_feedback()
    wait_close_sleipnir_update_dialog()


def move_sleipnir():
    r"""SUMMARY

    move_sleipnir()

    @Return:
    """
    print('Move Sleipnir window.')
    con = xcb2.connect()
    winlis = con.root.client_list().to_types().filter_wmclass('Sleipnir.exe')
    if not winlis:
        raise StandardError()
    win = winlis[0]
    if win.ismaximize():
        win.unsetmaximize()
    win.x, win.y = 1400, 100 # for my right windows
    win.move()
    sleep(0.5) # wait moved
    win.setmaximize()
    con.flush()


def click_sleipnir_refresh():
    r"""SUMMARY

    click_sleipnir_refresh()

    @Return:
    """
    print('try click refresh button')
    con = xcb2.connect()
    winlis = con.root.client_list().to_types().filter_wmclass('Sleipnir.exe')
    if not winlis:
        raise StandardError()
    win = winlis[0]
    sleep(1)
    sendkeys.SendKeys('{LClick 75 130}').sendkeys(win)


def auto_rss():
    r"""SUMMARY

    auto_rss()

    @Return:

    @Error:
    """
    run()
    wait_sleipnir_window()
    move_sleipnir()
    click_sleipnir_refresh()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sleipnir.py ends here
