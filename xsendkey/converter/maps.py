#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""maps -- DESCRIPTION

"""
import warnings as _warnings
from pprint import pformat as _pformat

from wxcb import conn as _conn
from wxcb.xobj.display import Display
from wxcb.protocol.xproto.requests import GetKeyboardMapping
from wxcb.xobj.keycode import Keycode
from wxcb.xobj.keysym import Keysym

from xsendkey.converter.keysymdef import Keysymdef


class CharToSym(object):
    r"""CharToSym

    CharToSym is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._data = {}
        for sym in Keysymdef.itervalues():
            try:
                self._data.setdefault(sym.to_char(), sym)
            except StandardError:
                # TODO: (Atami) [2015/01/25]
                pass

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._data.clear()

    def setdefault(self, char, sym):
        r"""SUMMARY

        setdefault(char, sym)

        @Arguments:
        - `char`:
        - `sym`:

        @Return:

        @Error:
        """
        if not isinstance(char, (str, )) and 1 < len(char):
            # TODO: (Atami) [2015/01/25]
            raise TypeError(char)
        if not isinstance(sym, (Keysym, )):
            raise TypeError(sym)
        self._data.setdefault(char, sym)

    def char_to_sym(self, char):
        """function char_to_sym

        char: unicode

        returns
        """
        return self[char]

    def chars(self):
        """function chars

        returns
        """
        return self._data.keys()

    def syms(self):
        """function syms

        returns
        """
        return self._data.values()

    def iterchars(self):
        """function iterchars

        returns
        """
        return self._data.iterkeys()

    def itersyms(self):
        """function itersyms

        returns
        """
        return self._data.itervalues()

    def items(self):
        """function items

        returns
        """
        return self._data.items()

    def iteritems(self):
        """function iteritems

        returns
        """
        return self._data.iteritems()

    def clear(self):
        """function clear

        returns
        """
        return self._data.clear()

    def copy(self):
        """function copy

        returns
        """
        from copy import deepcopy
        return deepcopy(self)

    def __setitem__(self, char, sym):
        if not isinstance(char, (basestring, )):
            # TODO: (Atami) [2015/01/11]
            raise StandardError()
        symobj = sym
        if isinstance(symobj, (int, )):
            symobj = Keysym(symobj)
        if not isinstance(symobj, (Keysym)):
            # TODO: (Atami) [2015/01/11]
            raise StandardError()
        self._data[char] = symobj

    def __getitem__(self, char):
        return self._data[char]

    def __delitem__(self, char):
        del self._data[char]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return '{0.__class__.__name__}({1})'.format(self, _pformat(self._data))

    def __contains__(self, char):
        return char in self._data

    def __nonzero__(self):
        return bool(self._data)


class CodeToSyms(object):
    r"""CodeToSyms

    CodeToSyms is a object.
    Responsibility:
    """
    _instances = {}

    # Singleton
    def __new__(cls, *args, **kwargs):
        if len(args):
            key = Display(args[0])
        else:
            key = Display(kwargs.get('display', ''))
        if key not in cls._instances:
            cls._instances[key] = object.__new__(cls, *args, **kwargs)
        return cls._instances[key]

    # Attributes:
    def __init__(self, display=None):
        r"""
        """
        self._display = Display(display)
        self.data = {}
        self.update()

    __hash__ = None # Avoid Py3k warning

    # Operations
    def update(self, ):
        """update

        dict_:

        returns None
        """
        self.clear()
        setup = _conn.connect(self.display).get_setup()
        min_, max_ = int(setup.min_keycode), int(setup.max_keycode)
        last, count = max_ + min_, max_ - min_ + 1
        rep = GetKeyboardMapping(
            min_, count, display=self.display).request().reply()
        # chunks rep.keysyms
        self[min_:last] = zip(*[iter(rep.keysyms)] * rep.keysyms_per_keycode)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._display

    display = property(get_display)

    def setdefault(self, code, syms=None):
        r"""SUMMARY

        setdefault(code, syms=None)

        @Arguments:
        - `code`:
        - `syms`: (default: [])

        @Return:

        @Error:
        """
        if code not in self:
            self[code] = syms or []
        return self[code]

    def code_to_syms(self, code):
        """code_to_syms

        @Arguments:
        - `code`:

        @Return list:
        """
        return self[code]

    # def code_to_sym(self, code, modifiers=0):
    #     """code_to_sym

    #     code: int
    #     modifiers: int

    #     returns Keysym
    #     """
    #     index = 0
    #     if (NamedModifierMask.Shift & modifiers) != 0:
    #         index += 1
    #     if (NamedModifierMask.Alt & modifiers) != 0:
    #         index += 2
    #     return self[code][index]

    def clear(self):
        """clear

        returns None
        """
        self.data.clear()

    def copy(self):
        """copy

        returns CodeToSyms
        """
        from copy import deepcopy
        return deepcopy(self)

    def codes(self):
        """codes

        returns list
        """
        return self.data.keys()

    def listsyms(self):
        """listsyms

        returns lsit
        """
        return self.data.values()

    def itercodes(self):
        """itercodes

        returns generator
        """
        return self.data.iterkeys()

    def itersyms(self):
        """itersyms

        returns generator
        """
        return self.data.itervalues()

    def items(self):
        """items

        returns list
        """
        return self.data.items()

    def iteritems(self):
        """iteritems

        returns generator
        """
        return self.data.iteritems()

    def __setitem__(self, code, syms):
        self.data[Keycode(code)] = [Keysym(x) for x in syms]

    def __getitem__(self, code):
        return self.data[code]

    def __delitem__(self, code):
        del self.data[code]

    def __getslice__(self, i, j):
        i, j = max(i, 0), max(j, 0)
        if j < i:
            i, j = j, i
        new = self.__class__()
        for code in xrange(i, j + 1):
            try:
                new.setdefault(code, self[code])
            except KeyError as _err:
                _warnings.warn(str(_err))
        return new

    def __setslice__(self, i, j, seq):
        i, j = max(i, 0), max(j, 0)
        if j < i:
            i, j = j, i
        for code, syms in zip(xrange(i, j + 1), seq):
            self[code] = syms

    def __delslice__(self, i, j):
        i, j = max(i, 0), max(j, 0)
        if j < i:
            i, j = j, i
        for code in xrange(i, j + 1):
            try:
                del self[code]
            except KeyError as _err:
                _warnings.warn(str(_err))

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return '{0.__class__.__name__}({1})'.format(self, _pformat(self.data))

    def __str__(self):
        return repr(self)

    def __cmp__(self, other):
        if isinstance(other, (self.__class__, )):
            return cmp(self.data, other.data)
        return cmp(self.data, other)


    def __contains__(self, code):
        return code in self.data

    def __iter__(self):
        return iter(self.data)

    def __nonzero__(self):
        return bool(self.data)


