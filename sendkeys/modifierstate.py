#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: modifierstate.py 182 2014-05-10 12:15:31Z t1 $
# $Revision: 182 $
# $Date: 2014-05-10 21:15:31 +0900 (Sat, 10 May 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-05-10 21:15:31 +0900 (Sat, 10 May 2014) $

r"""Modifier State -- a parts of sendkeys

"""
from struct import pack as _pack

from bitflag import BitFlagAbstract, BitFlag16

from xcb2.xproto import NamedModifierMask


class ModifierState(BitFlagAbstract):
    r"""Modifier Mask State Handler.

    ModifierMask from xcb2.xproto.NamedModifierMask

    All ModifierMask:
    Shift, Lock, Control, Alt, Numlock, Hiper, Super, Mod5,
    Left, Middle, Right, WheelUp, WheelDown, Any
    """

    def __init__(self, state=0):
        r"""Modifier Mask State Handler.

        @Arguments:
        - `state`: (int)

        ModifierState(state=0)
        """
        self.flags = BitFlag16(state)

    def pack(self, ):
        r"""Convert state to C short structs.

        @Return:
        (str)

        pack()

        >>> ModifierState(1).pack()
        '\x01\x00'
        """
        return _pack('H', self)

    def clear(self, ):
        r"""Clear state to 0.

        @Return:
        None

        clear()

        >>> state = ModifierState(1)
        >>> state.clear()
        >>> state == ModifierState(0)
        True
        """
        self.flags.clear()

    def setshift(self, ):
        r"""Set shift modifier mask.

        @Return:
        None

        setshift()

        >>> state = ModifierState(0)
        >>> state.setshift()
        >>> state.isshift()
        True
        """
        # NamedModifierMask.Shift
        self.flags.set1()

    def setlock(self, ):
        r"""Set lock modifier mask.

        @Return:
        None

        setlock()

        >>> state = ModifierState(0)
        >>> state.setlock()
        >>> state.islock()
        True
        """
        # NamedModifierMask.Lock
        self.flags.set2()

    def setcontrol(self, ):
        r"""Set control modifier mask.

        @Return:
        None

        setcontrol()

        >>> state = ModifierState(0)
        >>> state.setcontrol()
        >>> state.iscontrol()
        True
        """
        # NamedModifierMask.Control
        self.flags.set3()

    def setalt(self, ):
        r"""Set alt modifier mask.

        @Return:
        None

        setalt()

        >>> state = ModifierState(0)
        >>> state.setalt()
        >>> state.isalt()
        True
        """
        # NamedModifierMask.Alt
        self.flags.set4()

    def setnumlock(self, ):
        r"""Set numlock modifier mask.

        @Return:
        None

        setnumlock()

        >>> state = ModifierState(0)
        >>> state.setnumlock()
        >>> state.isnumlock()
        True
        """
        # NamedModifierMask.Numlock
        self.flags.set5()

    def sethiper(self, ):
        r"""Set hiper modifier mask.

        @Return:
        None

        sethiper()

        >>> state = ModifierState(0)
        >>> state.sethiper()
        >>> state.ishiper()
        True
        """
        # NamedModifierMask.Hiper
        self.flags.set6()

    def setsuper(self, ):
        r"""Set super modifier mask.

        @Return:
        None

        setsuper()

        >>> state = ModifierState(0)
        >>> state.setsuper()
        >>> state.issuper()
        True
        """
        # NamedModifierMask.Super
        self.flags.set7()

    def setmod5(self, ):
        r"""Set mod5 modifier mask.

        @Return:
        None

        setmod5()

        >>> state = ModifierState(0)
        >>> state.setmod5()
        >>> state.ismod5()
        True
        """
        # NamedModifierMask.Mod5
        self.flags.set8()

    def setleft(self, ):
        r"""Set left modifier mask.

        @Return:
        None

        setleft()

        >>> state = ModifierState(0)
        >>> state.setleft()
        >>> state.isleft()
        True
        """
        # NamedModifierMask.Left
        self.flags.set9()

    def setmiddle(self, ):
        r"""Set middle modifier mask.

        @Return:
        None

        setmiddle()

        >>> state = ModifierState(0)
        >>> state.setmiddle()
        >>> state.ismiddle()
        True
        """
        # NamedModifierMask.Middle
        self.flags.set10()

    def setright(self, ):
        r"""Set right modifier mask.

        @Return:
        None

        setright()

        >>> state = ModifierState(0)
        >>> state.setright()
        >>> state.isright()
        True
        """
        # NamedModifierMask.Right
        self.flags.set11()

    def setwheelup(self, ):
        r"""Set wheelup modifier mask.

        @Return:
        None

        setwheelup()

        >>> state = ModifierState(0)
        >>> state.setwheelup()
        >>> state.iswheelup()
        True
        """
        # NamedModifierMask.WheelUp
        self.flags.set12()

    def setwheeldown(self, ):
        r"""Set wheeldown modifier mask.

        @Return:
        None

        setwheeldown()

        >>> state = ModifierState(0)
        >>> state.setwheeldown()
        >>> state.iswheeldown()
        True
        """
        # NamedModifierMask.WheelDown
        self.flags.set13()

    def setany(self, ):
        r"""Set any modifier mask.

        @Return:
        None

        setany()

        >>> state = ModifierState(0)
        >>> state.setany()
        >>> state.isany()
        True
        """
        # NamedModifierMask.Any
        self.flags.set16()

    def resetshift(self, ):
        r"""Reset shift modifier mask.

        @Return:
        None

        resetshift()

        >>> state = ModifierState(40959) # set all
        >>> state.setshift()
        >>> state.isshift()
        False
        """
        self.flags.reset1()

    def resetlock(self, ):
        r"""Reset lock modifier mask.

        @Return:
        None

        resetlock()

        >>> state = ModifierState(40959) # set all
        >>> state.setlock()
        >>> state.islock()
        False
        """
        self.flags.reset2()

    def resetcontrol(self, ):
        r"""Reset control modifier mask.

        @Return:
        None

        resetcontrol()

        >>> state = ModifierState(40959) # set all
        >>> state.setcontrol()
        >>> state.iscontrol()
        False
        """
        self.flags.reset3()

    def resetalt(self, ):
        r"""Reset alt modifier mask.

        @Return:
        None

        resetalt()

        >>> state = ModifierState(40959) # set all
        >>> state.setalt()
        >>> state.isalt()
        False
        """
        self.flags.reset4()

    def resetnumlock(self, ):
        r"""Reset numlock modifier mask.

        @Return:
        None

        resetnumlock()

        >>> state = ModifierState(40959) # set all
        >>> state.setnumlock()
        >>> state.isnumlock()
        False
        """
        self.flags.reset5()

    def resethiper(self, ):
        r"""Reset hiper modifier mask.

        @Return:
        None

        resethiper()

        >>> state = ModifierState(40959) # set all
        >>> state.sethiper()
        >>> state.ishiper()
        False
        """
        self.flags.reset6()

    def resetsuper(self, ):
        r"""Reset super modifier mask.

        @Return:
        None

        resetsuper()

        >>> state = ModifierState(40959) # set all
        >>> state.setsuper()
        >>> state.issuper()
        False
        """
        self.flags.reset7()

    def resetmod5(self, ):
        r"""Reset mod5 modifier mask.

        @Return:
        None

        resetmod5()

        >>> state = ModifierState(40959) # set all
        >>> state.setmod5()
        >>> state.ismod5()
        False
        """
        self.flags.reset8()

    def resetleft(self, ):
        r"""Reset left modifier mask.

        @Return:
        None

        resetleft()

        >>> state = ModifierState(40959) # set all
        >>> state.setleft()
        >>> state.isleft()
        False
        """
        self.flags.reset9()

    def resetmiddle(self, ):
        r"""Reset middle modifier mask.

        @Return:
        None

        resetmiddle()

        >>> state = ModifierState(40959) # set all
        >>> state.setmiddle()
        >>> state.ismiddle()
        False
        """
        self.flags.reset10()

    def resetright(self, ):
        r"""Reset right modifier mask.

        @Return:
        None

        resetright()

        >>> state = ModifierState(40959) # set all
        >>> state.setright()
        >>> state.isright()
        False
        """
        self.flags.reset11()

    def resetwheelup(self, ):
        r"""Reset wheelup modifier mask.

        @Return:
        None

        resetwheelup()

        >>> state = ModifierState(40959) # set all
        >>> state.setwheelup()
        >>> state.iswheelup()
        False
        """
        self.flags.reset12()

    def resetwheeldown(self, ):
        r"""Reset wheeldown modifier mask.

        @Return:
        None

        resetwheeldown()

        >>> state = ModifierState(40959) # set all
        >>> state.setwheeldown()
        >>> state.iswheeldown()
        False
        """
        self.flags.reset13()

    def resetany(self, ):
        r"""Reset any modifier mask.

        @Return:
        None

        resetany()

        >>> state = ModifierState(40959) # set all
        >>> state.setany()
        >>> state.isany()
        False
        """
        self.flags.reset16()

    def isshift(self, ):
        r"""Check is setted shift modifier mask.

        @Return:
        None

        setshift()

        >>> state = ModifierState(0)
        >>> state.setshift()
        >>> state.isshift()
        True
        """
        return self.flags.isflaged1()

    def islock(self, ):
        r"""Check is setted lock modifier mask.

        @Return:
        None

        setlock()

        >>> state = ModifierState(0)
        >>> state.setlock()
        >>> state.islock()
        True
        """
        return self.flags.isflaged2()

    def iscontrol(self, ):
        r"""Check is setted control modifier mask.

        @Return:
        None

        setcontrol()

        >>> state = ModifierState(0)
        >>> state.setcontrol()
        >>> state.iscontrol()
        True
        """
        return self.flags.isflaged3()

    def isalt(self, ):
        r"""Check is setted alt modifier mask.

        @Return:
        None

        setalt()

        >>> state = ModifierState(0)
        >>> state.setalt()
        >>> state.isalt()
        True
        """
        return self.flags.isflaged4()

    def isnumlock(self, ):
        r"""Check is setted numlock modifier mask.

        @Return:
        None

        setnumlock()

        >>> state = ModifierState(0)
        >>> state.setnumlock()
        >>> state.isnumlock()
        True
        """
        return self.flags.isflaged5()

    def ishiper(self, ):
        r"""Check is setted hiper modifier mask.

        @Return:
        None

        sethiper()

        >>> state = ModifierState(0)
        >>> state.sethiper()
        >>> state.ishiper()
        True
        """
        return self.flags.isflaged6()

    def issuper(self, ):
        r"""Check is setted super modifier mask.

        @Return:
        None

        setsuper()

        >>> state = ModifierState(0)
        >>> state.setsuper()
        >>> state.issuper()
        True
        """
        return self.flags.isflaged7()

    def ismod5(self, ):
        r"""Check is setted mod5 modifier mask.

        @Return:
        None

        setmod5()

        >>> state = ModifierState(0)
        >>> state.setmod5()
        >>> state.ismod5()
        True
        """
        return self.flags.isflaged8()

    def isleft(self, ):
        r"""Check is setted left modifier mask.

        @Return:
        None

        setleft()

        >>> state = ModifierState(0)
        >>> state.setleft()
        >>> state.isleft()
        True
        """
        return self.flags.isflaged9()

    def ismiddle(self, ):
        r"""Check is setted middle modifier mask.

        @Return:
        None

        setmiddle()

        >>> state = ModifierState(0)
        >>> state.setmiddle()
        >>> state.ismiddle()
        True
        """
        return self.flags.isflaged10()

    def isright(self, ):
        r"""Check is setted right modifier mask.

        @Return:
        None

        setright()

        >>> state = ModifierState(0)
        >>> state.setright()
        >>> state.isright()
        True
        """
        return self.flags.isflaged11()

    def iswheelup(self, ):
        r"""Check is setted wheelup modifier mask.

        @Return:
        None

        setwheelup()

        >>> state = ModifierState(0)
        >>> state.setwheelup()
        >>> state.iswheelup()
        True
        """
        return self.flags.isflaged12()

    def iswheeldown(self, ):
        r"""Check is setted wheeldown modifier mask.

        @Return:
        None

        setwheeldown()

        >>> state = ModifierState(0)
        >>> state.setwheeldown()
        >>> state.iswheeldown()
        True
        """
        return self.flags.isflaged13()

    def isany(self, ):
        r"""Check is setted any modifier mask.

        @Return:
        None

        setany()

        >>> state = ModifierState(0)
        >>> state.setany()
        >>> state.isany()
        True
        """
        return self.flags.isflaged16()

    def __iter__(self, ):
        yield self.__class__(0)
        for mod in NamedModifierMask:
            if self & mod:
                yield self.__class__(mod)
        raise StopIteration()

    def __repr__(self, ):
        fmt = '{0.__class__.__name__}({1}, "{2}", {3})'.format
        return fmt(self, int(self), self.flags,
                   [str(NamedModifierMask(mod)).split('.')[1]
                    for mod in self if mod])

    def __str__(self, ):
        return '<{0} {1}>'.format(
            int(self), [str(NamedModifierMask(mod)).split('.')[1]
                        for mod in self if mod])



# For Emacs
# Local Variables:
# coding: utf-8
# no-check-type-miss: t
# End:
# state.py ends here
