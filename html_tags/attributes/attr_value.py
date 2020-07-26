#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""attr_value -- attribute value class

"""
from django.utils.safestring import mark_safe
from .base_attr_value import BaseAttrValue


class AttrValue(BaseAttrValue):
    """AttrValue

    AttrValue is a BaseAttrValue.
    Responsibility:
    """
    def __init__(self, values=None):
        self.values = set()
        if values is None:
            return
        if isinstance(values, (str, )):
            self.values.update(set(values.split(' ')))
            if '' in self.values:
                self.values.remove('')
            return
        self.values.update(set(values))
        if '' in self.values:
            self.values.remove('')

    def set(self, values):
        """set values.

        set(values)

        @Arguments:
        - `values`: リストか' ' 区切り文字列

        @Return: 自身のインスタンス

        @Error:

        TypeError: argument must be str or iterable.
        """
        if values is None:
            raise TypeError('values must be str or iterable. got(None)')
        if isinstance(values, (str, )):
            self.values.update(set(values.split(' ')))
            if '' in self.values:
                self.values.remove('')
            return self
        self.values.update(set(values))
        if '' in self.values:
            self.values.remove('')
        return self

    def list(self, ):
        """List values.

        list()

        @Return:

        @Error:
        """
        return list(self.values)

    def remove(self, value):
        """Remove class value.

        remove(value)

        @Arguments:
        - `value`: 属性の値

        @Return:

        @Error:
        """
        if value in self.values:
            self.values.remove(value)
        return self

    def contains(self, value):
        """Check Contains value.

        contains(value)

        @Arguments:
        - `value`: class value

        @Return:

        @Error:
        """
        return value in self.values

    def clear(self, ):
        """Clear values.

        clear()

        @Return:

        @Error:
        """
        self.values.clear()
        return self

    def as_values(self, ):
        """Generate class values.

        as_values()

        @Return: (str) attribute values

        @Error:
        """
        return mark_safe(' '.join(list(self.values)))

    def __str__(self):
        return self.as_values()

    def __repr__(self):
        return '{0.__class__.__name__}("{0}")'.format(self)

    def __iter__(self):
        return iter(self.values)

    def __add__(self, other):
        ls = self.list()
        if isinstance(other, (str, )):
            ls.extend(other.split(' '))
            return AttrValue(ls)
        ls.extend(other)
        return AttrValue(ls)

    def __iadd__(self, other):
        self.set(other)
        return self

    def __len__(self):
        return len(self.values)

    def __contains__(self, elm):
        return self.contains(elm)

    def __eq__(self, other):
        t_this_values = list(self.values)
        t_this_values.sort()
        t_other_values = str(other).split(' ')
        t_other_values.sort()
        return t_this_values == t_other_values

    def __ne__(self, other):
        return not self == other



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# attribute.py ends here
