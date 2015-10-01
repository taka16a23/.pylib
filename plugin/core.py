#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: core.py 468 2015-08-19 05:49:01Z t1 $
# $Revision: 468 $
# $Date: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $

r"""core -- DESCRIPTION

"""

import sys as _sys
import os as _os
import imp
import inspect
from abc import ABCMeta, abstractmethod

from dispatcher import Dispatcher
from t1 import pyutil
from pathhandler import PathHandler


import predicate as _predicate

if _sys.version_info < (2, 4):
    from sets import Set as set

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')

__revision__ = '$Revision: 468 $'
__version__ = '0.1.0'


class PluginAbstract(object):
    r"""
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()


class Plugin(Dispatcher):
    r"""Plugin load and dispatcher."""

    def __init__(self, path=None):
        Dispatcher.__init__(self)
        self.path = set()
        self.set_plugins_dir(path)

    def __repr__(self, ):
        if not self:
            self.load()
        if not self:
            return '{}'
        from dotavoider import ListDotAvoider
        strs, append = ListDotAvoider().append
        append('title: <class_string> "doc summary"\n{')
        fmt = '{}: {} "{}",'.format
        for key, func in self.iteritems():
            doc_summary = func.__doc__.splitlines()[0]
            append(fmt(key, func.__class__, doc_summary))
            append('\n ')
        strs.pop() # remove tail of '\n'
        append('}')
        return ''.join(strs)

    def __str__(self, ):
        return self.__repr__()

    def __call__(self, *args, **kwargs):
        if not self:
            self.load()
        # Dispatcher.__call__(self, *args, **kwargs)
        return super(Plugin, self).__call__(*args, **kwargs)

    def set_plugins_dir(self, dir_):
        r"""SUMMARY

        set_plugins_dir(dir_)

        @Arguments:
        - `dir_`:

        @Return:
        """
        if not dir_:
            pass
        elif _predicate.isstring(dir_):
            self.path.add(dir_)
        elif _predicate.islist(dir_) or _predicate.istuple(dir_):
            for dirpath in dir_:
                self.path.add(dirpath)

    def load(self):
        r"""SUMMARY

        load(path)

        @Arguments:
        - `path`:

        @Return:
        """
        for path in self.path:
            for file_ in pyutil.iter_pyfiles(path):
                if file_.endswith(('.pyc')) or file_ == '__init__.py':
                    continue
                try:
                    filename, _ = PathHandler(file_).splitext()
                    print(filename)
                    print(file_)
                    mod = imp.load_source(
                        file_.get_basename().splitext()[0], file_)
                except IOError as err:
                    # import warnings
                    # warnings.warn(err)
                    continue
                for name, obj in parse_plugins(mod):
                    if hasattr(obj, 'title'):
                        name = obj.title
                    if (hasattr(obj, 'activate') and not obj.activate):
                        continue
                    if name in self:
                        import warnings
                        warnings.warn('Plugin Warning already exists {}'
                                      .format(name))
                    self.register(name, obj())

    def reload(self, ):
        r"""SUMMARY

        reload()

        @Return:
        """
        self.clear()
        self.load()


def predicate(obj):
    r"""SUMMARY

    predicate(obj)

    @Arguments:
    - `obj`:

    @Return:
    """
    return (inspect.isclass(obj) and
            issubclass(obj, PluginAbstract) and
            obj != PluginAbstract)


def parse_plugins(module):
    r"""SUMMARY

    list_extclass(module)

    @Arguments:
    - `module`:

    @Return:
    """
    for name, obj in inspect.getmembers(module, predicate=predicate):
        yield name, obj


def load_plugins(path, dic=None):
    r"""SUMMARY

    load_plugins(path)

    @Arguments:
    - `path`:

    @Return:
    """
    dic = dic or {}
    for file_ in pyutil.iter_pyfiles(path):
        if file_.endswith(('.pyc')) or file_ == '__init__.py':
            continue
        mod = imp.load_source(
            PathHandler(file_).get_basename().splitext()[0], file_)
        for name, obj in parse_plugins(mod):
            if name in dic:
                import warnings
                warnings.warn('Plugin Warning already exists {}'.format(name))
            dic[name] = obj()
    return dic


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# core.py ends here