class SymToCodes(object):
    """Class SymToCodes
    """
    # Attributes:
    _instances = {}

    # Singleton
    def __new__(cls, *args, **kwargs):
        if len(args):
            key = Display(args[0])
        else:
            key = Display(kwargs.get('display', ''))
        if key not in cls._instances:
            cls._instances[key] = object.__new__(cls, *args, **kwargs)
        return cls._instances[key]

    def __init__(self, display=None):
        r"""

        @Arguments:
        - `dic`:
        """
        self._data = {}
        self._display = Display(display)
        for code, syms in CodeToSyms(self._display).iteritems():
            self.setsyms(code, syms)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._display

    display = property(get_display)

    # Operations
    def update(self, dic):
        """function update

        dict:

        returns None
        """
        if isinstance(dic, (dict, self.__class__)):
            for sym, codes in dic.items():
                self[sym] = codes

    def setsyms(self, code, syms):
        r"""SUMMARY

        setsyms(code, syms)

        @Arguments:
        - `code`:
        - `syms`:

        @Return:

        @Error:
        """
        sym, index = 0, 0 # for escape pylint warning
        for index, sym in enumerate(syms, start=0):
            if 0 == sym:
                continue
            self.appendcode(sym, code, index)

    def appendcode(self, sym, code, index):
        r"""SUMMARY

        appendcode(sym, code)

        @Arguments:
        - `sym`:
        - `code`:

        @Return:

        @Error:
        """
        codes = self[sym]
        codes.append((code, index))
        if 2 <= len(codes):
            self._sort_codes(sym)

    def _sort_codes(self, sym):
        r"""SUMMARY

        sort_codes(sym)

        @Arguments:
        - `sym`:

        @Return:

        @Error:
        """
        def getmodifiers(tup):
            r"""For sort modifiers."""
            return tup[1]
        self[sym].sort(key=getmodifiers)

    def set(self, sym, codes):
        """function set

        sym: int
        codes: list

        returns None
        """
        self[sym] = codes

    def sym_to_codes(self, sym):
        """function sym_to_codes

        sym: int

        returns list

        Error: KeyError
        """
        return self._data.get(sym)

    # def sym_to_code(self, sym, index):
    #     """function sym_to_code

    #     sym: int
    #     modifiers: int

    #     returns Keycode
    #     """
    #     return self.sym_to_codes(sym)[index]

    def clear(self):
        """function clear

        returns None
        """
        return self._data.clear()

    def copy(self):
        """function copy

        returns SymToCodes
        """
        from copy import deepcopy
        return deepcopy(self)

    def syms(self):
        """function syms

        returns list
        """
        return self._data.keys()

    def listcodes(self):
        """function listcodes

        returns list
        """
        return self._data.values()

    def itersyms(self):
        """function itersyms

        returns generator
        """
        return self._data.iterkeys()

    def itercodes(self):
        """function itercodes

        returns generator
        """
        return self._data.itervalues()

    def items(self):
        """function items

        returns list
        """
        return self._data.items()

    def iteritems(self):
        """function iteritems

        returns generator
        """
        return self._data.iteritems()

    def __setitem__(self, sym, codes):
        if not isinstance(sym, (int, Keysym)):
            # TODO: (Atami) [2015/01/10]
            raise TypeError()
        if not isinstance(codes, list):
            # TODO: (Atami) [2015/01/10]
            raise TypeError()
        self._data[sym] = codes

    def __getitem__(self, sym):
        if not sym in self:
            self[sym] = []
        return self._data[sym]

    def __delitem__(self, sym):
        del self._data[sym]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return '{0.__class__.__name__}({1})'.format(self, _pformat(self._data))

    def __str__(self):
        return None # should raise NotImplementedError()

    def __contains__(self, sym):
        return sym in self._data

    def __iter__(self):
        return iter(self._data)

    def __nonzero__(self):
        return bool(self._data)




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# maps.py ends here
