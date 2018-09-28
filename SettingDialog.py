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
## Class M_SettingDialog
###########################################################################

class M_SettingDialog ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"設定", pos = wx.DefaultPosition, size = wx.Size( 528,500 ), style=wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION )
		
		self.SetSizeHints( wx.Size( 300,500 ), wx.DefaultSize )
		self.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1.SetMinSize( wx.Size( -1,400 ) ) 
		self.m_Settingnotebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,300 ), 0 )
		self.m_Settingnotebook.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		self.m_Settingnotebook.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		self.tab = wx.Panel( self.m_Settingnotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.tab.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		self.tab.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.tab.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self.tab, wx.ID_ANY, u"フレームレート：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		
		self.m_staticText3.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer7.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10 )
		
		self.lineEdit = wx.TextCtrl( self.tab, wx.ID_ANY, u"350", wx.DefaultPosition, wx.Size( 60,18 ), 0 )
		self.lineEdit.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer7.Add( self.lineEdit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer6.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.tab, wx.ID_ANY, u"白飛び／黒潰れ領域の閾値（輝度値）" ), wx.HORIZONTAL )
		
		
		sbSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"白飛び：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		
		self.m_staticText5.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		sbSizer2.Add( self.m_staticText5, 0, wx.ALL, 10 )
		
		self.m_spinBox_3 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"255", wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 255, 255 )
		self.m_spinBox_3.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		self.m_spinBox_3.SetMinSize( wx.Size( 70,-1 ) )
		
		sbSizer2.Add( self.m_spinBox_3, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"以上　", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		
		self.m_staticText6.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		sbSizer2.Add( self.m_staticText6, 0, wx.ALL, 10 )
		
		self.m_staticText7 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"黒潰れ：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		
		self.m_staticText7.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		sbSizer2.Add( self.m_staticText7, 0, wx.ALL, 10 )
		
		self.m_spinBox_4 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 255, 0 )
		self.m_spinBox_4.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		self.m_spinBox_4.SetMinSize( wx.Size( 50,-1 ) )
		
		sbSizer2.Add( self.m_spinBox_4, 0, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"以下　", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		
		self.m_staticText61.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		sbSizer2.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.tab.SetSizer( bSizer6 )
		self.tab.Layout()
		bSizer6.Fit( self.tab )
		self.m_Settingnotebook.AddPage( self.tab, u"　基本設定　", False )
		self.m_tab2 = wx.Panel( self.m_Settingnotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_tab2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_tab2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_tab2, wx.ID_ANY, u"変位の算出方法" ), wx.VERTICAL )
		
		self.m_radioButton = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"絶対変位（基準フレームに対する変位を算出）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioButton.SetValue( True ) 
		self.m_radioButton.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		sbSizer3.Add( self.m_radioButton, 0, wx.ALL, 5 )
		
		self.m_radioButton2 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"相対変位（前フレームに対する変位を算出）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioButton2.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		sbSizer3.Add( self.m_radioButton2, 0, wx.ALL, 5 )
		
		
		bSizer12.Add( sbSizer3, 0, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1111 = wx.StaticText( self.m_tab2, wx.ID_ANY, u"最大数：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1111.Wrap( -1 )
		
		self.m_staticText1111.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer91.Add( self.m_staticText1111, 0, wx.ALL, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( self.m_tab2, wx.ID_ANY, u"10", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_textCtrl21.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer91.Add( self.m_textCtrl21, 0, wx.ALL, 5 )
		
		
		bSizer12.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.m_tab2.SetSizer( bSizer12 )
		self.m_tab2.Layout()
		bSizer12.Fit( self.m_tab2 )
		self.m_Settingnotebook.AddPage( self.m_tab2, u"　変位分析　", True )
		self.m_tab3 = wx.Panel( self.m_Settingnotebook, wx.ID_ANY, wx.DefaultPosition, wx.Size( 70,-1 ), wx.TAB_TRAVERSAL )
		self.m_tab3.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		self.m_tab3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_tab3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer70 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self.m_tab3, wx.ID_ANY, u"振動モード次数：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		
		self.m_staticText11.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer70.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_spinBox_5 = wx.SpinCtrl( self.m_tab3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 1, 100, 1 )
		bSizer70.Add( self.m_spinBox_5, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.m_tab3, wx.ID_ANY, u"(1-100)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		
		self.m_staticText10.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer70.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer70.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer70.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer18.Add( bSizer70, 0, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText111 = wx.StaticText( self.m_tab3, wx.ID_ANY, u"実寸値　　　　：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )
		
		self.m_staticText111.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer9.Add( self.m_staticText111, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_tab3, wx.ID_ANY, u"9000", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_textCtrl2.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer9.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_staticText101 = wx.StaticText( self.m_tab3, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )
		
		self.m_staticText101.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer9.Add( self.m_staticText101, 0, wx.ALL, 5 )
		
		
		bSizer18.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.m_tab3.SetSizer( bSizer18 )
		self.m_tab3.Layout()
		self.m_Settingnotebook.AddPage( self.m_tab3, u"振動モード", False )
		
		bSizer1.Add( self.m_Settingnotebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer19.SetMinSize( wx.Size( -1,50 ) ) 
		
		bSizer19.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( 60,30 ), 0 )
		self.m_button1.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer19.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.Size( 60,30 ), 0 )
		self.m_button2.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "メイリオ" ) )
		
		bSizer19.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer19, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

