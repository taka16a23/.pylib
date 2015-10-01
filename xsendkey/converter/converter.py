#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""converter -- DESCRIPTION

"""
from wxcb.xobj.keycode import Keycode
from wxcb.xobj.keysym import Keysym
from wxcb.protocol.xproto.define import NamedModifierMask

from xsendkey.converter.keyname import Keyname
from xsendkey.converter.maps import CodeToSyms, SymToCodes, CharToSym
from xsendkey.converter.err import ConvertError
from xsendkey.converter.keysymdef import Keysymdef


class CharConverter(object):
    r"""CharConverter

    CharConverter is a object.
    Responsibility:
    """
    _charmap = CharToSym()

    def __init__(self, char):
        r"""

        @Arguments:
        - `char`:
        """
        self._char = char

    def get_char(self, ):
        r"""SUMMARY

        get_char()

        @Return:

        @Error:
        """
        return self._char

    def set_char(self, char):
        r"""SUMMARY

        set_char(char)

        @Arguments:
        - `char`:

        @Return:

        @Error:
        """
        if not len(char) == 1 or not isinstance(char, (str, )):
            # TODO: (Atami) [2015/01/25]
            raise ValueError()
        self._char = char

    char = property(get_char, set_char)

    def to_sym(self, ):
        r"""SUMMARY

        to_sym()

        @Return:

        @Error:
        """
        return self._charmap.char_to_sym(self._char)

    def to_code(self, display=None):
        r"""SUMMARY

        to_code(display=None)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return SymConverter(self.to_sym()).to_code(display=display)


class NameConverter(object):
    r"""NameConverter

    NameConverter is a object.
    Responsibility:
    """
    def __init__(self, name):
        r"""

        @Arguments:
        - `name`:
        """
        self._name = Keyname(name)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._name

    def set_name(self, name):
        r"""SUMMARY

        set_name(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        self._name.set(name)

    name = property(get_name, set_name)

    def to_sym(self, ):
        r"""SUMMARY

        to_sym()

        @Return:

        @Error:
        """
        sym = Keysymdef.get(self._name, None)
        if sym is None:
            # TODO: (Atami) [2015/01/25]
            raise ConvertError()
        return sym

    def to_code(self, display=None):
        r"""SUMMARY

        to_code(display=None)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        return SymConverter(self.to_sym()).to_code(display=display)


class CodeConverter(object):
    r"""CodeConverter

    CodeConverter is a object.
    Responsibility:
    """
    def __init__(self, code):
        r"""

        @Arguments:
        - `code`:
        - `display`:
        """
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

    def to_syms(self, display=None):
        r"""SUMMARY

        to_syms()

        @Return:

        @Error:
        """
        return CodeToSyms(display).code_to_syms(self._code)

    def to_sym(self, modifier=0, display=None):
        r"""SUMMARY

        to_sym(modifier=0)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        index = 0
        if (NamedModifierMask.Shift & modifier) != 0:
            index += 1
        if (NamedModifierMask.Alt & modifier) != 0:
            index += 2
        try:
            return self.to_syms(display)[index]
        except IndexError as _err:
            raise ConvertError(_err)

    def to_name(self, modifier=0):
        r"""SUMMARY

        to_name(modifier=0)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        # TODO: (Atami) [2015/01/25]

    def __repr__(self):
        return '{0.__class__.__name__}(code={1})'.format(self, int(self._code))


class SymConverter(object):
    r"""SymConverter

    SymConverter is a object.
    Responsibility:
    """
    def __init__(self, sym):
        r"""

        @Arguments:
        - `sym`:
        - `display`:
        """
        self._sym = Keysym(sym)

    def get_sym(self, ):
        r"""SUMMARY

        get_sym()

        @Return:

        @Error:
        """
        return self._sym

    def set_sym(self, sym):
        r"""SUMMARY

        set_sym(sym)

        @Arguments:
        - `sym`:

        @Return:

        @Error:
        """
        self._sym.set(sym)

    sym = property(get_sym, set_sym)

    def to_codes(self, display=None):
        r"""SUMMARY

        to_codes()

        @Return:

        @Error:
        """
        return SymToCodes(display).sym_to_codes(self.sym)

    def to_code(self, index=0, display=None):
        r"""SUMMARY

        to_code(modifier=0)

        @Arguments:
        - `modifier`:

        @Return:

        @Error:
        """
        try:
            return self.to_codes(display)[index]
        except IndexError as _err:
            # TODO: (Atami) [2015/01/25]
            raise ConvertError(_err)

    def to_name(self, ):
        r"""SUMMARY

        to_name()

        @Return:

        @Error:
        """
        # TODO: (Atami) [2015/01/25]

    def __repr__(self):
        return '{0.__class__.__name__}(sym={1})'.format(self, int(self.sym))




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# converter.py ends here
