#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: piece.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

import xcb2
import xcode
import modifier


class Piece(object):
    """Class Piece
    """
    # Attributes:
    def __init__(self, code, mod=0):
        r"""

        @Arguments:
        - `code`:
        - `modifier`:
        """
        self._code = xcode.KeyCode(int(code))
        self._modifier = modifier.Modifier(int(mod))

    # Operations
    def getcode(self):
        """function getcode

        returns Keycode
        """
        return self._code

    def getmodifier(self):
        """function getmodifier

        returns Modifier
        """
        return self._modifier

    def __repr__(self):
        """function __repr__

        returns
        """
        return '{0.__class__.__name__}(code={1}, modifier={2})'.format(
            self, int(self._code), int(self._modifier))

    def __str__(self):
        """function __str__

        returns
        """
        return repr(self)

    def __eq__(self, other):
        """function __eq__

        returns bool
        """
        if not isinstance(other, self.__class__):
            return False
        return (self._code == other.getcode()
                and self._modifier == other.getmodifier())

    def __ne__(self, other):
        """function __ne__

        returns bool
        """
        return not self == other

    def __lt__(self, other):
        """function __lt__

        other:

        returns bool
        """
        return self._code > other

    def __le__(self, other):
        """function __le__

        other:

        returns bool
        """
        return self._code >= other

    def __gt__(self, other):
        """function __gt__

        other:

        returns bool
        """
        return self._code < other

    def __ge__(self, other):
        """function __ge__

        other:

        returns bool
        """
        return self._code <= other

    def __hash__(self):
        """function __hash__

        returns int
        """
        return hash(int(self._code) * 1000 + int(self._modifier))

    def __add__(self, other):
        """function __add__

        other:

        returns
        """
        if isinstance(other, self.__class__):
            return self.__class__(self._code + other.getcode(),
                                  self._modifier | other.getmodifier())
        return self.__class__(self._code + other, self._modifier)

    def __iadd__(self, other):
        """function __iadd__

        other:

        returns
        """
        if isinstance(other, self.__class__):
            self._code += other.getcode()
            self._modifier |= other.getmodifier()
        else:
            self._code += other
        return self

    def __sub__(self, other):
        """function __sub__

        other:

        returns
        """
        if isinstance(other, self.__class__):
            return self.__class__(self._code - other.getcode(),
                                  self._modifier ^ other.getmodifier())
        return self.__class__(self._code - other, self._modifier)

    def __isub__(self, other):
        """function __isub__

        other:

        returns
        """
        if isinstance(other, self.__class__):
            self._code -= other.getcode()
            self._modifier ^= other.getmodifier()
        else:
            self._code -= other
        return self

    def __mul__(self, other):
        """function __mul__

        other:

        returns
        """
        if isinstance(other, self.__class__):
            return self.__class__(self._code * other.getcode(),
                                  self._modifier | other.getmodifier())
        return self.__class__(self._code * other, self._modifier)

    def __imul__(self, other):
        """function __imul__

        other:

        returns
        """
        if isinstance(other, self.__class__):
            self._code *= other.getcode()
            self._modifier |= other.getmodifier()
        else:
            self._code *= other
        return self

    def __div__(self, other):
        """function __div__

        other:

        returns
        """
        if isinstance(other, self.__class__):
            return self.__class__(self._code / other.getcode(),
                                  self._modifier | other.getmodifier())
        return self.__class__(self._code / other, self._modifier)

    def __idiv__(self, other):
        """function __idiv__

        other:

        returns
        """
        if isinstance(other, self.__class__):
            self._code /= other.getcode()
            self._modifier |= other.getmodifier()
        else:
            self._code /= other
        return self

    def __mod__(self, other):
        """function __mod__

        other:

        returns
        """
        if isinstance(other, self.__class__):
            return self.__class__(self._code % other.getcode(),
                                  self._modifier | other.getmodifier())
        return self.__class__(self._code % other, self._modifier)

    def __imod__(self, other):
        """function __imod__

        other:

        returns
        """
        if isinstance(other, self.__class__):
            self._code %= other.getcode()
            self._modifier |= other.getmodifier()
        else:
            self._code %= other
        return self

    def __int__(self):
        """function __int__

        returns int
        """
        return int(self._code)

    def __long__(self):
        """function __long__

        returns long
        """
        return long(self._code)

    def __hex__(self):
        """function __hex__

        returns
        """
        return hex(self._code)

    def __or__(self, other):
        """function __or__

        other:

        returns
        """
        return self.__class__(self._code, self._modifier | other)

    def __ior__(self, other):
        """function __ior__

        other:

        returns
        """
        self._modifier |= other
        return self

    def __and__(self, other):
        return self.__class__(self._code, self._modifier & other)

    def __iand__(self, other):
        self._modifier &= other
        return self

    def __xor__(self, other):
        """function __xor__

        other:

        returns
        """
        return self.__class__(self._code, self._modifier ^ other)

    def __ixor__(self, other):
        """function __ixor__

        other:

        returns
        """
        self._modifier ^= other
        return self

    def __lshift__(self, other):
        """function __lshift__

        other:

        returns
        """
        return self.__class__(self._code, self._modifier << other)

    def __ilshift__(self, other):
        """function __ilshift__

        other:

        returns
        """
        self._modifier <<= other
        return self

    def __rshift__(self, other):
        """function __rshift__

        other:

        returns
        """
        return self.__class__(self._code, self._modifier >> other)

    def __irshift__(self, other):
        """function __irshift__

        other:

        returns
        """
        self._modifier >>= other
        return self


class Key(Piece):
    """Class Key
    """
    # Attributes:

    # Operations
    def press(self, propagate, window, sequence_number, time, child, rootx,
              rooty, eventx, eventy, samescreen, display=None):
        """function press

        window:
        time: int
        child: int
        rootx: int
        rooty: int
        eventx: int
        eventy: int
        samescreen: int
        propagate: int
        display: str

        returns
        """
        return self._code.press(
            propagate, window, sequence_number, time, child, rootx, rooty,
            eventx, eventy, self._modifier, samescreen, display)

    def release(self, propagate, window, sequence_number, time, child, rootx,
              rooty, eventx, eventy, samescreen, display=None):
        """function release

        window: int
        child: int
        rootx: int
        rooty: int
        eventx: int
        eventy: int
        samescreen: int
        propagate: int
        display: str

        returns
        """
        return self._code.release(
            propagate, window, sequence_number, time, child, rootx, rooty,
            eventx, eventy, self._modifier, samescreen, display)

    def grab(self, owner_events, window, display=None):
        """function grab

        returns
        """
        return self._code.grab(owner_events, window, self._modifier, display)

    def ungrab(self, window, display=None):
        """function ungrab

        returns
        """
        return self._code.ungrab(window, self._modifier, display)

    def to_keysym(self, display=None):
        """function to_keysym

        display:

        returns
        """
        return self._code.to_keysym(self._modifier, display=display)


class Button(Piece):
    """Class Button
    """
    # Attributes:

    # Operations
    def grabpress(self):
        """function grabpress

        returns
        """
        return None # should raise NotImplementedError()

    def grabrelease(self):
        """function grabrelease

        returns
        """
        return None # should raise NotImplementedError()

    def ungrab(self):
        """function ungrab

        returns
        """
        return None # should raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# piece.py ends here
