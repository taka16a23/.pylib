# -*- coding: utf-8 -*-
#
# $Id: ki_server_client.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
"""Subclass of KiServerClient, which is generated by wxFormBuilder."""

import socket
import wx
from myframe import ki_server_client_frame
import pyping
from ref.myinfo import king
from wakeonlan import wakeonlan

HOST = king.IP
PORT = 65535
BUFSIZE = 1024
ADDR = (HOST, PORT)
MAC = king.MAC

class MyProgressDialog(wx.ProgressDialog):
    """Progress Dialog for wait response from server."""

    def __init__(self, text, sec):
        """

        Arguments:
        - `sec`:
        """
        self.text = text
        self.sec = sec
        wx.ProgressDialog.__init__(self, 'Waiting', self.text, self.sec,
                                   style=wx.PD_REMAINING_TIME|wx.PD_AUTO_HIDE)

    def Show(self, *args, **kwargs):
        """SUMMARY

        @Return:
        """
        keepGoing = True
        count = 0
        while keepGoing and count < self.sec:
            count = count + 1
            wx.Sleep(1)
            keepGoing = self.Update(count)

# Implementing KiServerClient
class KiServerClient(ki_server_client_frame.KiServerClient):
    def __init__(self, parent):
        ki_server_client_frame.KiServerClient.__init__(self, parent)
        if king_isactive():
            self._show_active_msg()

    # Handlers for KiServerClient events.
    def wol(self, event):
        # check active
        if self.isactive():
            self._show_active_msg()
            wx.MessageBox(u'既に起動中です。')
            return

        # wol
        self.show_minor_msg(u'送信中')
        self.halt_button.Disable()
        self.close_button.Disable()

        wakeonlan(MAC)
        self.wait_with_daialog(u'起動するまで..', 70)

        # check active
        if self.isactive():
            self._show_active_msg()
        else:
            self._show_inactive_msg()
        self.halt_button.Enable()
        self.close_button.Enable()


    def halt(self, event):
        if self.isactive():
            self._halt()

        if self.isactive():
            self._show_inactive_msg()

    def _halt(self):
        """SUMMARY

        @Return:
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        try:
            sock.sendto('halt', ADDR)
            recved, addr = sock.recvfrom(BUFSIZE)
            if recved == 'accept':
                self.wait_with_daialog(u'コマンド送信中..', 7)
            if recved == 'using':
                self._show_active_msg()
                wx.MessageBox(u'他のユーザーが使用中です。\n')
                return
        except socket.timeout:
            pass



    def exit(self, event):
        if self.isactive() is True:
            # show dialog
            answer = wx.MessageBox(
                u'サーバーが起動中です。\nサーバーの電源を切りますか？',
                'Caption',
                wx.YES|wx.NO|wx.CANCEL)
            if answer == wx.YES:
                self._halt()
                self.wait_with_daialog(u'コマンド送信中..', 7)
            elif answer == wx.CANCEL:
                return
        self.Close()

    def wait_with_daialog(self, text, sec=10):
        """SUMMARY

        @Arguments:

        - `sec`:
        - `text`:

        @Return:
        """
        dialog = MyProgressDialog(text, sec)
        dialog.SetSize((250, 150))
        dialog.Show()
        dialog.Destroy()

    def isactive(self):
        """SUMMARY

        @Return:
        """
        self.show_minor_msg(u'確認中')
        if king_isactive() is True:
            self._show_active_msg()
            return True
        else:
            self._show_inactive_msg()
            return False

    def _show_inactive_msg(self):
        self.m_staticText2.SetLabel(u'停止中')
        self.m_staticText2.SetFont(wx.Font(18, 70, 90, 92, False,
                                            wx.EmptyString ) )
        self.m_staticText2.SetForegroundColour( wx.Colour( 128, 128, 128 ) )

    def _show_active_msg(self):
        """SUMMARY

        @Return:
        """
        self.m_staticText2.SetLabel(u'起動中')
        self.m_staticText2.SetFont(wx.Font(18, 70, 90, 92, False,
                                            wx.EmptyString))
        self.m_staticText2.SetForegroundColour(wx.Colour(247, 32, 9))

    def show_minor_msg(self, text):
        """SUMMARY

        @Arguments:

        - `text`:

        @Return:
        """
        self.m_staticText2.SetLabel(text)
        self.m_staticText2.SetFont(wx.Font(18, 70, 90, 92, False,
                                            wx.EmptyString))
        self.m_staticText2.SetForegroundColour(wx.Colour(247, 32, 9))

    def _wol(self):
        """SUMMARY

        @Return:
        """
        wakeonlan(MAC)

def king_isactive():
    """SUMMARY

    @Return:
    """
    ret = pyping.ping(HOST, count=1)
    return (0 == ret.ret_code)
