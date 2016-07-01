#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""key_accelerator_builder -- DESCRIPTION

"""
from xahk.x11.modifier import Modifier
from xahk.input.keyboard import Keyboard
from xahk.bind.accelerator import Accelerator


class KeyAcceleratorBuilder(object):
    r"""KeyAccleratorBuilder

    KeyAcceleratorBuilder is a object.
    Responsibility:
    """
    def __init__(self, code):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.code = code
        self.modifiers = Modifier.Mask.Null

    @classmethod
    def from_key_label(cls, label):
        """SUMMARY

        from_key_label(label)

        @Arguments:
        - `label`:

        @Return:

        @Error:
        """
        keyboard = Keyboard()
        key = keyboard.get_key(label)
        if key is None:
            # TODO: (Atami) [2016/05/29]
            raise StandardError()
        builder = cls(key.get_code())
        if label == key.get_shift_label():
            builder = builder.set_modifiers(Modifier.Mask.Shift)
        return builder

    def set_modifiers(self, modifiers):
        """SUMMARY

        set_modifiers(modifiers)

        @Arguments:
        - `modifiers`:

        @Return:

        @Error:
        """
        self.modifiers = modifiers
        return self

    def get_modifeirs(self, ):
        """SUMMARY

        get_modifeirs()

        @Return:

        @Error:
        """
        return self.modifiers

    def add_modifiers(self, modifiers):
        """SUMMARY

        add_modifiers(modifiers)

        @Arguments:
        - `modifiers`:

        @Return:

        @Error:
        """
        self.modifiers |= modifiers
        return self

    def build(self, ):
        """SUMMARY

        build()

        @Return:

        @Error:
        """
        return Accelerator(self.code, self.modifiers)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# key_accelerator_builder.py ends here
