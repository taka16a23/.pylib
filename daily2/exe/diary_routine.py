#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: diary_routine.py 472 2015-08-28 03:36:21Z t1 $
# $Revision: 472 $
# $Date: 2015-08-28 12:36:21 +0900 (Fri, 28 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-28 12:36:21 +0900 (Fri, 28 Aug 2015) $

r"""Name: diary_routine.py

"""

import sys
import os
import argparse

from diary import DiaryDatabaseClient
from tempfile import mktemp
from t1.dateutil import tomorrow, datetime
import subprocess as sbp
from pathhandler import PathHandler
from recipe.menu2 import MenuManager
from recipe.menu2.common import DEFAULT_DIR
from ref.CMD import icedove
from mygmail import GmailAddressConst
from rectangle import Rectangle
from xcb import xinerama

from xahk.wm import Display
from xahk.events import EventLoop
from xahk.listener import WindowListenerFactory
from xahk.listener import WindowListenerFactoryObserver
from xahk.layout import GridLayout, GridSpec, LayoutParams

# for debug
import cgitb
cgitb.enable(format='text')


__revision__ = '$Revision: 472 $'
__version__ = '0.0.1'

# get tomorrow dates Diary
# write
# show
# write diary

BODY_FMT = u'WEATHER: \nRECIPE: {}\n'


def show_month_date_diarys():
    r"""SUMMARY

    show_diarys()

    @Return:

    @Error:
    """
    nextday = tomorrow()
    tpath = PathHandler(mktemp())
    tmpf = tpath.open('w')
    diary_client = DiaryDatabaseClient()
    notes = diary_client.list_by_date(month=nextday.month, day=nextday.day)
    for note in notes:
        tmpf.write(u'\n{}\n{}\n{}'.format('*' * 40, note.date,
                                          note.text.decode('utf-8')))
    tmpf.close()
    return sbp.Popen(['/usr/bin/mousepad', tpath])


def show_write_diary():
    r"""SUMMARY

    show_write_diary()

    @Return:

    @Error:
    """
    recipes = [x.get_name() for x in
               MenuManager(DEFAULT_DIR).get_menu(datetime.now()).iter_recipes()]
    body = BODY_FMT.format(u' '.join(recipes))
    ice = icedove.IcedoveMail(
        to=GmailAddressConst.DAILY, subject='Daily Routines')
    ice.set_body(body)
    tup = list(ice.getcmdtuple())
    tup[-1] = tup[-1].replace('"', '')
    return sbp.Popen(tup)


class DiaryRoutine(WindowListenerFactoryObserver):
    r"""DiaryRoutine

    DiaryRoutine is a WindowListenerFactoryObserver.
    Responsibility:
    """
    row12 = GridSpec.create_with_size(1, 1)
    col01 = GridSpec.create_with_size(0, 1)
    col23 = GridSpec.create_with_size(2, 1)

    right_param = LayoutParams(row12, col01)
    left_param = LayoutParams(row12, col23)

    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        WindowListenerFactoryObserver.__init__(self)
        self.display = display
        xinrm = display(xinerama.key)
        s = xinrm.QueryScreens().reply().screen_info[0]
        self.screen = Rectangle(s.x_org, s.y_org, s.width, s.height)
        self.layout = GridLayout()
        self.layout.set_wspace(3)
        self.layout.set_rows(4)
        self.layout.set_columns(4)
        self.windows = []
        self.is_starting = False
        self.write_pid = None
        self.read_pid = None

    def start(self, ):
        r"""SUMMARY

        start()

        @Return:

        @Error:
        """
        if self.is_starting:
            return
        self.is_starting = True
        WindowListenerFactory(Display()).add_observer(self)
        popen = show_month_date_diarys()
        self.read_pid = popen.pid
        popen2 = show_write_diary()
        self.write_pid = popen2.pid
        EventLoop(self.display).start_loop()

    def stop(self, ):
        r"""SUMMARY

        stop()

        @Return:

        @Error:
        """
        if not self.is_starting:
            return
        self.is_starting = False
        for window in self.windows:
            window.close()
        WindowListenerFactory(Display()).remove_observer(self)
        EventLoop(self.display).stop_loop()

    def on_created_window_listener(self, window):
        r"""SUMMARY

        on_created_window_listener(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if window.pid not in (self.read_pid, self.write_pid):
            return
        if window.pid == self.read_pid:
            self.windows.append(window)
            self.layout.set_layout_item(window, self.left_param)
        if window.pid == self.write_pid:
            self.windows.append(window)
            self.layout.set_layout_item(window, self.right_param)
        self.layout.layout(self.screen)

    def on_destroyed_window_listener(self, window_id):
        r"""SUMMARY

        on_destroyed_window_listener(window_id)

        @Arguments:
        - `window_id`:

        @Return:

        @Error:
        """
        if window_id in self.windows:
            self.windows.remove(window_id)
        if len(self.windows) == 0:
            self.stop()


def _predef_options():
    parser = argparse.ArgumentParser(description="""""")
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
    DiaryRoutine(Display()).start()

    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# diary_routine.py ends here
