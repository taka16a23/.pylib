#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""diary_routine -- DESCRIPTION

"""
import sys
from tempfile import mktemp
import subprocess as sbp

from t1.dateutil import tomorrow, datetime
from pathhandler import PathHandler
from diary import DiaryDatabaseClient
from recipe.menu2 import MenuManager
from recipe.menu2.common import DEFAULT_DIR
from ref.CMD import icedove
from mygmail import GmailAddressConst

from xahk.listener.window_manager_observer import WindowManagerListenerObserver
from xahk.listener.window_manager import WindowManagerListener
from xahk.layout import GridLayout, GridSpec, LayoutParams
from xahk.x11.display import Display
from xahk.events.loop import EventLoop


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
    """SUMMARY

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


class DiaryRoutine(WindowManagerListenerObserver):
    r"""DiaryRoutine

    DiaryRoutine is a WindowManagerListenerObserver.
    Responsibility:
    """
    row12 = GridSpec.create_with_size(1, 1)
    col01 = GridSpec.create_with_size(0, 1)
    col23 = GridSpec.create_with_size(2, 1)

    right_param = LayoutParams(row12, col01)
    left_param = LayoutParams(row12, col23)
    layout = GridLayout()
    layout.set_wspace(3)
    layout.set_rows(4)
    layout.set_columns(4)

    def __init__(self, ):
        r"""
        """
        self.display = Display()
        self.windows = []
        self._wm = WindowManagerListener()
        self.screen = self._wm.list_screens()[0]
        self.read_pid = None
        self.write_pid = None

    def start(self, ):
        """SUMMARY

        start()

        @Return:

        @Error:
        """
        self._wm.add_observer(self)
        self.read_pid = show_month_date_diarys().pid
        self.write_pid = show_write_diary().pid
        EventLoop.get_instance(self.display).start_loop()

    def stop(self, ):
        """SUMMARY

        stop()

        @Return:

        @Error:
        """
        for window in self.windows:
            window.close().check()
        self._wm.remove_observer(self)
        EventLoop.get_instance(self.display).stop_loop()

    def on_created_window_client(self, window):
        """SUMMARY

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
        for cookie in self.layout.layout(self.screen):
            cookie.check()

    def on_destroyed_window_client(self, windowid):
        """SUMMARY

        on_destroyed_window_listener(windowid)

        @Arguments:
        - `windowid`:

        @Return:

        @Error:
        """
        if windowid in self.windows:
            self.windows.remove(windowid)
        if len(self.windows) == 0:
            self.stop()



def _main():
    DiaryRoutine().start()
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# diary_routine.py ends here
