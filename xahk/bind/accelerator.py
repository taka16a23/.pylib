#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""accelerator -- DESCRIPTION

"""
from xahk.x11.modifier import Modifier
from xahk.input.keyboard import Keyboard


class Accelerator(object):
    """Class Accelerator"""
    # Attributes:
    __slots__ = ('code', 'modifiers')

    def __init__(self, code, modifiers=Modifier.Mask.Null):
        """

        @Arguments:
        - `code`:
        - `modifier`:
        """
        self.code = code
        self.modifiers = Modifier(modifiers)

    # Operations
    @classmethod
    def from_key_label(cls, label, modifiers=Modifier.Mask.Null):
        """SUMMARY

        from_key_label(label, modifiers=Modifier.Mask.Null)

        @Arguments:
        - `label`:
        - `modifiers`:

        @Return:

        @Error:
        """
        keyboard = Keyboard()
        key = keyboard.get_key(label)
        if key is None:
            # TODO: (Atami) [2016/05/29]
            raise StandardError()
        if label == key.get_shift_label():
            modifiers |= Modifier.Mask.Shift
        return cls(key.get_code(), modifiers)

    def get_code(self):
        """function get_code

        returns
        """
        return self.code

    def get_modifiers(self):
        """function get_modifiers

        returns
        """
        return self.modifiers

    def set_modifiers(self, modifiers):
        """SUMMARY

        set_modifiers(modifiers)

        @Arguments:
        - `modifiers`:

        @Return:

        @Error:
        """
        self.modifiers.set(modifiers)

    def __hash__(self):
        """function __hash__

        returns
        """
        return hash((self.code, self.modifiers))

    def __eq__(self, other):
        """function __eq__

        returns
        """
        if isinstance(other, (Accelerator, )):
            return ((self.code, self.modifiers) ==
                    (other.get_code(), other.get_modifiers()))
        if isinstance(other, (tuple, list)):
            return ((self.code, self.modifiers) == (other[0], other[1]))
        return False

    def __ne__(self, other):
        """function __ne__

        returns
        """
        return not self == other

    def __repr__(self):
        modifier = repr(self.modifiers).replace(
            self.modifiers.__class__.__name__, '')
        return ('{0.__class__.__name__}'
                '(code={0.code}, modifiers={1})'.format(self, modifier))

    def __or__(self, other):
        return Accelerator(self.code, self.modifiers|other)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# accelerator.py ends here
