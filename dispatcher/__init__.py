#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 136 2014-04-05 08:42:53Z t1 $
# $Revision: 136 $
# $Date: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $

r"""Name: __init__.py


"""
from collections import Mapping

from predicate import iscallable, isclass
from inspect import getargspec
import warnings
from UserDict import UserDict
from abc import abstractmethod, ABCMeta

from predicate import isiterable


__revision__ = "$Revision: 136 $"
__version__ = "0.1.0"

__all__ = [ 'Dispatcher' ]

class NotCallableError(StandardError):
    r"""
    """
    pass


class FuncParamError(Exception):
    r"""
    """

    def __init__(self, value):
        r"""

        @Arguments:
        - `value`:
        """
        self._value = value


class DispatcherAbstract(Mapping):
    r"""SUMMARY
    """

    _missing_func = lambda *args, **kwargs: None

    def __init__(self, dict_=None, **kwargs):
        r"""
        """
        self._data = {}
        if dict_ is not None:
            self.update(dict_)
        if len(kwargs):
            self.update(kwargs)

    def unregister(self, key):
        r"""SUMMARY

        unregister(key)

        @Arguments:
        - `key`:

        @Return:
        """
        if key in self:
            del self[key]

    def register_missing_func(self, func):
        r"""SUMMARY

        register_missing_func(func)

        @Arguments:
        - `func`:

        @Return:
        """
        if not iscallable(func):
            raise NotCallableError(func)
        self._missing_func = func

    def clear(self):
        self._data.clear()

    def update(self, dict_=None, **kwargs):
        r"""SUMMARY

        update(dict_=None,** kwargs)

        @Arguments:
        - `dict_`:
        - `** kwargs`:

        @Return:
        """
        if dict_ is not None:
            for key, value in dict_.items():
                if iscallable(value):
                    self[key] = value
                else:
                    warnings.warn('Warning Skiped: {} not callable.'
                                  .format(value))
        if len(kwargs):
            for key, value in kwargs.items():
                if iscallable(value):
                    self[key] = value
                else:
                    warnings.warn('Warning Skiped: {} not callable.'
                                  .format(value))

    def copy(self, ):
        r"""SUMMARY

        copy()

        @Return:
        """
        if self.__class__ is Dispatcher:
            return Dispatcher(self._data.copy())
        import copy
        data = self._data
        try:
            self._data = {}
            copied = copy.copy(self)
        finally:
            self._data = data
        copied.update(self)
        return copied

    def setdefault(self, key, failobj=None):
        if key not in self:
            self[key] = failobj
        return self[key]

    def keys(self):
        return self._data.keys()
    def items(self):
        return self._data.items()
    def iteritems(self):
        return self._data.iteritems()
    def iterkeys(self):
        return self._data.iterkeys()
    def itervalues(self):
        return self._data.itervalues()
    def values(self):
        return self._data.values()
    def has_key(self, key):
        return key in self._data

    def __repr__(self):
        return '{0.__class__.__name__}{0._data}'.format(self)

    def __cmp__(self, dict_):
        if isinstance(dict_, self.__class__):
            return cmp(self._data, dict_._data)
        elif isinstance(dict_, UserDict):
            return cmp(self._data, dict_.data)
        else:
            return cmp(self._data, dict_)

    __hash__ = None # Avoid Py3k warning

    def __iter__(self, ):
        return self._data.__iter__()

    def __len__(self):
        return len(self._data)

    def __contains__(self, key):
        return key in self._data

    def __missing__(self, ):
        return self._missing_func

    def __setitem__(self, key, item):
        if not iscallable(item):
            raise NotCallableError(item)
        self._data[key] = item

    def __delitem__(self, key):
        del self._data[key]

    def __call__(self, key, *args, **kwargs):
        return self[key](*args, **kwargs)


class Dispatcher(DispatcherAbstract):
    r"""
    """
    def register(self, key, func):
        r"""SUMMARY

        register(key, func)

        @Arguments:
        - `key`:
        - `func`:

        @Return:
        """
        self[key] = func

    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        return self.__missing__()


class TypeDispatcher(DispatcherAbstract):
    r"""SUMMARY
    """

    def register(self, key, func):
        r"""SUMMARY

        register(key, func)

        @Arguments:
        - `key`:
        - `func`:

        @Return:
        """
        if not isclass(key):
            # TODO: (Atami) [2014/03/10]
            raise StandardError()
        self[key] = func

    def unregister(self, key):
        r"""SUMMARY

        unregister(key)

        @Arguments:
        - `key`:

        @Return:
        """
        if key in self:
            del self[key]

    def __getitem__(self, event):
        """Get by isinstance."""
        type_ = type(event)
        if type_ in self._data:
            return self._data[type_]
        return self.__missing__()


class NotIterableError(TypeError):
    r"""
    """

    def __init__(self, obj):
        r"""

        @Arguments:
        - `obj`:
        """
        self._obj = obj

    def __str__(self, ):
        r"""SUMMARY

        __str__()

        @Return:
        """
        fmt = "'{}' object is not iterable".format
        return fmt(self._obj.__class__.__name__)


class MakeDispatchFromListABC(object):
    r"""

    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_list(self, ):
        raise NotImplementedError()

    @abstractmethod
    def get_key(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def get_callable(self, *args, **kwargs):
        raise NotImplementedError()

    def make_dispatch(self, dict_=None, **kwargs):
        r"""SUMMARY

        make_dispatch(klass)

        @Arguments:
        - `klass`:

        @Return:
        """
        dispatcher = Dispatcher(dict_, **kwargs)
        if hasattr(self, 'missing'):
            dispatcher.register_missing_func(getattr(self, 'missing'))
        for elm in self.get_list():
            dispatcher.register(self.get_key(elm),
                                self.get_callable(elm))
        return dispatcher


# class DispatchMaker(object):
#     r"""
#     """
#     _dispatcher = Dispatcher

#     def __init__(self, obj):
#         r"""SUMMARY

#         __init__(obj)

#         @Arguments:
#         - `obj`:

#         @Return:
#         """
#         if not isinstance(obj, DispatchableListABC):
#             raise ValueError()
#         self._obj = obj

#     def make_dispatch(self, dict_=None, **kwargs):
#         r"""SUMMARY

#         make_dispatch(klass)

#         @Arguments:
#         - `klass`:

#         @Return:
#         """
#         if not isinstance(self._obj, DispatchableListABC):
#             raise ValueError()
#         dispatcher = DispatchMaker._dispatcher(dict_, **kwargs)
#         for elm in self._obj.get_list():
#             dispatcher.register(self._obj.get_key(elm),
#                                 self._obj.get_value(elm))
#         return dispatcher



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
