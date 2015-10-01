#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 236 2014-11-28 17:01:47Z t1 $
# $Revision: 236 $
# $Date: 2014-11-29 02:01:47 +0900 (Sat, 29 Nov 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-11-29 02:01:47 +0900 (Sat, 29 Nov 2014) $

r"""Name: __init__.py


0.1.1: Append function `recursive_update'.

"""
from collections import namedtuple, Mapping
from t1.dictutil.nameddeque import NamedDeque
from t1.dictutil.sortdict import SortedDict, ValueSortedDict
from t1.dictutil.orderdict import OrderDict
from t1.dictutil.twowaydict import TwoWayDict


__revision__ = "$Revision: 236 $"
__version__ = "0.1.3"

__all__ = ['DictUtil', 'swapdict', 'dict_to_namedtuple', 'recursive_update',
           'NamedDeque', 'OrderDict', 'TwoWayDict', ]


class DictUtil(dict):
    r"""My dictionary util.

    inherited from builtins `dict'
    """

    def set_all_value(self, value=None):
        r"""SUMMARY

        set_all_value(value=None)

        @Arguments:
        - `value`:

        @Return:
        """
        for key in list(self.iterkeys()): # excape RuntimeError by list
            self[key] = value

    def rename(self, old, new, override=False):
        r"""Rename key.

        @Arguments:
        - `old`: old key name.
        - `new`: new key name.
        - `override`: type(bool) Allow override if exists key.

        @Return:
        None

        rename(old, new)
        rename key old to new.
        """
        if not override and new in self:
            raise ValueError('{} is exists. Set override=True.')

        self[new] = self.get(old)
        del self[old]

    def swap(self, ):
        r"""Swap keys for values in a dictionary.

        swap()

        @Return:
        DictUtil(dict)
        """
        return self.__class__(swapdict(self))


def swapdict(dic):
    r"""Swap keys for values in a dictionary.

    swapdict(dic)

    @Arguments:
    - `dic`: dictionary object

    @Return:
    dict

    >>> d = {'a':1}
    >>> swapdict(d)
    {1:'a'}
    """
    return dict(zip(dic.values(), dic.keys()))


def dict_to_namedtuple(name, dic):
    r"""SUMMARY

    dict_to_namedtupel(dic)

    @Arguments:
    - `dic`:

    @Return:
    """
    ntuple = namedtuple(name, dic.keys())
    return ntuple(**dic)


def recursive_update(adict, bdict):
    """Recursive update dictionary

    @Arguments:
    - `adict`: base dictionary.
    - `bdict`: parsable dictionary.

    @Return:
    adict
    """
    # import pdb; pdb.set_trace()
    for key, value in bdict.iteritems():
        if isinstance(value, Mapping):
            ret = recursive_update(adict.get(key, adict.__class__()), value)
            adict[key] = ret
        else:
            adict[key] = bdict[key]
    return adict



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
