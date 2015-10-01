#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
## Change Log:
##
## 2013/11/22    Atami
##    Added: `showall' function.

r"""_functions -- part of wm

"""
import re as _re
import sys as _sys
import types as _types
from time import sleep as _sleep

from Xlib import X as X
from Xlib.display import Display
from wm._core import WindowManager
from wm.error import TimeoutError


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.'

__all__ = ['WinWait', 'listids', 'iter_wins', 'iter_winattr', 'exists',
           'getwin', 'iter_matchwin', 'getpid', 'isactive', 'showall']

def listids():
    r"""SUMMARY

    @Return:
    """
    display = Display()
    root = display.screen().root
    return (root.get_full_property(
        display.intern_atom('_NET_CLIENT_LIST'), X.AnyPropertyType).value)


def iter_wins():
    r"""Generator

    @Return:
    """
    for id_ in listids():
        yield WindowManager(id_)


def iter_winattr(attr):
    r"""SUMMARY

    @Arguments:
    - `attr`:

    @Return:
    """
    for win in iter_wins():
        yield getattr(win, attr)


def _confirm(win, **args):
    r"""SUMMARY

    @Arguments:

    - `win`:
    - `title`:
    - `klass`:
    - `pid`:
    - `regexp`:

    @Return:
    """
    # prevent
    if not win:
        return False

    if 'regexp' in args:
        return (_re.search(args['regexp'], win.title) is not None)
    elif 'klass' in args:
        return args['klass'] == win.klass[1]
    else:
        for attr in ('title', 'id', 'pid', 'psname', 'cmdline', 'cwd', ):
            if attr in args and args[attr] == getattr(win, attr):
                return True
        return False


def exists(confirm=_confirm, **args):
    r"""SUMMARY

    @Arguments:
    - `**args`:

    @Return:
    """
    return bool(getwin(confirm=confirm, **args))


def getwin(confirm=_confirm, **args):
    r"""SUMMARY

    @Arguments:

    - `title`:
    - `klass`:
    - `pid`:
    - `active`:
    - `regexp`:

    @Return: if exists window object, and not exists return None.
    """
    # parse windows
    for id_ in listids():
        win = WindowManager(id_)
        if confirm(win=win, **args):
            return win
    # not matched
    return None


def iter_matchwin(confirm=_confirm, **args):
    r"""SUMMARY

    @Arguments:
    - `confirm`:
    - `** args`:

    @Return:
    """
    for win in iter_wins():
        if confirm(win=win, **args):
            yield win


def getpid(win):
    r"""SUMMARY

    @Arguments:
    - `win`:

    @Return:
    """
    display = Display()
    pid_reply = win.get_property(display.intern_atom('_NET_WM_PID'),
                                 X.AnyPropertyType, 0, 10)
    return int(pid_reply.value.tolist()[0])


def isactive(confirm=_confirm, **args):
    r"""SUMMARY

    @Arguments:

    - `title`:
    - `klass`:
    - `pid`:
    - `regexp`:

    @Return:
    """
    win = getwin(confirm=confirm, **args)
    if not win:
        return False
    return win.isactive()


def showall():
    r"""SUMMARY

    showall()

    @Return:
    """
    for win in iter_wins():
        print('\n{0:*<40}'.format(''))
        print(win)


class WinWait(object):
    r"""
    """

    def __init__(self, sec=0, confirm=_confirm):
        r"""
        """
        self.set_sec(sec)
        self.set_confirm(confirm)

    def set_sec(self, sec):
        r"""SUMMARY

        @Arguments:

        - `sec`:

        @Return:
        """
        if type(sec) is not _types.IntType:
            msg = ('"sec" is not int type. Must be int. We got {}'
                   .format(str(type(sec))))
            raise ValueError(msg)
        self._sec = sec

    def set_confirm(self, confirm):
        r"""SUMMARY

        @Arguments:

        - `confirm`:

        @Return:
        """
        if type(confirm) != _types.FunctionType:
            raise ValueError('Not functions {}'.format(type(confirm)))
        self._confirm = confirm

    def _wait(self, breaker, **args):
        r"""SUMMARY

        @Arguments:
        - `breaker`:
        - `sec`:
        - `confirm`:
        - `**args`:

        @Return:
        """
        wait = self._sec * 2
        count = 0
        while 1:
            try:
                if breaker(confirm=self._confirm, **args) is True:
                    return True
                _sleep(0.5)
                # infinity loop if sec is 0
                if wait == 0:
                    continue
                count += 0.5
                if wait <= count:
                    raise TimeoutError(count / 2)
            except KeyboardInterrupt:
                print('KeyboardInterrupted')
                break

    def win(self, **args):
        r"""SUMMARY

        @Arguments:

        - `sec`:
        - `title`:
        - `klass`:
        - `pid`:
        - `regexp`:

        @Return:
        """
        def breaker(confirm, **args):
            if exists(confirm=confirm, **args) is True:
                return True
            return False
        return self._wait(breaker=breaker, **args)

    def close(self, **args):
        r"""SUMMARY

        @Arguments:

        - `sec`:
        - `title`:
        - `klass`:
        - `pid`:
        - `regexp`:

        @Return:
        """
        def breaker(confirm, **args):
            return bool(not exists(confirm=confirm, **args))
        return self._wait(breaker=breaker, **args)

    def active(self, **args):
        r"""SUMMARY

        @Arguments:

        - `title`:
        - `klass`:
        - `pid`:
        - `regexp`:

        @Return:
        """
        def breaker(confirm, **args):
            if isactive(confirm=confirm, **args) is True:
                return True
            return False
        return self._wait(breaker=breaker, **args)

    def deactive(self, **args):
        r"""SUMMARY

        @Arguments:

        - `title`:
        - `klass`:
        - `pid`:
        - `regexp`:

        @Return:
        """
        def breaker(confirm, **args):
            return bool(not isactive(confirm=confirm, **args))
        return self._wait(breaker=breaker, **args)


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _functions.py ends here
