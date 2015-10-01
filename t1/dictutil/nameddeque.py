#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""nameddeque -- DESCRIPTION

"""
import sys as _sys
import os as _os

from pythonutils import OrderedDict

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class NamedDeque(OrderedDict):
    r"""SUMMARY
    """

    def appendright(self, key, value):
        r"""SUMMARY

        append(key, value)

        @Arguments:
        - `key`:
        - `value`:

        @Return:
        """
        self[key] = value

    def appendleft(self, key, value):
        r"""SUMMARY

        appendleft(key, value)

        @Arguments:
        - `key`:
        - `value`:

        @Return:
        """
        self.insert(0, key, value)

    def count(self, ):
        r"""SUMMARY

        count()

        @Return:
        """
        return len(self._dict)

    def extendright(self, dict_):
        r"""SUMMARY

        extend_dict(items)

        @Arguments:
        - `items`:

        @Return:
        """
        if not hasattr(dict_, 'iteritems'):
            raise StandardError()
        for key, value in dict_.iteritems():
            self[key] = value

    def extendleft(self, dict_):
        r"""SUMMARY

        extendleft()

        @Return:
        """
        if not hasattr(dict_, 'iteritems'):
            raise StandardError()
        for key, value in dict_.iteritems():
            self.appendleft(key, value)

    def popright(self, ):
        r"""SUMMARY

        pop()

        @Return:
        """
        if not self:
            raise StandardError()
        return self.pop(self.keys()[-1])

    def popleft(self, ):
        r"""SUMMARY

        popleft()

        @Return:
        """
        if not self:
            raise StandardError()
        return self.pop(self.keys()[0])

    def remove(self, key):
        r"""SUMMARY

        remove()

        @Return:
        """
        self.pop(key)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# nameddeque.py ends here
