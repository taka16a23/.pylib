#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""orderdict -- DESCRIPTION

"""

class OrderDict(dict):
    r"""SUMMARY
    """

    def __init__(self, orderkeys, dict_=None, **kwargs):
        r"""

        @Arguments:
        - `orderkeys`:
        - `dict_`:
        - `kwargs`:
        """
        dict.__init__(self, )
        self._orderkeys = tuple(orderkeys)
        if not dict_ is None:
            self.update(dict_)
        if kwargs:
            self.update(kwargs)

    def __setitem__(self, key, item):
        if not key in self._orderkeys:
            # TODO: (Atami) [2014/06/17]
            raise StandardError('orderkeys error')
        super(OrderDict, self).__setitem__(key, item)

    def keys(self, ):
        r"""SUMMARY

        keys()

        @Return:
        """
        return [key for key in self._orderkeys if key in self]

    def items(self, ):
        r"""SUMMARY

        items()

        @Return:
        """
        return [(key, self[key]) for key in self._orderkeys if key in self]

    def iteritems(self, ):
        r"""SUMMARY

        iteritems()

        @Return:
        """
        for key in self._orderkeys:
            if key in self._orderkeys:
                yield (key, self[key])
        raise StopIteration()

    def iterkeys(self, ):
        r"""SUMMARY

        iterkeys()

        @Return:
        """
        for key in self._orderkeys:
            if key in self._orderkeys:
                yield key
        raise StopIteration()

    def itervalues(self, ):
        r"""SUMMARY

        itervalues()

        @Return:
        """
        for key in self._orderkeys:
            if key in self._orderkeys:
                yield self[key]
        raise StopIteration()

    def values(self, ):
        r"""SUMMARY

        values()

        @Return:
        """
        return [self[key] for key in self._orderkeys if key in self]

    def update(self, dict_=None, **kwargs):
        r"""SUMMARY

        update(dict_=None, **kwargs)

        @Arguments:
        - `dict_`:
        - `kwargs`:

        @Return:
        """
        if dict_ is None:
            pass
        else:
            for k, v in dict_.items():
                self[k] = v
        if len(kwargs):
            self.update(kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# orderdict.py ends here
