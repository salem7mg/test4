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
## Class m_setObsPoint_Dialog
###########################################################################

class m_setObsPoint_Dialog ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"観測点の指定", pos = wx.DefaultPosition, size = wx.Size( 413,447 ),style=wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION , name = u"観測点の指定" )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"パラメータ" ), wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"　  ブロック幅　：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		
		self.m_staticText2.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 10 )
		
		self.m_spinCtrl1 = wx.SpinCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 99, 32 )
		bSizer2.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"探査範囲　：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		
		self.m_staticText21.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer2.Add( self.m_staticText21, 0, wx.ALL, 10 )
		
		self.m_spinCtrl3 = wx.SpinCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 99, 5 )
		self.m_spinCtrl3.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer2.Add( self.m_spinCtrl3, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText22 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"  　ブロック高さ：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		
		self.m_staticText22.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer3.Add( self.m_staticText22, 0, wx.ALL, 10 )
		
		self.m_spinCtrl2 = wx.SpinCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 99, 32 )
		bSizer3.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )
		
		self.m_staticText211 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"拡大倍率　：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		
		bSizer3.Add( self.m_staticText211, 0, wx.ALL, 10 )
		
		self.m_spinCtrl4 = wx.SpinCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 99, 2 )
		bSizer3.Add( self.m_spinCtrl4, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		bSizer33.Add( sbSizer3, 0, wx.EXPAND, 0 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"点の指定方法" ), wx.VERTICAL )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer22.SetMinSize( wx.Size( 100,-1 ) ) 
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer23.SetMinSize( wx.Size( 50,-1 ) ) 
		m_comboBox2Choices = [ u"点", u"線", u"矩形", u"マスクファイル", u"過去の観測点ファイル" ]
		self.m_comboBox2 = wx.ComboBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"点", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.m_comboBox2.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "ＭＳ Ｐゴシック" ) )
		self.m_comboBox2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_comboBox2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer23.Add( self.m_comboBox2, 0, wx.ALL, 5 )
		
		self.m_staticText2212 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"               分割数：        ", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2212.Wrap( -1 )
		
		self.m_staticText2212.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer23.Add( self.m_staticText2212, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_spinCtrl51 = wx.SpinCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 99, 32 )
		bSizer23.Add( self.m_spinCtrl51, 0, wx.ALL, 5 )
		
		
		bSizer22.Add( bSizer23, 0, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText221 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"　 間隔(Ｘ方向)：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )
		
		self.m_staticText221.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer5.Add( self.m_staticText221, 0, wx.ALL, 10 )
		
		self.m_spinCtrl5 = wx.SpinCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 99, 32 )
		bSizer5.Add( self.m_spinCtrl5, 0, wx.ALL, 5 )
		
		self.m_staticText2211 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"間隔(Ｙ方向)：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2211.Wrap( -1 )
		
		self.m_staticText2211.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer5.Add( self.m_staticText2211, 0, wx.ALL, 10 )
		
		self.m_spinCtrl6 = wx.SpinCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 99, 32 )
		self.m_spinCtrl6.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer5.Add( self.m_spinCtrl6, 0, wx.ALL, 5 )
		
		
		bSizer22.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		self.m_staticText54 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"ファイルの指定：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		
		self.m_staticText54.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer22.Add( self.m_staticText54, 0, wx.ALL, 5 )
		
		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_lineEdit = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.m_lineEdit.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer9.Add( self.m_lineEdit, 0, wx.ALL, 5 )
		
		self.m_toolButton = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"参照...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toolButton.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer9.Add( self.m_toolButton, 0, wx.ALL, 5 )
		
		
		bSizer51.Add( bSizer9, 0, wx.EXPAND, 5 )
		
		
		bSizer22.Add( bSizer51, 0, wx.EXPAND, 5 )
		
		
		sbSizer4.Add( bSizer22, 0, wx.EXPAND, 5 )
		
		
		bSizer33.Add( sbSizer4, 0, wx.EXPAND, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"観測点グループを指定" ), wx.VERTICAL )
		
		bSizer511 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText12 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"現在のグループ番号：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		
		bSizer13.Add( self.m_staticText12, 0, wx.ALIGN_RIGHT, 5 )
		
		
		bSizer511.Add( bSizer13, 0, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer91.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"前グループ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer91.Add( self.m_button1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer91.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"次グループ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer91.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		bSizer91.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_textCtrl11.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer91.Add( self.m_textCtrl11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer91.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		
		bSizer511.Add( bSizer91, 0, wx.EXPAND, 5 )
		
		
		sbSizer5.Add( bSizer511, 1, wx.EXPAND, 5 )
		
		
		bSizer33.Add( sbSizer5, 0, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		m_sdbSizer = wx.StdDialogButtonSizer()
		self.m_sdbSizerOK = wx.Button( self, wx.ID_OK )
		m_sdbSizer.AddButton( self.m_sdbSizerOK )
		self.m_sdbSizerCancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer.AddButton( self.m_sdbSizerCancel )
		m_sdbSizer.Realize();
		
		bSizer16.Add( m_sdbSizer, 1, wx.EXPAND, 5 )
		
		
		bSizer33.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer33 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

