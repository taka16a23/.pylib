#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""window_listener_factory -- DESCRIPTION

"""
from xcb.xproto import BadWindow

from observer import Observable

from xahk.commons.display_multiton import multiton_display
from xahk.listener.root_window_listener_observer import RootWindowListenerObserver
from xahk.listener.root_window_listener import RootWindowListener
from xahk.listener._window_listener import WindowListener


@multiton_display()
class WindowListenerFactory(Observable, RootWindowListenerObserver):
    """Class WindowListenerFactory
    """
    # Attributes:
    def __init__(self, display):
        r"""

        @Arguments:
        - `display`:
        """
        Observable.__init__(self)
        self._root = RootWindowListener(display)
        self._root.add_observer(self)
        self._windows = []
        for wid in self._root.client_list():
            self._create_window_listener(wid)

    # Operations
    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._root.get_display()

    display = property(get_display)

    def on_changed_client_list(self, root_window):
        """function on_changed_client_list

        root_window:

        returns
        """
        windows = set(self._windows)
        window_ids = set(root_window.client_list())
        for wid in list(window_ids - windows):
            self._create_window_listener(wid)
        for wid in list(windows - window_ids):
            self._destroy_window_listener(wid.get_id())

    def list_windows(self, filter=bool):
        """function list_windows

        filter:

        returns
        """
        return [w for w in self._windows if filter(w)]

    def _create_window_listener(self, window_id):
        """function create_window_listener

        window_id: int

        returns
        """
        try:
            window = WindowListener(self.display, window_id)
        except BadWindow as err:
            from xahk.logger import LOG
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            return
        except StandardError as err:
            from xahk.logger import LOG
            LOG.error('{}'.format(err))
            import os
            os.system('modprobe pcspkr')
            os.system('/usr/bin/beep -f250 -r2 -l50')
            os.system('rmmod pcspkr')
            return
        self._windows.append(window)
        for observer in self._observers:
            observer.on_created_window_listener(window)

    def _destroy_window_listener(self, window_id):
        """function destroy_window_listener

        window_id:

        returns
        """
        if window_id not in self._windows:
            return
        self._windows.remove(window_id)
        for observer in self._observers:
            observer.on_destroyed_window_listener(window_id)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_listener_factory.py ends here
