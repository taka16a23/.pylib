#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""avoider -- DESCRIPTION

list, append = DotAvoider(list()).append

"""

__all__ = ['DotAvoider', 'ListDotAvoider', 'dotavoid']


def dotavoid(obj, *method):
    r"""SUMMARY

    dotavoider(obj, *method)

    @Arguments:
    - `obj`:
    - `method`:

    @Return:

    @Error:
    """
    return [obj] + [getattr(obj, mthd) for mthd in method]


class DotAvoidAttributeError(AttributeError):
    r"""DotAvoiderAttributeError

    Responsibility:
    """
    pass


class DotAvoider(object):
    r"""SUMMARY
    """

    def __init__(self, obj):
        r"""

        @Arguments:
        - `obj`:
        """
        self._obj = obj

    def __getattr__(self, attr):
        r"""SUMMARY

        __getattr__(attr)

        @Arguments:
        - `name`:

        @Return:
        """
        return self._obj, self.getattribute(attr)

    def getattribute(self, attr):
        r"""SUMMARY

        getattribute(attr)

        @Arguments:
        - `attr`:

        @Return:

        @Error:
        DotAvoidAttributeError
        """
        try:

            return getattr(self._obj, attr)
        except AttributeError as err:
            raise DotAvoidAttributeError(str(err))

    def getattributes(self, *args):
        r"""SUMMARY

        getattributes(*args)

        @Arguments:
        - `args`:

        @Return:
        """
        lis = list()
        append = lis.append
        for attr in args:
            append(self.getattribute(attr))
        return (self._obj, ) + tuple(lis)


class ListDotAvoider(DotAvoider):
    r"""SUMMARY
    """

    def __init__(self, initlist=None):
        r"""

        @Arguments:
        - `initlist`:
        """
        super(ListDotAvoider, self).__init__(initlist or list())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# avoider.py ends here
