#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""only_one_attr_value -- hold one attribute value like id.

"""
from .attr_value import AttrValue


class OnlyOneAttrValue(AttrValue):
    """OnlyOneAttrValue

    OnlyOneAttrValue is a Attribute.
    Responsibility:

    html tag attribute for only one value.
    Like id="element1"
    """
    def __init__(self, value=None):
        super(OnlyOneAttrValue, self).__init__(value)
        if 2 <= len(self.values):
            raise ValueError('value must be one value. got({})'.format(value))

    # override
    def set(self, value):
        """Set value.

        set()

        @Return:

        @Error:
        """
        self.clear()
        super(OnlyOneAttrValue, self).set(value)
        if 2 <= len(self.values):
            raise ValueError('value must be one value. got({})'.format(value))
        return self

    #override
    def remove(self, value):
        """Remove value.

        remove(value)

        @Return:

        @Error:
        """
        if value in self.values:
            super(OnlyOneAttrValue, self).remove(value)
        return self

    def __add__(self, other):
        t_attribute = OnlyOneAttrValue(str(self))
        t_attribute.set(other)
        return t_attribute

    def __iadd__(self, other):
        self.set(other)
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# only_one_attr_value.py ends here
