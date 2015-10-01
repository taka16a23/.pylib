#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from predicate import islist
from t1.listutil.sortlist import SortedList
from t1.listutil.onetypelist import OneTypeList


__version__ = "0.1.0"

__all__ = ['ListUtil', 'nth', 'flatten', 'init_list',
           'all_pair', 'get_first_index', 'SortedList']


class ListUtil(list):
    r"""
    """

    def __init__(self, value, default=None):
        r"""SUMMARY

        __init__(value, default)

        @Arguments:
        - `value`:
        - `default`:

        @Return:
        """
        list.__init__(self, value)
        self._default = default

    def __getitem__(self, val):
        r"""Return by getitem operator.

        If catched IndexError, then return default value.
        """
        try:
            return super(ListUtil, self).__getitem__(val)
        except IndexError:
            return self._default

    def setdefault(self, val):
        r"""SUMMARY

        setdefault(val)

        @Arguments:
        - `val`:

        @Return:
        """
        self._default = val

    def nth(self, num):
        r"""SUMMARY

        nth(nth)

        @Arguments:
        - `nth`:

        @Return:
        """
        return nth(self, num)

    def flatten(self, ):
        r"""SUMMARY

        flatten()

        @Return:
        """
        # TODO: (Atami) [2014/10/01]
        # refactoring
        self[:] = list(flatten(self))

    def chunks(self, size):
        r"""Split list into chunks of equal size.

        chunks(size)

        @Arguments:
        - `size`: size of chunks

        >>> lis=ListUtil((1,2,3,4,5,6,7,8,9))
        >>> lis.chunks(3)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> lis.chunks(2)
        [[1, 2], [3, 4], [5, 6], [7, 8]]

        @Return:
        ListUtil
        """
        self.flatten()
        if size == 0:
            return
        if size < 0:
            # TODO: (Atami) [2014/10/02]
            raise ValueError(size)
        self[:] = [ListUtil(x) for x in zip(*[iter(self)] * size)]


def nth(elements, nth):
    r"""Return list from nested.

    @Arguments:
    - `elements`: nested list
    - `nth`: type(int)

    @Return:
    list

    nth(elements, nth)
    """
    return [x[nth] for x in elements]


# borrow and modified from
# http://stackoverflow.com/questions/10823877/what-is-the-fastest-way-to-flatten-arbitrarily-nested-lists-in-python#answer-10824420
def flatten(container, seqtypes=(list, tuple)):
    r"""SUMMARY

    flatten(container, seqtypes=(list, tuple))

    @Arguments:
    - `container`:
    - `seqtypes`:
    - `tuple)`:

    @Return:
    """
    for i in container:
        if isinstance(i, seqtypes):
            for j in flatten(i):
                yield j
        else:
            yield i


def init_list(*args):
    r"""SUMMARY

    init_list(*args)

    @Arguments:
    - `*args`:

    @Return:
    """
    list_ = []
    result = [getattr(list_, x) for x in args]
    result.insert(0, list_)
    return result


def all_pair(lis):
    r"""SUMMARY

    all_pair(lis)

    @Arguments:
    - `lis`:

    @Return:
    """
    for item1 in lis:
        for item2 in lis:
            yield (item1, item2)


def get_first_index(iterable):
    r"""Get first index as safety.

    get_first_index(iterable)

    # same code
    if not iterable:
        return None
    return iterable[0]

    @Arguments:
    - `iterable`:

    @Return:
    """
    for elm in iterable:
        return elm
    return None



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
