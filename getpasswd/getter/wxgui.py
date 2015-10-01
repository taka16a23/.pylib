#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""getter -- DESCRIPTION

"""
from getpasswd.getter.abstract import PassGetter

import wx
from peak.rules import dispatch


class WXPassGetter(PassGetter):
    r"""WPassGetter

    WXPassGetter is a PassGetter.
    Responsibility:
    """
    def __init__(self, title='Enter Password', default='', *args, **kwargs):
        r"""

        @Arguments:
        - `title`:
        - `default`:
        """
        self._title = title
        self._default = default
        self._point = wx.Point(0, 0)
        self.setpoint(*args, **kwargs)

    def gettitle(self, ):
        r"""SUMMARY

        gettitle()

        @Return:

        @Error:
        """
        return self._title

    def settitle(self, title='Enter Password'):
        r"""SUMMARY

        settitle(title='Enter Password')

        @Arguments:
        - `title`:

        @Return:

        @Error:
        """
        self._title = title

    def getdefault(self, ):
        r"""SUMMARY

        getdefault()

        @Return:

        @Error:
        """
        return self._default

    def setdefault(self, default=''):
        r"""SUMMARY

        setdefault(default='')

        @Arguments:
        - `default`:

        @Return:

        @Error:
        """
        self._default = default

    def getpoint(self, ):
        r"""SUMMARY

        getpoint()

        @Return:

        @Error:
        """
        return self._point

    @dispatch.generic()
    def setpoint(self, *args, **kwargs):
        r"""SUMMARY

        setpoint(x=None, y=None)
        setpoint(x=10)
        setpoint(y=100)
        setpoint(1000, 300)
        setpoint(x=500, y=200)
        setpoint(wx.Point(2000, 500))

        @Arguments:
        - `x`:
        - `y`:

        @Return:

        @Error:
        """
        pass

    @setpoint.when('len(args) == 0 and len(kwargs) == 0')
    def __setpoint_novalue(self, *args, **kwargs):
        r"""SUMMARY

        __setpoint_novalue(*args, **kwargs)

        @Arguments:
        - `args`:
        - `kwargs`:

        @Return:

        @Error:
        """
        self.setpoint(0, 0)

    @setpoint.when('len(args) == 1 and isinstance(args[0], wx.Point)')
    def __setpoint_point(self, *args, **kwargs):
        r"""SUMMARY

        setpoint_point(*args, **kwargs)

        @Arguments:
        - `args`:
        - `kwargs`:

        @Return:

        @Error:
        """
        self._point = args[0]

    @setpoint.when('len(args) == 2')
    def __setpoint_xy(self, *args, **kwargs):
        r"""SUMMARY

        setpoint_xy()

        @Return:

        @Error:
        """
        self._point.Set(args[0], args[1])

    @setpoint.when('"x" in kwargs or "y" in kwargs')
    def __setpoint_xy_kwargs(self, *args, **kwargs):
        r"""SUMMARY

        setpoint_xy_kwargs(*args, **kwargs)

        @Arguments:
        - `args`:
        - `kwargs`:

        @Return:

        @Error:
        """
        x, y = kwargs.get('x', None), kwargs.get('y', None)
        if x is None:
            x = self._point.Get()[0]
        if y is None:
            y = self._point.Get()[1]
        self._point.Set(x, y)

    def getpass(self, prompt='Enter Password'):
        r"""SUMMARY

        getpass(prompt='Enter Password')

        @Arguments:
        - `prompt`:

        @Return:

        @Error:
        """
        app = wx.App(False)
        box2 = wx.TextEntryDialog(
            parent=None, message=prompt, caption=self._title,
            defaultValue=self._default,
            style=wx.TE_PASSWORD|wx.OK|wx.CANCEL,
            pos=self._point)
        pwd = ''
        if box2.ShowModal() == wx.ID_OK:
            pwd = box2.GetValue()
        box2.Destroy()
        app.MainLoop()
        return pwd



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getter.py ends here
