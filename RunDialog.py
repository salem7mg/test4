# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class M_RunDialog
###########################################################################

class M_RunDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"分析処理実行中", pos = wx.DefaultPosition, size = wx.Size( 243,100 ), style = wx.CAPTION )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "メイリオ" ) )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.Point( 1200,-1 ), wx.Size( 400,50 ), wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 ) 
		self.m_gauge1.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "ＭＳ Ｐゴシック" ) )
		
		bSizer14.Add( self.m_gauge1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

