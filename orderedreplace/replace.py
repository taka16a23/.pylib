#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: replace.py 272 2015-01-10 05:40:25Z t1 $
# $Revision: 272 $
# $Date: 2015-01-10 14:40:25 +0900 (Sat, 10 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-10 14:40:25 +0900 (Sat, 10 Jan 2015) $

r"""oerderedreplace -- DESCRIPTION

"""
import re as _re
from collections import OrderedDict as _OrderedDict


class NewArguments(object):
    r"""NewArguments

    NewArguments is a object.
    Responsibility:
    Informetion holder for `str.replace'.
    """
    __slots__ = ('new', 'count')

    def __init__(self, new, count=0):
        r"""

        @Arguments:
        - `new`:
        - `count`:
        """
        self.new = new
        self.count = count

    def get_new(self, ):
        r"""SUMMARY

        get_new()

        @Return:

        @Error:
        """
        return self.new

    def set_new(self, new):
        r"""SUMMARY

        set_new(new)

        @Arguments:
        - `new`:

        @Return:

        @Error:
        """
        if not isinstance(new, (basestring, )):
            # TODO: (Atami) [2015/01/07]
            raise TypeError(new)
        self.new = new

    def get_count(self, ):
        r"""SUMMARY

        get_count()

        @Return:

        @Error:
        """
        return self.count

    def set_count(self, count):
        r"""SUMMARY

        set_count(count)

        @Arguments:
        - `count`:

        @Return:

        @Error:
        """
        if not isinstance(count, (int, )):
            # TODO: (Atami) [2015/01/07]
            raise TypeError(count)
        self.count = count

    def __repr__(self):
        return ('{0.__class__.__name__}(new="{0.new}", count={0.count})'
                .format(self))


class OrderedReplace(object):
    r"""OrderedReplace

    OrderedReplace is a OrderedDict.
    Responsibility:
    """
    def __init__(self, dict_=None, **kwargs):
        r"""

        @Arguments:
        - `dict_`:
        - `kwargs`:
        """
        self._dict = _OrderedDict()
        if dict_ or kwargs:
            self.update(dict_, **kwargs)

    def replace(self, text):
        r"""SUMMARY

        replace(text)

        @Arguments:
        - `text`:

        @Return:

        @Error:
        """
        if not isinstance(text, str):
            # TODO: (Atami) [2014/10/25]
            raise TypeError()
        line = text
        for rx, new in self.iteritems():
            line = rx.sub(new.get_new(), line, new.get_count())
        return line

    def set(self, old, new, count=None):
        r"""SUMMARY

        set(old, new, count=None)

        @Arguments:
        - `old`:
        - `new`:
        - `count`:

        @Return:

        @Error:
        """
        if isinstance(new, (NewArguments, )):
            self[old] = new
        else:
            self[old] = (new, count)

    def __setitem__(self, key, new, prev=0, next_=1):
        if isinstance(new, (NewArguments, )):
            newarg = new
        elif isinstance(new, (str, )):
            newarg = NewArguments(new)
        elif isinstance(new, (tuple, list)) and 2 <= len(new):
            newarg = NewArguments(new[0], new[1])
        self._dict.__setitem__(_re.compile(key), newarg, prev, next_)

    def __getitem__(self, key):
        return self._dict[_re.compile(key)]

    def __delitem__(self, key, prev=0, next_=1):
        self._dict.__delitem__(_re.compile(key))

    def update(self, dict_=None, **kwargs):
        r"""SUMMARY

        update(dict_=None, **kwargs)

        @Arguments:
        - `dict_`:
        - `kwargs`:

        @Return:

        @Error:
        """
        if isinstance(dict_, (self.__class__, dict)):
            for key, value in dict_.iteritems():
                self[key] = value
        else:
            # if (('key', 1), ('key2', 2)), and so on
            self.update(_OrderedDict((dict_))) # recursive call
        if len(kwargs):
            self.update(kwargs)

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._dict.clear()

    def keys(self, ):
        r"""SUMMARY

        keys()

        @Return:

        @Error:
        """
        return self._dict.keys()

    def values(self, ):
        r"""SUMMARY

        values()

        @Return:

        @Error:
        """
        return self._dict.values()

    def items(self, ):
        r"""SUMMARY

        items()

        @Return:

        @Error:
        """
        return self._dict.items()

    def iterkeys(self, ):
        r"""SUMMARY

        iterkeys()

        @Return:

        @Error:
        """
        return self._dict.iterkeys()

    def itervalues(self, ):
        r"""SUMMARY

        itervalues()

        @Return:

        @Error:
        """
        return self._dict.itervalues()

    def iteritems(self, ):
        r"""SUMMARY

        iteritems()

        @Return:

        @Error:
        """
        return self._dict.iteritems()

    def setdefault(self, key, default, count=None):
        r"""SUMMARY

        setdefault(key, default)

        @Arguments:
        - `key`:
        - `default`:

        @Return:

        @Error:
        """
        if key in self:
            return self[key]
        self.set(key, default, count)
        return self[key]

    def __contains__(self, el):
        return _re.compile(el) in self._dict

    def __repr__(self):
        return '{0.__class__.__name__}({1})'.format(
            self, [(rxp.pattern, repl) for rxp, repl in self._dict.iteritems()])

    def copy(self, ):
        r"""SUMMARY

        copy()

        @Return:

        @Error:
        """
        return self.__class__(self._dict)

    def __len__(self):
        return len(self._dict)

    def __call__(self, text):
        return self.replace(text)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# oerderedreplace.py ends here
