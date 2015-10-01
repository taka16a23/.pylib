#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""abc -- a parts of abstract

"""

import sys as _sys
import os as _os
from time import sleep as _sleep
import select
from abc import ABCMeta, abstractmethod

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class IterABC(object):
    r"""Abstract Base Classes for Iterator."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def __iter__(self, ):
        raise NotImplementedError

    @abstractmethod
    def next(self, ):
        raise NotImplementedError


class BoolABC(object):
    r"""Abstract Base Classes for Boolean."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def __nonzero__(self, ):
        raise NotImplementedError


class WithABC(object):
    r"""Abstract Base Classes for With Statements."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def __enter__(self, ):
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, type, value, tb):
        raise NotImplementedError


class FileAdaptorABC(object):
    r"""Abstract Base Classes for File Adaptor."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def close(self, ):
        raise NotImplementedError

    @abstractmethod
    def __del__(self, ):
        raise NotImplementedError

    @abstractmethod
    def flush(self, ):
        raise NotImplementedError

    @abstractmethod
    def fileno(self, ):
        raise NotImplementedError

    @abstractmethod
    def write(self, ):
        raise NotImplementedError

    @abstractmethod
    def writelines(self, ):
        raise NotImplementedError

    @abstractmethod
    def read(self, ):
        raise NotImplementedError

    @abstractmethod
    def readline(self, ):
        raise NotImplementedError

    @abstractmethod
    def __iter__(self, ):
        raise NotImplementedError

    @abstractmethod
    def next(self, ):
        raise NotImplementedError


class SelectABC(object):
    r"""
    """

    __metaclass__ = ABCMeta

    def __init__(self, rlist, wlist, xlist, timeout=0):
        r"""

        @Arguments:
        - `rlist`:
        - `wlist`:
        - `xlist`:
        - `timeout`:
        """
        self.rlist = rlist
        self.wlist = wlist
        self.xlist = xlist
        self.timeout = timeout

    def wait_io(self, ):
        r"""SUMMARY

        wait_io()

        @Return:
        """
        return select.select(self.rlist, self.wlist, self.xlist, self.timeout)

    def handle_io(self, ):
        r"""SUMMARY

        handle_io()

        @Return:
        """
        while 1:
            _sleep(0.015) # for prevent exhaust cpu
            try:
                rlist, wlist, xlist = self.wait_io()
            except select.error, err:
                print(err)
                break
            except IOError, err:
                print(err)
                break
            # rlist
            if rlist: # for fast
                for obj in rlist:
                    self.handle_read(obj)
            # wlist
            if wlist: # for fast
                for obj in wlist:
                    self.handle_write(obj)
            # xlist
            if xlist: # for fast
                for obj in xlist:
                    self.handle_except(obj)

    @abstractmethod
    def handle_read(self, obj):
        r"""SUMMARY

        handle_read(io_obj)

        @Arguments:
        - `io_obj`:

        @Return:
        """
        raise NotImplementedError

    @abstractmethod
    def handle_write(self, obj):
        r"""SUMMARY

        handle_write(io_obj)

        @Arguments:
        - `io_obj`:

        @Return:
        """
        raise NotImplementedError

    @abstractmethod
    def handle_except(self, obj):
        r"""SUMMARY

        handle_except(io_obj)

        @Arguments:
        - `io_obj`:

        @Return:
        """
        raise NotImplementedError


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# abc.py ends here
