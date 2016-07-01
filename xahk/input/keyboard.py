#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""keyboard -- DESCRIPTION

"""
from xcb import xtest
from xcb.xproto import Time
from peak.rules import dispatch

from xahk.x11.display import Display
from xahk.x11.eventcode import EventCode

from .keysymdef import Keysym


class Keyboard(object):
    """Keyboard

    Keyboard is a object.
    Responsibility:
    """

    class Key(object):
        """Key

        Key is a object.
        Responsibility:
        """
        __slots__ = ('display', '_xtest', 'root', 'code', 'sym', 'shiftsym', )

        def __init__(self, display, code, sym=None, shiftsym=None):
            """

            @Arguments:
            - `args`:
            - `kwargs`:
            """
            self.display = display
            self._xtest = self.display(xtest.key)
            self.root = self.display.get_setup().roots[0].root
            self.code = code
            self.sym = sym
            self.shiftsym = shiftsym

        def get_display(self, ):
            """SUMMARY

            get_display()

            @Return:

            @Error:
            """
            return self.display

        def get_code(self, ):
            """SUMMARY

            get_code()

            @Return:

            @Error:
            """
            return self.code

        def get_label(self, ):
            """SUMMARY

            get_label()

            @Return:

            @Error:
            """
            if self.sym is None:
                return u''
            return unicode(self.sym.to_char() or self.sym.to_name())

        label = property(get_label)

        def get_shift_label(self, ):
            """SUMMARY

            get_shift_label()

            @Return:

            @Error:
            """
            if self.shiftsym is None:
                return u''
            return unicode(self.shiftsym.to_char() or self.shiftsym.to_name())

        shift_label = property(get_shift_label)

        def is_labeled(self, label):
            """SUMMARY

            is_labeled(label)

            @Arguments:
            - `label`:

            @Return:

            @Error:
            """
            return label in (self.label, self.shift_label)

        def _fake_input_checked(self, type, point):
            """SUMMARY

            _fake_input_checked(type, time, root_x, root_y)

            @Arguments:
            - `type`:
            - `time`:
            - `root_x`:
            - `root_y`:

            @Return:

            @Error:
            """
            return self._xtest.FakeInputChecked(
                type, self.code, Time.CurrentTime, self.root,
                int(point.x), int(point.y), 0)

        def press(self, point):
            """SUMMARY

            press(time, root_x, root_y)

            @Arguments:
            - `time`:
            - `root_x`:
            - `root_y`:

            @Return:

            @Error:
            """
            return self._fake_input_checked(EventCode.KeyPress, point)

        def release(self, point):
            """SUMMARY

            release(point)

            @Arguments:
            - `time`:
            - `root_x`:
            - `root_y`:

            @Return:

            @Error:
            """
            return self._fake_input_checked(EventCode.KeyRelease, point)

        # def __repr__(self):
        #     string = u''
        #     string += unicode(self.__class__.__name__)
        #     string += u'(code=' + unicode(self.code) + u', '
        #     string += u'label=' + unicode(str(self.label)) + u', '
        #     string += u'shift_label=' + unicode(self.shift_label) + u')'
        #     return string
            # return (u'{0.__class__.__name__}'
            #         u'(code={0.code}, label={1}, shift_label={2})'
            #         ).format(self, unicode(repr(self.label)),
            #                  repr(self.shift_label).decode('utf-8'))

    def __init__(self, ):
        """

        @Arguments:
        - `display`:
        """
        self.display = Display()
        self.keys = []
        self.modifiers = []
        self.shift_keys = []
        self._load()

    def get_display(self, ):
        """SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.display

    def _load(self, ):
        """SUMMARY

        _load()

        @Return:

        @Error:
        """
        setup = self.display.get_setup()
        mincode, maxcode = int(setup.min_keycode), int(setup.max_keycode)
        count = maxcode - mincode + 1
        rep = self.display.core.GetKeyboardMapping(mincode, count).reply()
        keymapping = zip(*[iter(rep.keysyms)] * rep.keysyms_per_keycode)
        append = self.keys.append
        for keycode, symcodes in enumerate(keymapping, start=mincode):
            append(self.Key(self.display, keycode,
                            sym=Keysym(symcodes[0]),
                            shiftsym=Keysym(symcodes[1])))
        # load modifiers
        shift_keys = ('Shift_L', 'Shift_R')
        modifiers = ('Control_L', 'Control_R', 'Meta_L', 'Meta_R', 'Alt_L',
                     'Alt_R', 'Super_L', 'Super_R', 'Hyper_L') + shift_keys
        for key in self.keys:
            if key.get_label() in modifiers:
                self.modifiers.append(key)
            if key.get_label() in shift_keys:
                self.shift_keys.append(key)

    def list_keys(self, ):
        """SUMMARY

        list_keys()

        @Return:

        @Error:
        """
        return self.keys[:]

    def list_modifiers(self, ):
        """SUMMARY

        list_modifiers()

        @Return:

        @Error:
        """
        return self.modifiers[:]

    def get_shift_key(self, ):
        """SUMMARY

        get_shift_key()

        @Return:

        @Error:
        """
        return self.shift_keys[0]

    @dispatch.generic()
    def get_key(self, value):
        """SUMMARY

        get_key(value)

        @Return:

        @Error:
        """

    @get_key.when('isinstance(value, basestring)')
    def get_key_str(self, value):
        """SUMMARY

        get_key(label)

        @Arguments:
        - `label`:

        @Return:

        @Error:
        """
        for key in self.list_keys():
            if key.is_labeled(value):
                return key
        return None

    @get_key.when('isinstance(value, int)')
    def get_key_code(self, value):
        """SUMMARY

        get_key_code(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        for key in self.list_keys():
            if value == key.get_code():
                return key
        return None

    @get_key.when('isinstance(value, Keysym)')
    def get_key_sym(self, value):
        """SUMMARY

        get_key_sym(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        for key in self.list_keys():
            if value in (key.sym, key.shiftsym):
                return key
        return None



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keyboard.py ends here
