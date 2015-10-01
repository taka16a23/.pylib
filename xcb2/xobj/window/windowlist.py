#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: windowlist.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""windowlist -- DESCRIPTION

"""
import re
from predicate import iscallable
from dotavoider import ListDotAvoider
from t1.listutil import OneTypeList

from xcb2.logger import LOG
from xcb2.xproto import BadWindow
from xcb2.xobj.window.window import Window
from xcb2.xobj.window.windowtypes import WindowUnknownType


class WindowList(OneTypeList):
    r"""SUMMARY
    """
    types = Window

    def to_types(self, ):
        r"""SUMMARY

        convert_typs()

        @Return:
        """
        lis, append = ListDotAvoider().append
        for win in self:
            try:
                append(win.get_net_wm_window_type())
            except BadWindow as err:
                LOG.warn('Warning {}'.format(err))
        return WindowTypesList(lis)


class WindowTypesList(OneTypeList):
    r"""SUMMARY
    """
    types = WindowUnknownType
    viewfmt = ('Window({0.window.id}, "{0.name}", '
               '("{0.wmclass.res_name}", "{0.wmclass.res_class}"))')

    def filter_name(self, name):
        r"""Filter windows by title name.

        @Arguments:
        - `name`: (str) window title name.

        @Return:
        WindowList

        filter_name(name)

        name is '_NET_WM_NAME' window properties.
        """
        lis, append = ListDotAvoider().append
        for win in self:
            try:
                if name == win.name:
                    append(win)
            except BadWindow as err:
                LOG.warn('Warning {}'.format(err))
                continue
        return self.__class__(lis)

    def filter_wmclass(self, wmclass):
        r"""Filter windows by window class.

        @Arguments:
        - `wmclass`: (str) window class.

        @Return:
        WindowList

        filter_wmclass(wmclass)

        wmclass is 'WM_CLASS' window properties.
        """
        lis, append = ListDotAvoider().append
        for win in self:
            try:
                if wmclass in win.wmclass:
                    append(win)
            except BadWindow as err:
                LOG.warn('Warning {}'.format(err))
                continue
        return self.__class__(lis)

    def filter_types(self, types):
        r"""Filter windows by window types.

        @Arguments:
        - `types`: (int or string or AtomPair)

        @Return:
        WindowList

        filter_types(types)

        types is '_NET_WM_WINDOW_TYPE' window properties.
        """
        return self.__class__([x for x in self if types == x.types])

    def filter_func(self, bool_func):
        r"""Filter windows by boolean function.

        @Arguments:
        - `bool_func`: (func) boolean function.

        @Return:
        WindowList

        filter_func(bool_func)
        """
        if not iscallable(bool_func):
            # TODO: (Atami) [2014/05/01]
            raise StandardError()
        return self.__class__([x for x in self if bool_func(x)])

    def filter_regexp_name(self, regexp):
        r"""SUMMARY

        filter_regexp_name(regexp)

        @Arguments:
        - `regexp`:

        @Return:
        """
        search = re.compile(regexp).search
        lis, append = ListDotAvoider().append
        for win in self:
            try:
                if search(win.name) is not None:
                    append(win)
            except BadWindow as err:
                LOG.warn('Warning {}'.format(err))
                continue
        return self.__class__(lis)

    def filter_regexp_wmclass(self, regexp):
        r"""SUMMARY

        filter_regexp_wmclass(regexp)

        @Arguments:
        - `regexp`:

        @Return:
        """
        search = re.compile(regexp).search
        lis, append = ListDotAvoider().append
        for win in self:
            try:
                if (search(win.wmclass.res_name) is not None or
                    search(win.wmclass.res_class) is not None):
                    append(win)
            except BadWindow as err:
                LOG.warn('Warning {}'.format(err))
                continue
        return self.__class__(lis)

    def set_attributes(self, value_list):
        r"""SUMMARY

        set_attributes(value_list)

        @Arguments:
        - `value_list`:

        @Return:
        """
        for win in self:
            win.set_attributes(value_list)

    def view(self, ):
        r"""SUMMARY

        view()

        @Return:
        """
        print(
            '[{}]'.format(',\n '.join([self.viewfmt.format(x) for x in self])))

    def __repr__(self, ):
        return '{0.__class__.__name__}({1})'.format(
            self, super(WindowTypesList, self).__repr__())

    def __add__(self, other):
        return self.__class__(set(list(self) + list(other)))

    def __iadd__(self, other):
        self[:] = (self + other)[:]
        return self

    def __sub__(self, other):
        return self.__class__(set(self) - set(other))

    def __isub__(self, other):
        self[:] = (self - other)[:]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# windowlist.py ends here
