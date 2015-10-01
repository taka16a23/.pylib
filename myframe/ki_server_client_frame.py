# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class KiServerClient
###########################################################################

class KiServerClient ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"サーバー操作", pos = wx.DefaultPosition, size = wx.Size( 400,260 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"   KI Server", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 25, 70, 90, 92, False, wx.EmptyString ) )

		bSizer6.Add( self.m_staticText1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer3.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.status_bitmap = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.status_bitmap, 0, wx.ALIGN_BOTTOM|wx.EXPAND|wx.ALL, 5 )

		bSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Message" ), wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"停止中", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 18, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 128, 128, 128 ) )

		sbSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer4.Add( sbSizer1, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.wol_button = wx.Button( self.m_panel1, wx.ID_ANY, u"起動(&W)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.wol_button.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.wol_button.SetToolTipString( u"wake on lan" )

		bSizer7.Add( self.wol_button, 1, wx.ALL|wx.EXPAND, 5 )

		self.halt_button = wx.Button( self.m_panel1, wx.ID_ANY, u"サーバー電源&OFF", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.halt_button.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.halt_button.SetToolTipString( u"halt" )

		bSizer7.Add( self.halt_button, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 0 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.close_button = wx.Button( self.m_panel1, wx.ID_ANY, u"閉じる(C)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.close_button.SetToolTipString( u"exit" )

		bSizer5.Add( self.close_button, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer2.Add( bSizer5, 0, wx.ALIGN_RIGHT, 0 )

		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )

		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.wol_button.Bind( wx.EVT_BUTTON, self.wol )
		self.halt_button.Bind( wx.EVT_BUTTON, self.halt )
		self.close_button.Bind( wx.EVT_BUTTON, self.exit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def wol( self, event ):
		event.Skip()

	def halt( self, event ):
		event.Skip()

	def exit( self, event ):
		event.Skip()
