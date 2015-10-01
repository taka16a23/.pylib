#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: keyboardmapping.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""keyboardmapping -- DESCRIPTION

"""
from pprint import pformat as _pformat

import xcb2
import xcode
import keysym
import piece
from t1.listutil import ListUtil


class GetKeyboardMapping(object):
    r"""GetKeyboardMapping

    GetKeyboardMapping is a object.
    Responsibility:
    """
    def __init__(self, conn, mincode, maxcode):
        r"""

        @Arguments:
        - `mincode`:
        - `maxcode`:
        - `display`:
        """
        self._conn = conn
        self._mincode = mincode
        self._maxcode = maxcode

    def getmincode(self, ):
        r"""SUMMARY

        getmincode()

        @Return:

        @Error:
        """
        return self._mincode

    def getmaxcode(self, ):
        r"""SUMMARY

        getmaxcode()

        @Return:

        @Error:
        """
        return self._maxcode

    def getlastcode(self, ):
        r"""SUMMARY

        getlastcode()

        @Return:

        @Error:
        """
        return self.getmincode() + self.getmaxcode()

    def getkeyboardmapping(self, ):
        r"""SUMMARY

        getkeyboardmapping()

        @Return:

        @Error:
        """
        mincode, maxcode = self.getmincode(), self.getmaxcode()
        return self._conn.core.GetKeyboardMapping(
            mincode, maxcode - mincode + 1)

    def __call__(self,):
        return self.getkeyboardmapping()


class SymbolsMap(object):
    """Class SymbolsMap
    """
    # Attributes:
    def __init__(self, display, dic=None):
        r"""

        @Arguments:
        - `dic`:
        - `kwargs`:
        """
        self._display = display
        self._dic = {}
        if dic is not None:
            self.update(dic)

    # Operations
    def getdisplay(self, ):
        r"""SUMMARY

        getdisplay()

        @Return:

        @Error:
        """
        return self._display

    def getsyms(self, code, default=None):
        """function getsyms

        code:

        returns
        """
        return self._dic.get(code, default or [])

    def getsym(self, code, index, default=None):
        """function getsym

        code:
        index:

        returns
        """
        syms = self.getsyms(code)
        if index > len(syms):
            return default
        return syms[index]

    def loadsyms(self, symslist, mincode):
        """function loadsyms

        syms: list
        mincode:

        returns
        """
        for code, syms in enumerate(symslist, start=mincode):
            self[xcode.KeyCode(code)] = syms

    def listsyms(self):
        """function listsyms

        returns
        """
        return self._dic.values()

    def listcodes(self):
        """function listcodes

        returns
        """
        return self._dic.keys()

    def itersyms(self):
        """function itersyms

        returns
        """
        return self._dic.itervalues()

    def itercodes(self):
        """function itercodes

        returns
        """
        return self._dic.iterkeys()

    def items(self):
        """function listsymcode

        returns
        """
        return self._dic.items()

    def iteritems(self):
        """function itersymcode

        returns
        """
        return self._dic.iteritems()

    def clear(self):
        """function clear

        returns
        """
        return self._dic.clear()

    def update(self, dic):
        """function update

        dict:
        **kwargs:

        returns
        """
        if isinstance(dic, (dict, self.__class__)):
            for code, syms in dic.items():
                self[code] = syms

    def copy(self):
        """function copy

        returns
        """
        return self.__class__(self._display, self._dic.copy())

    def __contains__(self, code):
        """function __contains__

        code:

        returns
        """
        if not isinstance(code, int):
            # TODO: (Atami) [2014/10/22]
            raise TypeError(
                'TODO: {}({})'.format('SymbolsMap.__contains__', code))
        return code in self._dic

    def __getitem__(self, code):
        """function __getitem__

        code:

        returns
        """
        return self._dic[code]

    def __setitem__(self, code, syms):
        """function __setitem__

        code:
        syms:

        returns
        """
        if not isinstance(code, int):
            # TODO: (Atami) [2014/10/22]
            raise TypeError(
                '{}({})'.format('SymbolsMap.__setitem__', code))
        if not isinstance(syms, list):
            # TODO: (Atami) [2014/10/22]
            raise TypeError(
                '{}({})'.format('SymbolsMap.__setitem__', syms))
        self._dic[code] = syms

    def __delitem__(self, code):
        """function __delitem__

        code:

        returns
        """
        del self._dic[code]

    def __len__(self):
        """function __len__

        returns
        """
        return len(self._dic)

    def __repr__(self):
        return '{0.__class__.__name__}(\n{1})'.format(self, _pformat(self._dic))

    @classmethod
    def fromdisplay(cls, display=None):
        """function fromdisplay

        display:

        returns
        """
        disp = display or ':0.0'
        this = cls(disp)
        conn = xcb2.connect(display=disp)
        setup = conn.get_setup()
        reply = GetKeyboardMapping(
            conn, setup.min_keycode, setup.max_keycode)().reply()
        symslist = ListUtil(reply.keysyms)
        symslist.chunks(reply.keysyms_per_keycode)
        this.loadsyms(symslist, setup.min_keycode)
        return this


class CodesMap(object):
    """Class CodesMap
    """
    # Attributes:
    def __init__(self, display, dic=None):
        r"""

        @Arguments:
        - `dic`:
        - `kwargs`:
        """
        self._display = display
        self._dic = {}
        if dic is not None:
            self.update(dic)

    # Operations
    def getdisplay(self):
        """function getdisplay

        returns
        """
        return self._display

    def getcodes(self, sym, default=None):
        """function getcodes

        sym:

        returns
        """
        return self._dic.get(sym, default or [])

    def getcode(self, sym, default=None):
        """function getcode

        sym:
        index:

        returns
        """
        codes = self.getcodes(sym)
        if codes is None:
            return default
        return codes[0]

    def listcodes(self):
        """function listcodes

        returns
        """
        return self._dic.values()

    def listsyms(self):
        """function listsyms

        returns
        """
        return self._dic.keys()

    def itercodes(self):
        """function itercodes

        returns
        """
        return self._dic.itervalues()

    def itersyms(self):
        """function itersyms

        returns
        """
        return self._dic.iterkeys()

    def items(self):
        """function items

        returns
        """
        return self._dic.items()

    def iteritems(self):
        """function iteritems

        returns
        """
        return self._dic.iteritems()

    def clear(self):
        """function clear

        returns
        """
        self._dic.clear()

    def update(self, dic):
        """function update

        dict:

        returns
        """
        if isinstance(dic, (dict, self.__class__)):
            for sym, codes in dic.items():
                self[sym] = codes

    def copy(self):
        """function copy

        returns
        """
        return self.__class__(self._display, self._dic.copy())

    def __contains__(self, sym):
        """function __contains__

        sym:

        returns
        """
        return sym in self._dic

    def __getitem__(self, sym):
        return self._dic[sym]

    def __delitem__(self, sym):
        """function __delitem__

        sym:

        returns
        """
        del self._dic[sym]

    def __setitem__(self, sym, codes):
        """function __setitem__

        sym:
        codes:

        returns
        """
        if not isinstance(sym, int):
            raise TypeError('{}({})'.format('CodesMap.__setitem__', sym))
        if not isinstance(codes, list):
            raise TypeError('{}({})'.format('CodesMap.__setitem__', codes))
        self._dic[sym] = codes

    def __len__(self):
        """function __len__

        returns
        """
        return len(self._dic)

    def __repr__(self):
        return '{0.__class__.__name__}(\n{1})'.format(self, _pformat(self._dic))

    def appendkey(self, sym, key):
        r"""SUMMARY

        appendkey(sym, key)

        @Arguments:
        - `sym`:
        - `key`:

        @Return:

        @Error:
        """
        def getmodifier(key):
            return key.getmodifier()

        if not sym in self:
            self[sym] = []
        codes = self.getcodes(sym)
        codes.append(key)
        if 1 < len(codes):
            codes.sort(key=getmodifier)

    def setsyms(self, code, syms):
        r"""SUMMARY

        setsyms(code, syms)

        @Arguments:
        - `code`:
        - `syms`:

        @Return:

        @Error:
        """
        for index, sym in enumerate(syms, start=0):
            if 0 == sym:
                continue
            self.appendkey(sym, piece.Key(code, index))

    @classmethod
    def fromdisplay(cls, display=None):
        """function fromdisplay

        display:

        returns
        """
        return cls.fromsymbolsmap(SymbolsMap.fromdisplay(display=display))

    @classmethod
    def fromsymbolsmap(cls, map_):
        """function fromsymbolsmap

        map:

        returns
        """
        if not isinstance(map_, SymbolsMap):
            # TODO: (Atami) [2014/10/22]
            raise StandardError()

        codemap = cls(map_.getdisplay())
        for code, syms in map_.iteritems():
            codemap.setsyms(code, syms)
        return codemap


class KeyboardMapping(object):
    """Class KeyboardMapping
    """
    # Attributes:
    def __init__(self, display=None):
        r"""

        @Arguments:
        - `codemap`:
        - `symmap`:
        """
        self._symmap = SymbolsMap.fromdisplay(display=display)
        self._codemap = CodesMap.fromsymbolsmap(self._symmap)

    # Operations
    def get_codemap(self):
        """function get_codemap

        returns
        """
        return self._codemap

    def get_symmap(self):
        """function get_symmap

        returns
        """
        return self._symmap

    def sym_to_codes(self, sym):
        r"""SUMMARY

        sym_to_codes(sym)

        @Arguments:
        - `sym`:

        @Return:

        @Error:
        """
        return self._codemap.getcodes(sym)

    def sym_to_key(self, sym, default=None):
        """function sym_to_code

        sym:

        returns
        """
        codes = self.sym_to_codes(sym)
        if codes is None:
            return default
        return codes[0]

    def code_to_syms(self, code):
        r"""SUMMARY

        code_to_syms(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        return self._symmap.getsyms(code)

    def code_to_sym(self, code, index):
        """function code_to_sym

        code:
        index:

        returns
        """
        syms = self.code_to_syms(code)
        if not syms is None and index > len(syms):
            return keysym.Keysym(xcb2.NoSymbol)
        return syms[index]

    def update(self, ):
        r"""SUMMARY

        update()

        @Return:

        @Error:
        """
        self._symmap.clear()
        self._codemap.clear()
        symmap = SymbolsMap.fromdisplay(display=self._symmap.getdisplay())
        codemap = CodesMap.fromsymbolsmap(symmap)
        self._symmap.update(symmap)
        self._codemap.update(codemap)


class KeyboardMappingHolder(object):
    """Class KeyboardMappingHolder
    """
    # Attributes:
    def __init__(self, ):
        r"""
        """
        self._maps = {}

    # Operations
    def get(self, display):
        """function get_keyboardmapping

        display:

        returns
        """
        if not display in self:
            self._create_keyboardmapping(display)
        return self[display]

    def update(self, display):
        """function update

        display:

        returns
        """
        if display in self:
            self[display].update()

    def clear(self):
        """function clear

        returns
        """
        self._maps.clear()

    def delete(self, display):
        """function delete

        display:

        returns
        """
        del self[display]

    def listdisplays(self):
        """function listdisplays

        returns
        """
        return self._maps.keys()

    def iterdisplays(self):
        """function iterdisplays

        returns
        """
        return self._maps.iterkeys()

    def listkeyboardmapping(self):
        """function listkeyboardmapping

        returns
        """
        return self._maps.values()

    def iterkeyboardmapping(self):
        """function iterkeyboardmapping

        returns
        """
        return self._maps.itervalues()

    def items(self):
        """function items

        returns
        """
        return self._maps.items()

    def iteritems(self):
        """function iteritems

        returns
        """
        return self._maps.iteritems()

    def __delitem__(self, display):
        """function __delitem__

        display:

        returns
        """
        del self._maps[display]

    def __contains__(self, display):
        """function __contains__

        display:

        returns
        """
        return display in self._maps

    def __getitem__(self, display):
        """function __getitem__

        display:

        returns
        """
        return self._maps[display]

    def __len__(self):
        return len(self._maps)

    def __setitem__(self, display, mapping):
        """function __setitem__

        display:
        keyboardmapping:

        returns
        """
        if not isinstance(mapping, KeyboardMapping):
            # TODO: (Atami) [2014/10/22]
            raise StandardError()
        self._maps[display] = mapping

    def _create_keyboardmapping(self, display):
        """function create_keyboardmapping

        display:

        returns
        """
        self[display] = KeyboardMapping(display)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keyboardmapping.py ends here
