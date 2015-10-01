#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import sys
import os as _os
import imp as _imp

from singledispatch import singledispatch

from pathhandler import PathHandler

if sys.version_info < (2, 4):
    from sets import Set as set


__version__ = "0.1.0"

__all__ = [ 'iter_pyfiles', 'list_pyfiles', ]


@singledispatch
def iter_pyfiles(dir_):
    r"""SUMMARY

    iter_pyfiles(dir_)

    @Arguments:
    - `dir_`:

    @Return:
    """
    raise TypeError('Must be String or List, given {}.'.format(type(dir_)))


@iter_pyfiles.register(str)
def iter_pyfiles_str(dir_):
    r"""SUMMARY

    iter_pyfiles(dir_)

    @Arguments:
    - `dir_`:

    @Return:
    """
    dir_ = PathHandler(dir_)
    for file_ in dir_.listdir():
        if file_.endswith(('.py', '.pyc')):
            yield dir_.join(file_)


@iter_pyfiles.register(list)
def iter_pyfiles_list(dirs):
    r"""SUMMARY

    iter_pyfiles_list(dir_)

    @Arguments:
    - `dir_`:

    @Return:
    """
    for dir_ in dirs:
        for file_ in iter_pyfiles_str(str(dir_)):
            yield file_


@iter_pyfiles.register(tuple)
def iter_pyfiles_tuple(dirs):
    r"""SUMMARY

    iter_pyfiles_list(dirs)

    @Arguments:
    - `dir_`:

    @Return:
    """
    for dir_ in dirs:
        for file_ in iter_pyfiles_str(str(dir_)):
            yield file_


def list_pyfiles(dir_):
    r"""SUMMARY

    list_pyfiles(dir_)

    @Arguments:
    - `dir_`:

    @Return:
    """
    return list(iter_pyfiles(dir_))


def getmodules(path):
    r"""SUMMARY

    getmodules(path)

    @Arguments:
    - `path`:

    @Return:
    """
    mods = set()
    add = mods.add
    for file_ in list_pyfiles(path):
        if not file_.endswith(('.pyc')):
            fname, _ = file_.splitext()
            add(_imp.load_source(fname, file_))
    return list(mods)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
