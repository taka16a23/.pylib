#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""accelerator -- DESCRIPTION

"""


class Accelerator(object):
    """Class Accelerator
    """
    # Attributes:
    __slots__ = ('_code', '_modifiers')

    def __init__(self, code, modifiers=0):
        r"""

        @Arguments:
        - `code`:
        - `modifier`:
        """
        self._code = code
        self._modifiers = modifiers

    # Operations
    def get_code(self):
        """function get_code

        returns
        """
        return self._code

    def get_modifiers(self):
        """function get_modifiers

        returns
        """
        return self._modifiers

    def is_shift_down(self):
        """function is_shift_down

        returns
        """
        return None # should raise NotImplementedError()

    def is_ctrl_down(self):
        """function is_ctrl_down

        returns
        """
        return None # should raise NotImplementedError()

    def is_alt_down(self):
        """function is_alt_down

        returns
        """
        return None # should raise NotImplementedError()

    def __hash__(self):
        """function __hash__

        returns
        """
        return hash((self._code, self._modifiers))

    def __eq__(self, other):
        """function __eq__

        returns
        """
        return ((self._code, self._modifiers) ==
                (other.get_code(), other.get_modifiers()))

    def __ne__(self, other):
        """function __ne__

        returns
        """
        return not self == other

    def __repr__(self):
        return ('{0.__class__.__name__}'
                '(code={0._code}, modifiers={0._modifiers})'.format(self))

    def __or__(self, other):
        return Accelerator(self._code, self._modifiers|other)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# accelerator.py ends here
