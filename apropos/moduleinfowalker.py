#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" moduleinfowalker -- gathering infomation of modules for apropos.
"""

import sys as _sys
import inspect as inspect
from collections import defaultdict as _defaultdict

import pkgutil as _pkgutil

from abstract.abcs import IterABC


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class ModuleInfoWalker(IterABC):
    r"""
    """

    def __init__(self, ):
        for _, _, _ in _pkgutil.walk_packages(onerror=lambda name: None):
            pass
        self._iters = self._itermodinfo()

    def __iter__(self):
        return self

    def next(self):
        r"""SUMMARY

        @Return:
        """
        return self._iters.next()

    def _itermodinfo(self):
        r"""SUMMARY

        @Return:
        """
        for key, obj in _sys.modules.items():
            if not obj:
                continue
            yield _defaultdict(str, name=key, file=getsafeabsfile(obj),
                               type=type(obj), definition=key,
                               summary=getdocsummary(obj),
                               doc = (inspect.getdoc(obj) or ''))
            try:
                for d in self._recursivemod(obj, parent=key):
                    yield d
            except NotImplementedError:
                continue
            except SystemExit:
                continue

    def _recursivemod(self, obj, parent=''):
        r"""SUMMARY

        @Return:
        """
        if '' == parent and hasattr(obj, '__name__'):
            parent = obj.__name__

        for memname, subobj in inspect.getmembers(obj):
            if memname.startswith('_') and memname.endswith('__'):
                continue
            if inspect.isfunction(subobj) or inspect.ismethod(subobj):
                yield _defaultdict(
                    str, name=parent+'.'+memname,
                    file=getsafeabsfile(subobj),
                    type=type(subobj),
                    definition=getdef(subobj, parent+'.'+memname),
                    summary=getdocsummary(subobj),
                    doc=(inspect.getdoc(subobj) or ''))

            if inspect.isclass(subobj):
                yield _defaultdict(str,
                                   name=parent+'.'+memname,
                                   file=getsafeabsfile(subobj),
                                   type=type(subobj),
                                   definition=parent+'.'+memname+'()',
                                   summary=getdocsummary(subobj),
                                   doc = (inspect.getdoc(subobj) or ''))
                self._recursivemod(subobj, parent=parent+'.'+memname+'()')


## functions
#
def getbuiltins():
    r"""SUMMARY

    @Return:
    """
    for name, builtin in inspect.getmembers(__builtins__):
        if name.startswith('_'):
            continue
        yield name, builtin


def getbuiltinmodules():
    r"""SUMMARY

    @Return:
    """
    for modname in _sys.builtin_module_names:
        if modname == '__main__':
            continue
        yield modname, __import__(modname)


def getmodules():
    r"""SUMMARY

    @Return:
    """
    for _, modname, _ in _pkgutil.iter_modules():
        yield modname, __import__(modname)


def getdef(obj, name):
    r"""SUMMARY

    @Arguments:
    - `obj`:
    - `name`:

    @Return:
    """
    if not callable(obj):
        return name
    try:
        return str(inspect.getargspec(obj)).replace('ArgSpec', name)
    except TypeError:
        return name + '()'


def getdocsummary(obj):
    r"""SUMMARY

    @Arguments:
    - `obj`:

    @Return:
    """
    # Do not use splitlines instead split('\n'),
    # it will raise IndexError.
    return (inspect.getdoc(obj) or '').split('\n')[0]


def getsafeabsfile(obj):
    r"""SUMMARY

    @Arguments:
    - `obj`:

    @Return:
    """
    try:
        return inspect.getabsfile(obj)
    except TypeError:
        return ''


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# moduleinfowalker.py ends here
