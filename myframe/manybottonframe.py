# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

import gettext
_ = gettext.gettext

###########################################################################
## Class ManyBottonFrame
###########################################################################

class ManyBottonFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _("サーバー管理"), pos = wx.DefaultPosition, size = wx.Size( 523,349 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_panel, wx.ID_ANY, _("KI Server"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 30, 70, 90, 92, False, wx.EmptyString ) )

		bSizer3.Add( self.m_staticText1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )

		bSizer2.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button = wx.Button( self.m_panel, wx.ID_ANY, _("起動(&W)"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button.SetMinSize( wx.Size( -1,70 ) )

		bSizer4.Add( self.m_button, 1, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panel, wx.ID_ANY, _("サーバー電源OFF"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetMinSize( wx.Size( -1,70 ) )

		bSizer4.Add( self.m_button2, 1, wx.ALL, 5 )

		bSizer2.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button3 = wx.Button( self.m_panel, wx.ID_ANY, _("未実装1"), wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		bSizer5.Add( self.m_button3, 1, wx.ALL, 5 )

		self.m_button4 = wx.Button( self.m_panel, wx.ID_ANY, _("未実装2"), wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		bSizer5.Add( self.m_button4, 1, wx.ALL, 5 )

		bSizer2.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button5 = wx.Button( self.m_panel, wx.ID_ANY, _("Help"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetMinSize( wx.Size( -1,70 ) )

		bSizer7.Add( self.m_button5, 1, wx.ALL, 5 )

		self.m_button6 = wx.Button( self.m_panel, wx.ID_ANY, _("About"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetMinSize( wx.Size( -1,70 ) )

		bSizer7.Add( self.m_button6, 1, wx.ALL, 5 )

		bSizer6.Add( bSizer7, 1, 0, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_button7 = wx.Button( self.m_panel, wx.ID_ANY, _("閉じる(&X)"), wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.m_button7.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )

		bSizer8.Add( self.m_button7, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer6.Add( bSizer8, 1, 0, 5 )

		bSizer2.Add( bSizer6, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_panel.SetSizer( bSizer2 )
		self.m_panel.Layout()
		bSizer2.Fit( self.m_panel )
		bSizer1.Add( self.m_panel, 1, wx.EXPAND, 5 )

		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass
