#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: keysym.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

from xcb2 import NoSymbol

import keysymdef
import namesym
import charsym
import keyboardmapping as mapping
from .err import ConvertError


class Keysym(int):
    """Class Keysym
    """
    _mapping = mapping.KeyboardMappingHolder()

    @classmethod
    def getmapping(cls, ):
        r"""SUMMARY

        getmapping()

        @Return:

        @Error:
        """
        return cls._mapping

    # Operations
    def to_name(self):
        """function to_name

        returns Namesym
        """
        return keysymdef.Keysymdef.sym_to_name(self)

    def to_char(self):
        """function to_char

        returns Charsym
        """
        # TODO: (Atami) [2014/10/15]
        # entrust to converter object
        if self.isspecial():
            raise ConvertError(self)
        if self.islatin1():
            return charsym.Charsym(unichr(self))
        if self.isunicode():
            return charsym.Charsym(unichr(self - 0x01000000))
        if self.islegacy():
            return charsym.Charsym(unichr(keysymdef.LEGACY[self]))
        # nothing
        raise ConvertError(self)

    def isspecial(self, ):
        r"""SUMMARY

        isspecial()

        @Return:

        @Error:
        """
        return self in (0, 0x00ffffff)

    def islatin1(self, ):
        r"""SUMMARY

        islatin1()

        @Return:

        @Error:
        """
        return (0x0020 <= self <= 0x007e or 0x00a0 <= self <= 0x00ff)

    def isunicode(self, ):
        r"""SUMMARY

        isunicode()

        @Return:

        @Error:
        """
        return (0x01000100 <= self <= 0x0110ffff)

    def islegacy(self, ):
        r"""SUMMARY

        islegacy()

        @Return:

        @Error:
        """
        return self in keysymdef.LEGACY

    def to_code(self, display=':0.0'):
        """function to_code

        returns tuple
        """
        return self._mapping.get(display).sym_to_code(self)

    def to_key(self, display=':0.0'):
        """function to_key

        returns Key
        """
        return self._mapping.get(display).sym_to_key(self)

    def isnosymbol(self):
        """function isnosymbol

        returns bool
        """
        return self == NoSymbol

    def iscursorkey(self):
        """function iscursorkey

        returns bool
        """
        return (self >= 'Home' and self < 'Select')

    def isfunctionkey(self):
        """function isfunctionkey

        returns bool
        """
        return (self >= 'F1' and self <= 'F35')

    def iskeypadkey(self):
        """function iskeypadkey

        returns bool
        """
        return (self >= 'KP_Space' and self <= 'KP_Equal')

    def isprivatekeypadkey(self):
        """function isprivatekeypadkey

        returns bool
        """
        return (self >= 0x11000000 and self <= 0x1100FFFF)

    def ismiscfunctionkey(self):
        """function ismiscfunctionkey

        returns bool
        """
        return (self >= 'Select' and self <= 'Break')

    def ismodifierkey(self):
        """function ismodifierkey

        returns bool
        """
        return ((self >= 'Shift_L' and self <= 'Hyper_R')
                or (self >= 'ISO_Lock' and self <= 'ISO_Level5_Lock')
                or (self == 'Mode_switch')
                or (self == 'Num_Lock'))

    def ispfkey(self):
        """function ispfkey

        returns bool
        """
        return ((self >= 'Shift_L' and self <= 'Hyper_R')
                or (self == 'Mode_switch')
                or (self == 'Num_Lock'))

    def __repr__(self):
        """function __repr__

        returns
        """
        return '{0.__class__.__name__}({1})'.format(self, hex(self))

    def __str__(self):
        """function __str__

        returns
        """
        return str(self.to_name())

    def __eq__(self, other):
        if isinstance(other, (basestring, )):
            sym = keysymdef.Keysymdef.name_to_sym(other)
            if sym == 0:
                return False
            return int(self) == sym
        return int(self) == int(other)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, (basestring, )):
            sym = keysymdef.Keysymdef.name_to_sym(other)
            if sym == 0:
                return False
            return int(self) < sym
        return int(self) < int(other)

    def __le__(self, other):
        if isinstance(other, (basestring, )):
            sym = keysymdef.Keysymdef.name_to_sym(other)
            if sym == 0:
                return False
            return int(self) <= sym
        return int(self) <= int(other)

    def __gt__(self, other):
        if isinstance(other, (basestring, )):
            sym = keysymdef.Keysymdef.name_to_sym(other)
            if sym == 0:
                return False
            return int(self) > sym
        return int(self) > int(other)

    def __ge__(self, other):
        if isinstance(other, (basestring, )):
            sym = keysymdef.Keysymdef.name_to_sym(other)
            if sym == 0:
                return False
            return int(self) >= sym
        return int(self) >= int(other)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keysym.py ends here
