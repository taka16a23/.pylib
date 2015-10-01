#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""weather2 -- DESCRIPTION

"""
import argparse
from time import sleep
import sys
from mygoogle import chrome
from mygoogle.chrome.variables import DEFAULT_OPTS as CHROME_OPTS
from datetime import datetime

from xahk.binder import Accelerator
from xahk.windowspec import WindowTitleSpec
from xahk.events import EventLoop
from xahk.listener import WindowListenerFactory
from xahk.listener import WindowListenerFactoryObserver
from xahk.listener import WindowListenerObserver
from xahk.wm import Display
from xahk.layout import GridLayout, GridSpec, LayoutParams
from xahk.piece import X11Key
from rectangle import Rectangle
from xcb import xinerama


ROW0 = GridSpec.create(0)
ROW1 = GridSpec.create(1)
COL0 = GridSpec.create(0)
COL1 = GridSpec.create(1)
COL2 = GridSpec.create(2)

DOWN_ACCE = Accelerator(116)


CHROME_OPTIONS = CHROME_OPTS + ['--new-window']


class WeatherInfo(object):
    r"""WeatherInfo

    WeatherInfo is a object.
    Responsibility:
    """
    def __init__(self, spec, param, key_count=0, above=False):
        r"""

        @Arguments:
        - `spec`:
        - `param`:
        - `command`:
        """
        self.spec = spec
        self.param = param
        self.key_count = key_count
        self.above = above


class WeatherMap(WindowListenerFactoryObserver, WindowListenerObserver):
    r"""WeatherMap

    WeatherMap is a WindowListenerFactoryObserver.
    Responsibility:
    """
    winfo = [
        WeatherInfo(
            WindowTitleSpec(
                'ピンポイント天気（大津） - ウェザーニュース - Google Chrome'),
                        LayoutParams(ROW0, COL0), 2, True),
            WeatherInfo(WindowTitleSpec(
                '気象庁 | 天気予報 - Google Chrome'),
                        LayoutParams(ROW0, COL1), 9, True),
            WeatherInfo(WindowTitleSpec(
                '雨雲レーダー - ウェザーニュース - Google Chrome'),
                        LayoutParams(ROW0, COL2), 1, True),
            WeatherInfo(WindowTitleSpec(
                '気象庁 | 天気図 - Google Chrome'),
                        LayoutParams(ROW1, COL0, top=-40, bottom=55), 9),
            WeatherInfo(WindowTitleSpec(
                '衛星画像 - ウェザーニュース - Google Chrome'),
                        LayoutParams(ROW1, COL1, top=-40, bottom=40), 1),
            WeatherInfo(WindowTitleSpec(
                '気象庁 | 異常天候早期警戒情報 - Google Chrome'),
                        LayoutParams(ROW1, COL2, top=-40, bottom=40), 8)
                         ]

    def __init__(self, display):
        r"""
        """
        self.display = display
        xinrm = display(xinerama.key)
        s = xinrm.QueryScreens().reply().screen_info[0]
        self.screen = Rectangle(s.x_org, s.y_org, s.width, s.height)
        self.layout = GridLayout()
        self.windows = []
        self.is_starting = False

    def start(self, ):
        r"""SUMMARY

        start()

        @Return:

        @Error:
        """
        if self.is_starting:
            return
        self.is_starting = True
        for window in WindowListenerFactory(self.display).list_windows():
            window.add_observer(self)
        WindowListenerFactory(Display()).add_observer(self)
        urls = list(chrome.ChromeBMParse('【天気】'))
        for url in urls:
            chrome.run(url, options=CHROME_OPTIONS)
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

    def on_window_title_changed(self, window):
        r"""SUMMARY

        on_window_title_changed(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if window in self.windows:
            return
        for info in self.winfo:
            if info.spec.is_satisfied(window):
                self.layout.set_layout_item(window, info.param)
                self.windows.append(window)
                break
        if len(self.winfo) == len(self.windows):
            self.layout.layout(self.screen)
            for info in self.winfo:
                windows = [w for w in self.windows if info.spec.is_satisfied(w)]
                if not windows:
                    continue
                if info.above:
                    windows[0].set_always_on_top()
                else:
                    windows[0].raise_window()
            sleep(1.5)
            for info in self.winfo:
                windows = [w for w in self.windows if info.spec.is_satisfied(w)]
                if not windows:
                    continue
                xkey = X11Key(DOWN_ACCE.get_code())
                windows[0].activate()
                sleep(1)
                for _ in xrange(info.key_count):
                    xkey.tap(windows[0].id)
                    xkey.display.flush()
                sleep(0.3)

    def on_created_window_listener(self, window):
        r"""SUMMARY

        on_created_window_listener(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        window.add_observer(self)

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
            self.stop()

    def __del__(self):
        """
        INTERNAL COMMENT
        Do not imprement `raise'!!
        """
        self.stop()


def _predef_options():
    parser = argparse.ArgumentParser(description=""" """)

    parser.add_argument('--winter',
                        dest='winter',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Open Winter weather')

    parser.add_argument('--summer',
                        dest='summer',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='open summer weather')

    # (yas/expand-link "argparse_add_argument" t)
    return parser


def _main():
    parser = _predef_options()
    opts = parser.parse_args()
    # TODO: (Atami) [2015/08/05]
    # chrome activate
    # sleep(1)
    if datetime.now().month in (2, 3, 4) or opts.winter:
        chrome.open_folder('Winter')
        sleep(5)
    if datetime.now().month in (7, 8, 9, 10) or opts.summer:
        chrome.open_folder('Summer')
        sleep(5)
    WeatherMap(Display()).start()
    return 0

if __name__ == '__main__':
    sys.exit(_main())




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# weather2.py ends here
