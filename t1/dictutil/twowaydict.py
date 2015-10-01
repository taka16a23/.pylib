#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""twowaydict -- Two way dictionary.

"""
from pprint import pformat

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class TwoWayDict(dict):
    r"""TwoWayDict

    TwoWayDict is a dict.
    Responsibility:
    """
    def __init__(self, dict_=None, **kwargs):
        r"""

        @Arguments:
        - `dict_`:
        - `kwargs`:
        """
        super(TwoWayDict, self).__init__()
        if dict_ is not None:
            self.update(dict_)
        if len(kwargs):
            self.update(kwargs)

    def update(self, dict_=None, **kwargs):
        r"""SUMMARY

        update(dict_=None, **kwargs)

        @Arguments:
        - `dict_`:
        - `kwargs`:

        @Return:

        @Error:
        """
        if dict_ is None:
            pass
        elif isinstance(dict_, self.__class__):
            super(TwoWayDict, self).update(dict_)
        elif isinstance(dict_, dict):
            for key, value in dict_.iteritems():
                self[key] = value
        else:
            # if (('key', 1), ('key2', 2)), and so on
            self.update(dict(dict_)) # recursive call
        if len(kwargs):
            self.update(kwargs) # recursive call

    def __setitem__(self, key, val):
        super(TwoWayDict, self).__setitem__(key, val)
        super(TwoWayDict, self).__setitem__(val, key)

    def __delitem__(self, key):
        super(TwoWayDict, self).__delitem__(self[key])
        if key in self:
            super(TwoWayDict, self).__delitem__(key)

    def truelen(self, ):
        r"""SUMMARY

        truelen()

        @Return:

        @Error:
        """
        return super(TwoWayDict, self).__len__()

    def pop(self, key, *args):
        r"""SUMMARY

        pop(key, *args)

        @Arguments:
        - `key`:
        - `args`:

        @Return:

        @Error:
        """
        value = super(TwoWayDict, self).pop(key, *args)
        return value, super(TwoWayDict, self).pop(value, *args)

    def popitem(self, ):
        r"""SUMMARY

        popitem()

        @Return:

        @Error:
        """
        key, value = super(TwoWayDict, self).popitem()
        super(TwoWayDict, self).__delitem__(value)
        return key, value

    def __len__(self):
        return self.truelen() // 2

    def __repr__(self):
        return '{0.__class__.__name__}({1})'.format(
            self, pformat(dict(self)))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# twowaydict.py ends here
