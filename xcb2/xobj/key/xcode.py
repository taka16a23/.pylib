#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: xcode.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

import xcb2
import keysym


class Code(int):
    r"""Code

    Code is a int.
    Responsibility:
    """
    def __repr__(self):
        return '{0.__class__.__name__}({0})'.format(self)


class KeyCode(Code):
    """Class KeyCode
    """

    # Operations
    def press(self, propagate, window, sequence_number, time, child, rootx,
              rooty, eventx, eventy, state, samescreen, display=None):
        """function press

        @Arguments:
        - `conn`:
        - `propagate`:
        - `window`:
        - `sequence_number`:
        - `time`:
        - `child`:
        - `rootx`:
        - `rooty`:
        - `eventx`:
        - `eventy`:
        - `state`:
        - `samescreen`:

        @Return:
        """
        conn = xcb2.connect(display=display)
        return conn.core.SendEvent.KeyPress(
            propagate, window, self, sequence_number, time, self,
            child, rootx, rooty, eventx, eventy, state, samescreen)

    def release(self, propagate, window, sequence_number, time, child, rootx,
                rooty, eventx, eventy, state, samescreen, display=None):
        """function release

        window:
        state:
        time:
        child:
        rootx:
        rooty:
        eventx:
        evnety:
        samescreen:
        propagate:
        display:

        returns
        """
        conn = xcb2.connect(display=display)
        return conn.core.SendEvent.KeyRelease(
            propagate, window, self, sequence_number, time, self,
            child, rootx, rooty, eventx, eventy, state, samescreen)

    def grab(self, owner_events, window, modifiers, display=None):
        """function grab

        window: int
        mod: int
        display: str

        returns
        """
        conn = xcb2.connect(display=display)
        return conn.core.GrabKey.async(owner_events, window, modifiers, self)

    def ungrab(self, window, modifiers, display=None):
        """function ungrab

        window:
        mod:
        display: str

        returns
        """
        conn = xcb2.connect(display=display)
        return conn.core.UngrabKey(self, window, modifiers)

    def to_keysym(self, modifiers, display=None):
        """function to_keysym

        mod:
        display: str

        returns
        """
        index = 0
        if bool(modifiers & 1):
            index += 1
        if bool(modifiers & 8):
            index += 2
        maps = keysym.Keysym.getmapping().get(display)
        return maps.code_to_sym(self, index)


class ButtonCode(Code):
    """Class ButtonCode
    """
    # Attributes:

    # Operations
    def press(self, conn, window, state, time, child, rootx, rooty,
              eventx, eventy, samescreen, propagate):
        """function press

        window:
        state:
        time:
        child:
        rootx:
        rooty:
        eventx:
        eventy:
        samescreen:
        propagate:
        display:

        returns
        """
        return None # should raise NotImplementedError()

    def release(self, conn, window, state, time, child, rootx, rooty,
                eventx, evnety, samescreen, propagate):
        """function release

        window:
        state:
        time:
        child:
        rootx:
        rooty:
        eventx:
        evnety:
        samescreen:
        propagate:
        display:

        returns
        """
        return None # should raise NotImplementedError()

    def grabpress(self, conn, window, mod, owner_events, confine_to, cursor,
                  pointer_mode, keyboard_mode):
        """function grabpress

        window:
        mod:
        owner_events:
        confine_to:
        cursor:
        pointer_mode:
        keyboard_mode:
        display: str

        returns
        """
        return None # should raise NotImplementedError()

    def grabrelease(self, conn, window, mod, owner_events, confine_to,
                    cursor, pointer_mode, keyboard_mode):
        """function grabrelease

        window:
        mod:
        owner_events:
        confine_to:
        cursor:
        pointer_mode:
        keyboard_mode:
        display: str

        returns
        """
        return None # should raise NotImplementedError()

    def ungrab(self, window, mod):
        """function ungrab

        window:
        mod:
        display: str

        returns
        """
        return None # should raise NotImplementedError()

    def motionnotify(self):
        """function motionnotify

        returns
        """
        return None # should raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# code.py ends here
