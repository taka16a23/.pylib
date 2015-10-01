#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""onetypelist -- DESCRIPTION

"""
__version__ = '0.1.0'


class OneTypeList(list):
    r"""SUMMARY
    """
    types = object

    def __typecheck(self, item):
        r"""SUMMARY

        _typecheck(item)

        @Arguments:
        - `item`:

        @Return:
        """
        if not isinstance(item, self.types):
            # TODO: (Atami) [2014/04/30]
            raise TypeError(item)

    def __typelistcheck(self, list_):
        r"""SUMMARY

        __typelistcheck(list)

        @Arguments:
        - `list`:

        @Return:
        """
        if not isinstance(list_, self.__class__):
            for item in list_:
                self.__typecheck(item)

    def __setitem__(self, i, item):
        r"""SUMMARY

        __setitem__(i, window)

        @Arguments:
        - `i`:
        - `window`:

        @Return:
        """
        self.__typecheck(item)
        super(OneTypeList, self).__setitem__(i, item)

    def __setslice__(self, i, j, other):
        r"""SUMMARY

        __setslice__(i, j, other)

        @Arguments:
        - `i`:
        - `j`:
        - `other`:

        @Return:
        """
        self.__typelistcheck(other)
        super(OneTypeList, self).__setslice__(i, j, other)

    def __add__(self, other):
        r"""SUMMARY

        __add__(other)

        @Arguments:
        - `other`:

        @Return:
        """
        self.__typelistcheck(other)
        return super(OneTypeList, self).__add__(other)

    def __radd__(self, other):
        r"""SUMMARY

        __radd__(other)

        @Arguments:
        - `other`:

        @Return:
        """
        self.__typelistcheck(other)
        return super(OneTypeList, self).__radd__(other)

    def append(self, item):
        r"""SUMMARY

        append(item)

        @Arguments:
        - `item`:

        @Return:
        """
        self.__typecheck(item)
        super(OneTypeList, self).append(item)

    def insert(self, i, item):
        r"""SUMMARY

        insert(i, item)

        @Arguments:
        - `i`:
        - `item`:

        @Return:
        """
        self.__typecheck(item)
        super(OneTypeList, self).insert(i, item)

    def extend(self, other):
        r"""SUMMARY

        extend(other)

        @Arguments:
        - `other`:

        @Return:
        """
        self.__typelistcheck(other)
        super(OneTypeList, self).extend(other)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# onetypelist.py ends here
