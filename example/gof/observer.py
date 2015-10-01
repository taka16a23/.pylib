#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: observer.py 105 2014-02-22 09:25:25Z t1 $
# $Revision: 105 $
# $Date: 2014-02-22 18:25:25 +0900 (Sat, 22 Feb 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-02-22 18:25:25 +0900 (Sat, 22 Feb 2014) $

r"""observer -- DESCRIPTION

"""

import sys as _sys
import os as _os

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 105 $'
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
