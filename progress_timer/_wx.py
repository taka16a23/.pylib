#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _wx.py 467 2015-08-17 16:32:37Z t1 $
# $Revision: 467 $
# $Date: 2015-08-18 01:32:37 +0900 (Tue, 18 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-18 01:32:37 +0900 (Tue, 18 Aug 2015) $

r"""_wx -- DESCRIPTION

"""
import wx


class ProgressTimerWX(object):
    r"""ProgressTimerWX

    ProgressTimerWX is a object.
    Responsibility:
    """
    def __init__(self, title='Progress',
                 style=wx.PD_CAN_ABORT|wx.PD_ELAPSED_TIME|wx.PD_REMAINING_TIME):
        r"""

        @Arguments:
        - `title`:
        """
        self._title = title
        self.style = style

    def progress(self, sec, msg='Waiting'):
        r"""SUMMARY

        progress(msg='Remain ')

        @Arguments:
        - `msg`:

        @Return:

        @Error:
        """
        app = wx.PySimpleApp()
        dialog = wx.ProgressDialog(
            title=self._title, message=msg, maximum=sec,
            style=self.style)
        count = 0
        keepgoing = True
        while keepgoing and count < sec:
            count += 1
            wx.Sleep(1)
            keepgoing = dialog.Update(count)
        dialog.Destroy()

    def get_title(self, ):
        r"""SUMMARY

        get_title()

        @Return:

        @Error:
        """
        return self._title

    def set_title(self, title):
        r"""SUMMARY

        set_title(title)

        @Arguments:
        - `title`:

        @Return:

        @Error:
        """
        self._title = title

    title = property(get_title, set_title)

    def __call__(self, sec, msg='Waiting'):
        self.progress(sec, msg)




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _wx.py ends here
