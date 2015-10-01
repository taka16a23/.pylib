#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""observer -- DESCRIPTION

"""

import sys as _sys
import os as _os

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class Listener:
    def __init__(self, name, subject):
        self.name = name
        subject.register(self)

    def update(self, event):
        print self.name, "received event", event

class Subject:
    def __init__(self):
        self.listeners = []

    def register(self, listener):
        self.listeners.append(listener)

    def unregister(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self, event):
        for listener in self.listeners:
            listener.update(event)

subject = Subject()
listenerA = Listener("<listener A>", subject)
listenerB = Listener("<listener B>", subject)
# subject には2つのリスナーが登録されている。
subject.notify_listeners ("<event 1>")
# 出力:
#     <listener A> received event <event 1>
#     <listener B> received event <event 1>


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# observer.py ends here
