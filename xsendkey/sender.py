#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sender -- DESCRIPTION

"""
from collections import deque

from interval import Interval


class XSender(object):
    r"""XSender

    XSender is a object.
    Responsibility:
    """
    def __init__(self, xinputs):
        r"""

        @Arguments:
        - `sendkeys`:
        - `interval`:
        """
        self._xinputs = deque()
        self.extend(xinputs)

    def _check(self, xinput):
        r"""SUMMARY

        _check(sendkey)

        @Arguments:
        - `sendkey`:

        @Return:

        @Error:
        """
        for attr in ('set_window', 'input'):
            if not hasattr(xinput, attr):
                # TODO: (Atami) [2015/01/25]
                raise AttributeError()

    def append(self, xinput):
        r"""SUMMARY

        append(sendkey)

        @Arguments:
        - `sendkey`:

        @Return:

        @Error:
        """
        self._check(xinput)
        self._xinputs.append(xinput)

    def appendleft(self, xinput):
        r"""SUMMARY

        appendleft(sendkey)

        @Arguments:
        - `xinput`:

        @Return:

        @Error:
        """
        self._check(xinput)
        self._xinputs.appendleft(xinput)

    def pop(self, ):
        r"""SUMMARY

        pop()

        @Return:

        @Error:
        """
        return self._xinputs.pop()

    def popleft(self, ):
        r"""SUMMARY

        popleft()

        @Return:

        @Error:
        """
        return self._xinputs.popleft()

    def extend(self, xinputs):
        r"""SUMMARY

        extend(inputs)

        @Arguments:
        - `inputs`:

        @Return:

        @Error:
        """
        for xinput in xinputs:
            self._check(xinput)
        self._xinputs.extend(xinputs)

    def extendleft(self, xinputs):
        r"""SUMMARY

        extendleft(xinputs)

        @Arguments:
        - `sendkeys`:

        @Return:

        @Error:
        """
        for xinput in xinputs:
            self._check(xinput)
        self._xinputs.extendleft(xinputs)

    def remove(self, xinput):
        r"""SUMMARY

        remove(xinput)

        @Arguments:
        - `sendkey`:

        @Return:

        @Error:
        """
        self._xinputs.remove(xinput)

    def reverse(self, ):
        r"""SUMMARY

        reverse()

        @Return:

        @Error:
        """
        self._xinputs.reverse()

    def count(self, xinput):
        r"""SUMMARY

        count()

        @Return:

        @Error:
        """
        return self._xinputs.count(xinput)

    def rotate(self, n=1):
        r"""SUMMARY

        rotate(n=1)

        @Arguments:
        - `n`:

        @Return:

        @Error:
        """
        self._xinputs.rotate(n)

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._xinputs.clear()

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        for xinput in self._xinputs:
            xinput.set_window(window)

    def send(self, ):
        r"""SUMMARY

        send(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        for xinput in self._xinputs:
            xinput.input()

    def __getitem__(self, index):
        return self._xinputs[index]

    def __setitem__(self, index, xinput):
        self._check(xinput)
        self._xinputs[index] = xinput

    def __delitem__(self, index):
        del self._xinputs[index]

    def __len__(self):
        return len(self._xinputs)

    def __iter__(self):
        return iter(self._xinputs)


class XIntervalSender(XSender):
    r"""XIntervalSend

    XIntervalSend is a object.
    Responsibility:
    """
    def __init__(self, xinputs, interval=0):
        r"""

        @Arguments:
        - `sendkeys`:
        - `interval`:
        """
        XSender.__init__(self, xinputs)
        self._interval = Interval(interval)

    def get_interval(self, ):
        r"""SUMMARY

        get_interval()

        @Return:

        @Error:
        """
        return self._interval

    def set_interval(self, sec):
        r"""SUMMARY

        set_interval(sec)

        @Arguments:
        - `sec`:

        @Return:

        @Error:
        """
        self._interval.set(sec)

    interval = property(get_interval, set_interval)

    def _check(self, xinput):
        r"""SUMMARY

        _check(xinput)

        @Arguments:
        - `xinput`:

        @Return:

        @Error:
        """
        super(XIntervalSender, self)._check(xinput)
        if not hasattr(xinput, 'flush'):
            # TODO: (Atami) [2015/01/25]
            raise AttributeError()

    def _interval_send(self, ):
        r"""SUMMARY

        interval_send(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        for xinput in self._xinputs:
            self._interval()
            xinput.input()
            xinput.flush()

    def send(self, ):
        r"""SUMMARY

        send(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        if self._interval == 0:
            return super(XIntervalSender, self).send()
        return self._interval_send()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sender.py ends here
