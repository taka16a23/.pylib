#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""attributes -- Attributes class

"""
from _collections_abc import Mapping
from collections import UserDict

from .attr_value import AttrValue


class Attributes(UserDict):
    """Attributes

    Attributes is a UserDict.
    Responsibility:
    """
    # for attrbute name only
    NONE_VALUE = None

    def set_value(self, name, value):
        """Set attribute value.

        set(name, value)

        @Arguments:
        - `name`: attribute name
                 like <span class="val"> class is this name.
        - `value`: attribute value
                 like <span class="val"> val is this value.

        @Return: this instance

        @Error:
        """
        if value is None:
            self[name] = None
            return self
        self[name] = AttrValue(value)
        return self

    def append_value(self, name, value):
        """Append attribute value.

        append_value(name, value)

        @Arguments:
        - `name`: attribute name
        - `value`: 'a b c' or ['a', 'b', 'c',] or AttrValue

        @Return: this instance

        @Error:
        """
        if name not in self or self[name] is None:
            self[name] = AttrValue()
        self[name] += value
        return self

    def remove_value(self, name, value):
        """Remove attribute value.

        remove_value(name, value)

        @Arguments:
        - `name`: attribute name
        - `value`: 'a b c' or ['a', 'b', 'c',] or AttrValue

        @Return: this instance

        @Error:
        """
        if name in self and isinstance(self[name], AttrValue):
            self[name].remove(value)
        return self

    def clear_value(self, name):
        """Clear attribute values.

        clear_value(name)

        @Arguments:
        - `name`: attribute name

        @Return: this instance

        @Error:
        """
        if name in self and isinstance(self[name], AttrValue):
            self[name].clear()
        return self

    def remove_attribute(self, name):
        """Remove attribute value.

        remove_attribute(name)

        @Arguments:
        - `name`: attribute name

        @Return: this instance

        @Error:
        """
        if name in self:
            del self[name]
        return self

    def set_none(self, name):
        """Set None.

        set_none(name)

        @Arguments:
        - `name`: attribute name

        for attribute name only like this.
        <option selected>

        @Return: this instance

        @Error:
        """
        self[name] = self.NONE_VALUE
        return self

    def get_value(self, name):
        """Get attribute value.

        get_value(name)

        @Arguments:
        - `name`: attribute name

        @Return: attribute value if exists. None if not exists.

        @Error:
        """
        if name in self:
            return self[name]
        return None

    def contains_value(self, name, value):
        """Determin contain value.

        contains_value(value)

        @Arguments:
        - `name`: attribute name
        - `value`: attribute value

        @Return: True if exists value in name. else False.

        @Error:
        """
        if name not in self:
            return False
        if self[name] is None:
            return False
        return self[name].contains(value)

    def update(*args, **kwds):
        if not args:
            raise TypeError("descriptor 'update' of 'MutableMapping' object "
                            "needs an argument")
        self, *args = args
        if len(args) > 1:
            raise TypeError('update expected at most 1 arguments, got %d' %
                            len(args))
        if args:
            other = args[0]
            if isinstance(other, (self.__class__, )):
                for key in other:
                    self[key] = other[key]
            elif isinstance(other, Mapping):
                for key in other:
                    self[key] = AttrValue(other[key])
            elif hasattr(other, "keys"):
                for key in other.keys():
                    self[key] = AttrValue(other[key])
            else:
                for key, value in other.items():
                    self[key] = AttrValue(value)
        for key, value in kwds.items():
            self[key] = AttrValue(value)

    def setdefault(self, key, default=None):
        return super(Attributes, self).setdefault(key, AttrValue(default))

    def __setitem__(self, key, val):
        if isinstance(val, (AttrValue, )) == True:
            super(Attributes, self).__setitem__(str(key), val)
            return
        if val is None:
            super(Attributes, self).__setitem__(str(key), None)
            return
        super(Attributes, self).__setitem__(str(key), AttrValue(val))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# attributes.py ends here
