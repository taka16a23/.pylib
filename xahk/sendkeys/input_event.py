#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""input_event -- DESCRIPTION

"""
from struct import pack
from enum import IntEnum as _IntEnum

from xcb import xproto
from xcb.xproto import EventMask

from xahk.x11.eventcode import EventCode
from xahk.x11.modifier import Modifier
from xahk.input.mouse import Mouse


class KeyEvent(object):
    r"""KeyEvent

    KeyEvent is a object.
    Responsibility:
    """
    def __init__(self, context, code, modifiers, point):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._context = context
        self.code = code
        self.modifiers = modifiers
        self.point = point

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._context.get('display')

    display = property(get_display)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._context.get('window')

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._context['window'] = window

    window = property(get_window, set_window)

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self.modifiers

    def set_modifiers(self, modifiers):
        r"""SUMMARY

        set_modifiers(modifiers)

        @Arguments:
        - `modifiers`:

        @Return:

        @Error:
        """
        self.modifiers = modifiers

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return abs(int(self.point.x))

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - `newx`:

        @Return:

        @Error:
        """
        self.point.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return abs(int(self.point.y))

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - `newy`:

        @Return:

        @Error:
        """
        self.point.set_y(newy)

    y = property(get_y, set_y)

    def get_keycode(self, ):
        r"""SUMMARY

        get_keycode()

        @Return:

        @Error:
        """
        return self.code

    def set_keycode(self, keycode):
        r"""SUMMARY

        set_keycode(keycode)

        @Arguments:
        - `keycode`:

        @Return:

        @Error:
        """
        self.code = keycode

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._context.get('time')

    def set_time(self, time):
        r"""SUMMARY

        set_time(time)

        @Arguments:
        - `time`:

        @Return:

        @Error:
        """
        self._context['time'] = time

    time = property(get_time, set_time)

    def get_root(self, ):
        r"""SUMMARY

        get_root()

        @Return:

        @Error:
        """
        return self._context['root']

    def set_root(self, root):
        r"""SUMMARY

        set_root(root)

        @Arguments:
        - `root`:

        @Return:

        @Error:
        """
        self._context['root'] = root

    root = property(get_root, set_root)

    def get_child(self, ):
        r"""SUMMARY

        get_child()

        @Return:

        @Error:
        """
        return self._context['child']

    def set_child(self, child):
        r"""SUMMARY

        set_child(child)

        @Arguments:
        - `child`:

        @Return:

        @Error:
        """
        self._context['child'] = child

    child = property(get_child, set_child)

    def get_samescreen(self, ):
        r"""SUMMARY

        get_samescreen()

        @Return:

        @Error:
        """
        return self._context.get('samescreen')

    def set_samescreen(self, samescreen):
        r"""SUMMARY

        set_samescreen(samescreen)

        @Arguments:
        - `samescreen`:

        @Return:

        @Error:
        """
        self._context['samescreen'] = samescreen

    samescreen = property(get_samescreen, set_samescreen)

    def get_rootx(self, ):
        r"""SUMMARY

        get_rootx()

        @Return:

        @Error:
        """
        return self._context.get('rootx')

    def set_rootx(self, rootx):
        r"""SUMMARY

        set_rootx(rootx)

        @Arguments:
        - `rootx`:

        @Return:

        @Error:
        """
        self._context['rootx'] = rootx

    rootx = property(get_rootx, set_rootx)

    def get_rooty(self, ):
        r"""SUMMARY

        get_rooty()

        @Return:

        @Error:
        """
        return self._context.get('rooty')

    def set_rooty(self, rooty):
        r"""SUMMARY

        set_rooty(rooty)

        @Arguments:
        - `rooty`:

        @Return:

        @Error:
        """
        self._context['rooty'] = rooty

    rooty = property(get_rooty, set_rooty)

    def get_sequence(self, ):
        r"""SUMMARY

        get_sequence()

        @Return:

        @Error:
        """
        return self._context.get('sequence')

    def set_sequence(self, sequence):
        r"""SUMMARY

        set_sequence(sequence)

        @Arguments:
        - `sequence`:

        @Return:

        @Error:
        """
        self._context['sequence'] = sequence

    sequence = property(get_sequence, set_sequence)

    def press(self, ):
        r"""SUMMARY

        press()

        @Return:

        @Error:
        """
        event = pack('BBH4I5HBx', EventCode.KeyPress, self.code, self.sequence,
                     self.time, self.root, self.window, self.child,
                     self.rootx, self.rooty, self.x, self.y, self.modifiers,
                     self.samescreen)
        return self.display.core.SendEventChecked(
            False, self.window, EventMask.KeyPress, event)

    def release(self, ):
        r"""SUMMARY

        release()

        @Return:

        @Error:
        """
        event = pack('BBH4I5HBx', EventCode.KeyRelease, self.code, self.sequence,
                     self.time, self.root, self.window, self.child,
                     self.rootx, self.rooty, self.x, self.y, self.modifiers,
                     self.samescreen)
        return self.display.core.SendEventChecked(
            False, self.window, EventMask.KeyRelease, event)


class ButtonEvent(object):
    r"""ButtonEvent

    ButtonEvent is a object.
    Responsibility:
    """
    _release_modifier = {Mouse.Button.Index.Left: Modifier.Mask.Left,
                         Mouse.Button.Index.Middle: Modifier.Mask.Middle,
                         Mouse.Button.Index.Right: Modifier.Mask.Right,
                         Mouse.Button.Index.WheelUp: Modifier.Mask.WheelUp,
                         Mouse.Button.Index.WheelDown: Modifier.Mask.WheelDown,
                         }

    def __init__(self, context, code, modifiers, point):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._context = context
        self.code = code
        self.modifiers = modifiers
        self.point = point

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._context.get('display')

    display = property(get_display)

    def get_window(self, ):
        r"""SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self._context.get('window')

    def set_window(self, window):
        r"""SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self._context['window'] = window

    window = property(get_window, set_window)

    def get_modifiers(self, ):
        r"""SUMMARY

        get_modifiers()

        @Return:

        @Error:
        """
        return self.modifiers

    def set_modifiers(self, modifiers):
        r"""SUMMARY

        set_modifiers(modifiers)

        @Arguments:
        - `modifiers`:

        @Return:

        @Error:
        """
        self.modifiers = modifiers

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:

        @Error:
        """
        return self.point.x

    def set_x(self, newx):
        r"""SUMMARY

        set_x(newx)

        @Arguments:
        - `newx`:

        @Return:

        @Error:
        """
        self.point.set_x(newx)

    x = property(get_x, set_x)

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:

        @Error:
        """
        return self.point.y

    def set_y(self, newy):
        r"""SUMMARY

        set_y(newy)

        @Arguments:
        - `newy`:

        @Return:

        @Error:
        """
        self.point.set_y(newy)

    y = property(get_y, set_y)

    def get_keycode(self, ):
        r"""SUMMARY

        get_keycode()

        @Return:

        @Error:
        """
        return self.code

    def set_keycode(self, keycode):
        r"""SUMMARY

        set_keycode(keycode)

        @Arguments:
        - `keycode`:

        @Return:

        @Error:
        """
        self.code = keycode

    def get_time(self, ):
        r"""SUMMARY

        get_time()

        @Return:

        @Error:
        """
        return self._context.get('time')

    def set_time(self, time):
        r"""SUMMARY

        set_time(time)

        @Arguments:
        - `time`:

        @Return:

        @Error:
        """
        self._context['time'] = time

    time = property(get_time, set_time)

    def get_root(self, ):
        r"""SUMMARY

        get_root()

        @Return:

        @Error:
        """
        return self._context['root']

    def set_root(self, root):
        r"""SUMMARY

        set_root(root)

        @Arguments:
        - `root`:

        @Return:

        @Error:
        """
        self._context['root'] = root

    root = property(get_root, set_root)

    def get_child(self, ):
        r"""SUMMARY

        get_child()

        @Return:

        @Error:
        """
        return self._context['child']

    def set_child(self, child):
        r"""SUMMARY

        set_child(child)

        @Arguments:
        - `child`:

        @Return:

        @Error:
        """
        self._context['child'] = child

    child = property(get_child, set_child)

    def get_samescreen(self, ):
        r"""SUMMARY

        get_samescreen()

        @Return:

        @Error:
        """
        return self._context.get('samescreen')

    def set_samescreen(self, samescreen):
        r"""SUMMARY

        set_samescreen(samescreen)

        @Arguments:
        - `samescreen`:

        @Return:

        @Error:
        """
        self._context['samescreen'] = samescreen

    samescreen = property(get_samescreen, set_samescreen)

    def get_rootx(self, ):
        r"""SUMMARY

        get_rootx()

        @Return:

        @Error:
        """
        return self._context.get('rootx')

    def set_rootx(self, rootx):
        r"""SUMMARY

        set_rootx(rootx)

        @Arguments:
        - `rootx`:

        @Return:

        @Error:
        """
        self._context['rootx'] = rootx

    rootx = property(get_rootx, set_rootx)

    def get_rooty(self, ):
        r"""SUMMARY

        get_rooty()

        @Return:

        @Error:
        """
        return self._context.get('rooty')

    def set_rooty(self, rooty):
        r"""SUMMARY

        set_rooty(rooty)

        @Arguments:
        - `rooty`:

        @Return:

        @Error:
        """
        self._context['rooty'] = rooty

    rooty = property(get_rooty, set_rooty)

    def get_sequence(self, ):
        r"""SUMMARY

        get_sequence()

        @Return:

        @Error:
        """
        return self._context.get('sequence')

    def set_sequence(self, sequence):
        r"""SUMMARY

        set_sequence(sequence)

        @Arguments:
        - `sequence`:

        @Return:

        @Error:
        """
        self._context['sequence'] = sequence

    sequence = property(get_sequence, set_sequence)

    def press(self, ):
        r"""SUMMARY

        press()

        @Return:

        @Error:
        """
        # return self._xtest.FakeInputChecked(
            # EventCode.ButtonPress, self.code, self.time, self.root, self.x, self.y, 0)
        event = pack('BBH4I5HBx', EventCode.ButtonPress, self.code, self.sequence,
                     self.time, self.root, self.window, self.child,
                     self.rootx, self.rooty, self.x, self.y, self.modifiers,
                     self.samescreen)
        return self.display.core.SendEventChecked(
            False, self.window, EventMask.ButtonPress, event)

    def release(self, ):
        r"""SUMMARY

        release()

        @Return:

        @Error:
        """
        # return self._xtest.FakeInputChecked(
            # EventCode.ButtonRelease, self.code, self.time, self.root, self.x, self.y, 0)
        event = pack('BBH4I5HBx', EventCode.ButtonRelease, self.code, self.sequence,
                     self.time, self.root, self.window, self.child,
                     self.rootx, self.rooty, self.x, self.y,
                     self.modifiers|self._release_modifier.get(self.code, 0),
                     self.samescreen)
        return self.display.core.SendEventChecked(
            False, self.window, EventMask.ButtonRelease, event)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# input_event.py ends here
