#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""weather -- DESCRIPTION

"""
from time import sleep
import sys

from mygoogle import chrome
from mygoogle.chrome.variables import DEFAULT_OPTS as CHROME_OPTS

from xahk.wm.window_spec import WindowSpec
from xahk.listener.window_manager import WindowManagerListener
from xahk.listener.window_manager_observer import WindowManagerListenerObserver
from xahk.listener.client_observer import WindowClientListenerObserver
from xahk.events.loop import EventLoop
from xahk.x11.display import Display
from xahk.rectangle import Point


class WeatherSpec(WindowSpec):
    r"""WeatherSpec

    WeatherSpec is a WindowSpec.
    Responsibility:
    """
    title = 'weather - Google Chrome'
    wmclass = 'google-chrome'

    def is_satisfied_window(self, window):
        """SUMMARY

        is_satisfied_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if self.title == window.title and self.wmclass in window.wmclass:
            return True
        return False


class Weather(WindowManagerListenerObserver, WindowClientListenerObserver):
    r"""Weather

    Weather is a WindowManagerListenerObserver.
    Responsibility:
    """
    chrome_options = CHROME_OPTS + ['--new-window']
    url = 'http://sato.atso-net.jp/lab/weather'
    spec = WeatherSpec()
    right_point = Point(1500, 50)

    def __init__(self, ):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.window = None
        self.display = Display()
        self.wm = WindowManagerListener()
        self.wm.add_observer(self)
        if not self.exists_weather():
            self.show()
        for window in self.wm.client_list():
            window.add_observer(self)
            self.on_window_title_changed(window)
            self.on_created_window_client(window)
        EventLoop.get_instance(self.display).start_loop()

    def exists_weather(self, ):
        """SUMMARY

        exists_weather()

        @Return:

        @Error:
        """
        for window in self.wm.client_list():
            if self.spec.is_satisfied_window(window):
                return True
        return False

    def show(self, ):
        """SUMMARY

        show()

        @Return:

        @Error:
        """
        chrome.run(self.url, options=self.chrome_options)

    def on_window_title_changed(self, window):
        """SUMMARY

        on_window_title_changed(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if self.window:
            # on changed page weather to other
            if self.window == window:
                self.stop()
            return
        if not self.spec(window):
            return
        self.window = window
        self.window.move(self.right_point).check()
        self.window.maximize().check()
        self.window.raise_window().check()

    def on_created_window_client(self, window):
        """SUMMARY

        on_created_window_client(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if self.window:
            return
        window.add_observer(self)

    def on_destroyed_window_client(self, windowid):
        """SUMMARY

        on_destroyed_window_client(windowid)

        @Arguments:
        - `windowid`:

        @Return:

        @Error:
        """
        if self.window == windowid:
            self.stop()

    def stop(self, ):
        """SUMMARY

        on_destroyed_window_client(windowid)

        @Arguments:
        - `windowid`:

        @Return:

        @Error:
        """
        self.wm.remove_observer(self)
        EventLoop.get_instance(self.display).stop_loop()


def _main():
    Weather()
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# weather.py ends here
