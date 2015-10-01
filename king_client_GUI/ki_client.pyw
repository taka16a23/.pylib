#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""\
Name: ki_client.py

"""


__version__ = '0.1.0'

import wx
from myframe.ki_server_client import KiServerClient

class KiGUI(wx.App):
    """
    """

    def OnInit(self):
        """SUMMARY

        @Return:
        """
        self.m_frame = KiServerClient(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

app = KiGUI(0)
app.MainLoop()






# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ki_client.py ends here
