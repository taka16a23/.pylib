#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""loop -- DESCRIPTION


Xサーバー から event を受け取り EventDispatcher へ送る。
Singleton である。

EventListener のインターフェースを変更したい場合は
EventDispatcher を変更する。
Event の分配方法はEventDispatcherに依存する。
EventDispatcher は インターフェース dispatch_event(event) を保持すること。

`poll_for_event` を持った Display を置き換えれば再利用できる。
`dispatch_event` を持った EventDispatcher を置き換えれば再利用できる。
"""
from time import sleep
from collections import deque

from xahk.utils.observer import Observable
from .dispatcher import EventDispatcher
from .dispatcher_observer import EventDispatcherObserver


class EventLoop(Observable, EventDispatcherObserver):
    """EventLoop

    EventLoop is a object.
    Responsibility: Xサーバー から受け取ったイベントを EventDispatcher へ送る。
    """
    _instance = None

    def __init__(self, display):
        """

        @Arguments:
        - `display`: Display
        display は `poll_for_event` を要求する。
        `poll_for_event` はイベントか None を返す。

        @Return:
        """
        Observable.__init__(self)
        self.display = display
        self.dispatcher = EventDispatcher()
        self.dispatcher.add_observer(self)
        self._event_queue = deque()
        self._continue_stream = False

    @classmethod
    def get_instance(cls, display):
        if cls._instance is None:
            cls._instance = cls(display)
        return cls._instance

    def get_display(self, ):
        """保持しているXDisplay を返す。

        get_display()

        @Return:

        @Error:
        """
        return self.display

    def get_event_dispatcher(self, ):
        """保持している EventDispatcher を返す。

        get_event_dispatcher()

        @Return:

        @Error:
        """
        return self.dispatcher

    def set_event_dispatcher(self, dispatcher):
        """EventDispatcher をセットする。

        set_event_dispatcher(dispatcher)

        @Arguments:
        - `dispatcher`: EventDispatcher

        @Return:

        @Error:
        """
        self.dispatcher = dispatcher
        self.dispatcher.add_observer(self)

    def add_event_listener(self, listener):
        """EventListener を追加する。

        add_listener(listener)

        @Arguments:
        - `listener`: EventListener

        @Return:

        @Error:
        """
        if self.has_event_listener(listener):
            return False
        self.dispatcher.add_event_listener(listener)

    def remove_event_listener(self, listener):
        """EventListener を削除する。

        remove_listener(listener)

        @Arguments:
        - `listener`:

        @Return:

        @Error:
        ValueError
        """
        self.dispatcher.remove_event_listener(listener)

    def has_event_listener(self, listener):
        """EventListener があればTrue を返す。

        has_listener(listener)

        @Arguments:
        - `listener`:

        @Return:

        @Error:
        """
        return self.dispatcher.has_event_listener(listener)

    def clear_event_listeners(self, ):
        """保持している EventListener をすべて削除する。

        clear_listeners()

        @Return:

        @Error:
        """
        self.dispatcher.clear_event_listeners()

    def list_event_listeners(self, ):
        """保持している EventListener をすべて返す。

        list_listeners()

        @Return:

        @Error:
        """
        return self.dispatcher.list_event_listeners()

    def _load_events(self, ):
        """Xサーバー からのイベントを保持する。

        _load_events()

        @Return:
        None

        @Error:
        """
        while 1:
            event = self.display.poll_for_event()
            if event is None:
                sleep(0.01) # reduce cpu usage
                break
            self._event_queue.append(event)

    def _dispatch_events(self, ):
        """保持している Event を EventDispatcher へ送る。

        _dispatch_events()

        @Return:

        @Error:
        AttributeError

        queue にある Event を EventDispatcher へ送る。
        """
        while self._event_queue:
            self.dispatcher.dispatch_event(self._event_queue.popleft())

    def start_loop(self, ):
        """Xサーバー からの Event を EventDispatcher へ送る。ループを開始する。

        start_loop()

        @Return:

        @Error:
        """
        self._notify_before_start_loop()
        self._continue_stream = True
        while self._continue_stream:
            self._load_events()
            self._dispatch_events()
        self._notify_after_stopped_loop()

    def stop_loop(self, ):
        """ループを停止する。

        stop_loop()

        @Return:

        @Error:
        """
        self._continue_stream = False

    def is_starting(self, ):
        """ループしているか確認する。

        is_starting()

        @Return:

        @Error:
        """
        return self._continue_stream

    def on_changed_listeners(self, dispatcher):
        """SUMMARY

        on_changed_listeners(dispatcher)

        @Arguments:
        - `dispatcher`:

        @Return:

        @Error:
        """
        self._notify_changed_listeners()

    def _notify_changed_listeners(self, ):
        """SUMMARY

        _notify_changed_listeners()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_listeners(self)

    def _notify_changed_dispatcher(self, ):
        """SUMMARY

        _notify_changed_dispatcher(loop)

        @Arguments:
        - `loop`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_dispatcher(self)

    def _notify_before_start_loop(self, ):
        """SUMMARY

        _notify_before_start_loop()

        @Arguments:
        - `loop`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_before_start_loop(self)

    def _notify_after_stopped_loop(self, ):
        """SUMMARY

        _notify_after_stopped_loop()

        @Arguments:
        - `loop`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_after_stopped_loop(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# loop.py ends here
