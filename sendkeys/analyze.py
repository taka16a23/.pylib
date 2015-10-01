#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: analyze.py 189 2014-05-17 09:44:59Z t1 $
# $Revision: 189 $
# $Date: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $

r"""analyze -- DESCRIPTION

"""
from xcb2.xproto import NamedModifierMask, NamedButtonIndex

from sendkeys.display import KeymapDisplay
from sendkeys.modifierstate import ModifierState
from sendkeys.stoken import TokenType
from sendkeys.expression import Expression


class Analyzer(KeymapDisplay):
    r"""SUMMARY
    """

    def __init__(self, tokens, display=None):
        r"""SUMMARY

        __init__(tokens, display=None)

        @Arguments:
        - `tokens`:
        - `display`:

        @Return:
        """
        KeymapDisplay.__init__(self, display)
        self.tokens = tokens
        self._iter = None
        self._state = ModifierState(NamedModifierMask.Null) # init 0

    def _clear_state(self, ):
        r"""SUMMARY

        clear_state()

        @Return:
        """
        self._state = ModifierState(NamedModifierMask.Null)

    def _iter_incurly(self, ):
        r"""SUMMARY

        _iterinculy()

        @Return:
        """
        code = None
        kwargs = {}
        repeat = 1
        press, release = True, True
        while 1:
            token = self._iter.next()
            if token.types in (TokenType.KEY, TokenType.BUTTON):
                code = token.get()
            elif token.types in (TokenType.GEOX, TokenType.GEOY):
                kwargs.update(token.get())
            elif TokenType.KEYUP == token.types:
                press = False # release only
            elif TokenType.KEYDOWN == token.types:
                release = False # press only
            elif TokenType.REPEAT == token.types:
                repeat = token.get()
            elif TokenType.CURLYEND == token.types: # '}'
                if code is None:
                    # TODO: (Atami) [2014/04/29]
                    raise StandardError()
                code |= self._state
                for _ in xrange(repeat):
                    yield Expression(code, press, release, kwargs)
                break
        self._clear_state()
        raise StopIteration()

    def iteranalyze(self, ):
        r"""SUMMARY

        iteranalyze()

        @Return:
        """
        self._iter = iter(self.tokens)
        code = None
        while 1:
            token = self._iter.next()
            # code
            if token.types in (TokenType.KEY, TokenType.BUTTON):
                code = token.get()
            # analyze in {}
            elif TokenType.CURLYSTART == token.types: # '{'
                for exp in self._iter_incurly():
                    yield exp
                continue
            # modifier
            elif TokenType.MODIFIER == token.types:
                self._state |= token
                continue
            if code is None:
                raise StandardError(token)
            code |= self._state
            yield Expression(code)
            # clear
            code = None
            self._clear_state()

    def __iter__(self, ):
        return iter(self.iteranalyze())

    def __repr__(self, ):
        return '{0.__class__.__name__}(tokens={0.tokens})'.format(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# analyze.py ends here
