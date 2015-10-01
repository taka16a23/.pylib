#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_pieces -- DESCRIPTION

"""
from wxcb.xobj.buttoncode import Buttoncode
from wxcb.xobj.keycode import Keycode
from xsendkey.obj.modifiers import Modifiers


class XPieces(object):
    r"""XPieces

    XPieces is a object.
    Responsibility:
    """

    def __init__(self, modifier):
        r"""

        @Arguments:
        - `modifier`:
        """
        self._modifier = Modifiers(modifier)

    def set_modifier(self, mod):
        """function set_modifier

        mod: int

        returns None
        """
        self._modifier.set(mod)

    def get_modifier(self):
        """function get_modifier

        returns Modifier
        """
        return self._modifier

    def add_modifier(self, mod):
        r"""SUMMARY

        add_modifier(mod)

        @Arguments:
        - `mod`:

        @Return:

        @Error:
        """
        self._modifier.add(mod)

    def remove_modifier(self, mod):
        r"""SUMMARY

        remove_modifier(mod)

        @Arguments:
        - `mod`:

        @Return:

        @Error:
        """
        self._modifier.remove(mod)

    def clear_modifier(self, ):
        r"""SUMMARY

        clear_modifier()

        @Return:

        @Error:
        """
        self._modifier.clear()

    def ismodified(self, mod):
        r"""SUMMARY

        isflaged(mod)

        @Arguments:
        - `mod`:

        @Return:

        @Error:
        """
        return self._modifier.isflaged(mod)

    def __iand__(self, other):
        if isinstance(other, (self.__class__, )):
            self.set_modifier(self._modifier & other.get_modifier())
        else:
            self.set_modifier(self._modifier & other)
        return self

    def __ixor__(self, other):
        if isinstance(other, (self.__class__, )):
            self.set_modifier(self._modifier ^ other.get_modifier())
        else:
            self.set_modifier(self._modifier ^ other)
        return self

    def __ior__(self, other):
        if isinstance(other, (self.__class__, )):
            self.set_modifier(self._modifier | other.get_modifier())
        else:
            self.set_modifier(self._modifier | other)
        return self

    def __ilshift__(self, other):
        self.set_modifier(self._modifier << other)
        return self

    def __irshift__(self, other):
        self.set_modifier(self._modifier >> other)
        return self


class XKey(XPieces):
    r"""XKey

    XKey is a XPieces.
    Responsibility:
    """
    def __init__(self, code, modifier=0):
        r"""

        @Arguments:
        - `code`:
        - `modifier`:
        """
        XPieces.__init__(self, modifier)
        self._code = Keycode(code)

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._code

    def set_code(self, code):
        r"""SUMMARY

        set_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        self._code.set(code)

    code = property(get_code, set_code)

    def __eq__(self, other):
        if isinstance(other, (self.__class__, )):
            return (self._code == other.get_code() and
                    self._modifier == other.get_modifier())
        elif isinstance(other, (tuple, list)):
            return (self._code == other[0] and self._modifier == other[1])
        return False

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return '{0.__class__.__name__}(code={1}, modifier="{2}")'.format(
            self, int(self._code), self._modifier)

    def __str__(self):
        return '({}, {})'.format(int(self._code), int(self._modifier))

    def __and__(self, other):
        if isinstance(other, (self.__class__, )):
            return self.__class__(
                self._code, self._modifier & other.get_modifier())
        return self.__class__(self._code, self._modifier & other)

    def __xor__(self, other):
        if isinstance(other, (self.__class__, )):
            return self.__class__(
                self._code, self._modifier ^ other.get_modifier())
        return self.__class__(self._code, self._modifier ^ other)

    def __or__(self, other):
        if isinstance(other, (self.__class__, )):
            return self.__class__(
                self._code, self._modifier | other.get_modifier())
        return self.__class__(self._code, self._modifier | other)

    def __lshift__(self, other):
        return self.__class__(self._code, self._modifier << other)

    def __rshift__(self, other):
        return self.__class__(self._code, self._modifier >> other)


class XButton(XPieces):
    r"""XButton

    XButton is a XPieces.
    Responsibility:
    """
    def __init__(self, code, modifiers=0):
        r"""

        @Arguments:
        - `code`:
        - `modifiers`:
        """
        super(XButton, self).__init__(modifiers)
        self._code = Buttoncode(code)

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._code

    def set_code(self, code):
        r"""SUMMARY

        set_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        self._code.set(code)

    code = property(get_code, set_code)

    def __eq__(self, other):
        if isinstance(other, (self.__class__, )):
            return (self._code == other.get_code() and
                    self._modifier == other.get_modifier())
        elif isinstance(other, (tuple, list)):
            return (self._code == other[0] and self._modifier == other[1])
        return False

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return '{0.__class__.__name__}(code={1}, modifier={2})'.format(
            self, int(self._code), int(self._modifier))

    def __str__(self):
        return '({}, {})'.format(int(self._code), int(self._modifier))

    def __and__(self, other):
        if isinstance(other, (self.__class__, )):
            mod = self._modifier & other.get_modifier()
            return self.__class__(self._code, mod)
        return self.__class__(self._code, self._modifier & other)

    def __xor__(self, other):
        if isinstance(other, (self.__class__, )):
            return self.__class__(
                self._code, self._modifier ^ other.get_modifier())
        return self.__class__(self._code, self._modifier ^ other)

    def __or__(self, other):
        if isinstance(other, (self.__class__, )):
            return self.__class__(
                self._code, self._modifier | other.get_modifier())
        return self.__class__(self._code, self._modifier | other)

    def __lshift__(self, other):
        return self.__class__(self._code, self._modifier << other)

    def __rshift__(self, other):
        return self.__class__(self._code, self._modifier >> other)




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _pieces.py ends here
