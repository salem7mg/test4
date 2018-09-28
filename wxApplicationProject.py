# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 22 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class wxApplicationFrame
###########################################################################

class wxApplicationFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"橋梁観測アプリ", pos = wx.DefaultPosition, size = wx.Size( 1600,900 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar = wx.MenuBar( 0 )
		self.m_fileMenu = wx.Menu()
		self.m_fileMenuItem1 = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"開く", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.Append( self.m_fileMenuItem1 )

		self.m_fileMenuItem2 = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"最近使用したプロジェクト", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.Append( self.m_fileMenuItem2 )

		self.m_fileMenuItem3 = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"閉じる", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.Append( self.m_fileMenuItem3 )

		self.m_fileMenu.AppendSeparator()

		self.m_fileMenuItem4 = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"保存", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.Append( self.m_fileMenuItem4 )

		self.m_fileMenuItem5 = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"名前を付けて保存", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.Append( self.m_fileMenuItem5 )

		self.m_fileMenu.AppendSeparator()

		self.m_fileMenuItem6 = wx.Menu()
		self.m_fileMenuItem61 = wx.MenuItem( self.m_fileMenuItem6, wx.ID_ANY, u"静止画（*.bmp,*png,*.pgm）", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenuItem6.Append( self.m_fileMenuItem61 )

		self.m_fileMenuItem62 = wx.MenuItem( self.m_fileMenuItem6, wx.ID_ANY, u"動画（*.mp4）", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenuItem6.Append( self.m_fileMenuItem62 )

		self.m_fileMenu.AppendSubMenu( self.m_fileMenuItem6, u"インポート" )

		self.m_fileMenuItem7 = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"エクスポート", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.Append( self.m_fileMenuItem7 )

		self.m_fileMenu.AppendSeparator()

		self.m_fileMenuItem8 = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"終了", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.Append( self.m_fileMenuItem8 )

		self.m_menubar.Append( self.m_fileMenu, u"ファイル" )

		self.m_editMenu = wx.Menu()
		self.m_editMenuItem1 = wx.MenuItem( self.m_editMenu, wx.ID_ANY, u"元に戻す", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_editMenu.Append( self.m_editMenuItem1 )

		self.m_editMenu.AppendSeparator()

		self.m_editMenuItem2 = wx.MenuItem( self.m_editMenu, wx.ID_ANY, u"ノイズ除去", wx.EmptyString, wx.ITEM_CHECK )
		self.m_editMenu.Append( self.m_editMenuItem2 )

		self.m_editMenuItem3 = wx.MenuItem( self.m_editMenu, wx.ID_ANY, u"ドリフトカット（HPF）", wx.EmptyString, wx.ITEM_CHECK )
		self.m_editMenu.Append( self.m_editMenuItem3 )

		self.m_editMenuItem4 = wx.MenuItem( self.m_editMenu, wx.ID_ANY, u"メディアンフィルタ", wx.EmptyString, wx.ITEM_CHECK )
		self.m_editMenu.Append( self.m_editMenuItem4 )

		self.m_menubar.Append( self.m_editMenu, u"編集" )

		self.m_analyzeMenu = wx.Menu()
		self.m_analyzeMenuItem1 = wx.MenuItem( self.m_analyzeMenu, wx.ID_ANY, u"観測点を指定", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_analyzeMenu.Append( self.m_analyzeMenuItem1 )

		self.m_analyzeMenuItem2 = wx.MenuItem( self.m_analyzeMenu, wx.ID_ANY, u"白飛び/黒潰れ 領域表示", wx.EmptyString, wx.ITEM_CHECK )
		self.m_analyzeMenu.Append( self.m_analyzeMenuItem2 )

		self.m_analyzeMenuItem3 = wx.MenuItem( self.m_analyzeMenu, wx.ID_ANY, u"自動セグメンテーション", wx.EmptyString, wx.ITEM_CHECK )
		self.m_analyzeMenu.Append( self.m_analyzeMenuItem3 )

		self.m_analyzeMenu.AppendSeparator()

		self.m_analyzeMenuItem4 = wx.MenuItem( self.m_analyzeMenu, wx.ID_ANY, u"分析開始", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_analyzeMenu.Append( self.m_analyzeMenuItem4 )

		self.m_analyzeMenuItem5 = wx.MenuItem( self.m_analyzeMenu, wx.ID_ANY, u"変位分析のみ開始", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_analyzeMenu.Append( self.m_analyzeMenuItem5 )

		self.m_analyzeMenuItem6 = wx.MenuItem( self.m_analyzeMenu, wx.ID_ANY, u"振動モード分析のみ開始", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_analyzeMenu.Append( self.m_analyzeMenuItem6 )

		self.m_analyzeMenuItem7 = wx.MenuItem( self.m_analyzeMenu, wx.ID_ANY, u"空間差分分析のみ開始", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_analyzeMenu.Append( self.m_analyzeMenuItem7 )

		self.m_analyzeMenuItem8 = wx.MenuItem( self.m_analyzeMenu, wx.ID_ANY, u"減衰分析のみ実施", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_analyzeMenu.Append( self.m_analyzeMenuItem8 )

		self.m_menubar.Append( self.m_analyzeMenu, u"分析" )

		self.m_displayMenu = wx.Menu()
		self.m_displayMenuItem1 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"変位ベクトル", wx.EmptyString, wx.ITEM_CHECK )
		self.m_displayMenu.Append( self.m_displayMenuItem1 )

		self.m_displayMenuItem2 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"変位ベクトル（X)", wx.EmptyString, wx.ITEM_CHECK )
		self.m_displayMenu.Append( self.m_displayMenuItem2 )

		self.m_displayMenuItem3 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"変位ベクトル（Y)", wx.EmptyString, wx.ITEM_CHECK )
		self.m_displayMenu.Append( self.m_displayMenuItem3 )

		self.m_displayMenuItem4 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"変位たわみ表示", wx.EmptyString, wx.ITEM_CHECK )
		self.m_displayMenu.Append( self.m_displayMenuItem4 )

		self.m_displayMenuItem5 = wx.Menu()
		self.m_displayMenuItem51 = wx.MenuItem( self.m_displayMenuItem5, wx.ID_ANY, u"相対変位（前フレームに対する変位を表示）", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_displayMenuItem5.Append( self.m_displayMenuItem51 )

		self.m_displayMenuItem52 = wx.MenuItem( self.m_displayMenuItem5, wx.ID_ANY, u"絶対変位（基準フレームに対する変位を表示）", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_displayMenuItem5.Append( self.m_displayMenuItem52 )

		self.m_displayMenu.AppendSubMenu( self.m_displayMenuItem5, u"変位表示オプション" )

		self.m_displayMenu.AppendSeparator()

		self.m_displayMenuItem6 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"振動モードベクトル", wx.EmptyString, wx.ITEM_CHECK )
		self.m_displayMenu.Append( self.m_displayMenuItem6 )

		self.m_displayMenuItem7 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"振動たわみ表示", wx.EmptyString, wx.ITEM_CHECK )
		self.m_displayMenu.Append( self.m_displayMenuItem7 )

		self.m_displayMenu.AppendSeparator()

		self.m_displayMenuItem8 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"応力分布（ヒートマップ）", wx.EmptyString, wx.ITEM_CHECK )
		self.m_displayMenu.Append( self.m_displayMenuItem8 )

		self.m_displayMenu.AppendSeparator()

		self.m_displayMenuItem9 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"観測点表示", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_displayMenu.Append( self.m_displayMenuItem9 )

		self.m_displayMenuItem10 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"観測点の矩形表示", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_displayMenu.Append( self.m_displayMenuItem10 )

		self.m_displayMenuItem11 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"基準点表示", wx.EmptyString, wx.ITEM_CHECK )
		self.m_displayMenu.Append( self.m_displayMenuItem11 )

		self.m_displayMenuItem12 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"基準点の矩形表示", wx.EmptyString, wx.ITEM_CHECK )
		self.m_displayMenu.Append( self.m_displayMenuItem12 )

		self.m_displayMenu.AppendSeparator()

		self.m_displayMenuItem13 = wx.MenuItem( self.m_displayMenu, wx.ID_ANY, u"カラーバー表示", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_displayMenu.Append( self.m_displayMenuItem13 )

		self.m_menubar.Append( self.m_displayMenu, u"表示" )

		self.m_cameraCalibMenu = wx.Menu()
		self.m_cameraCalibMenuItem1 = wx.MenuItem( self.m_cameraCalibMenu, wx.ID_ANY, u"レンズ歪み補正", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_cameraCalibMenu.Append( self.m_cameraCalibMenuItem1 )

		self.m_menubar.Append( self.m_cameraCalibMenu, u"カメラ調整" )

		self.m_optionMenu = wx.Menu()
		self.m_optionMenuItem1 = wx.MenuItem( self.m_optionMenu, wx.ID_ANY, u"環境設定", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_optionMenu.Append( self.m_optionMenuItem1 )

		self.m_menubar.Append( self.m_optionMenu, u"オプション" )

		self.m_helpMenu = wx.Menu()
		self.m_helpMenuItem1 = wx.MenuItem( self.m_helpMenu, wx.ID_ANY, u"橋梁観測アプリについて", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_helpMenu.Append( self.m_helpMenuItem1 )

		self.m_helpMenuItem2 = wx.MenuItem( self.m_helpMenu, wx.ID_ANY, u"ヘルプ", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_helpMenu.Append( self.m_helpMenuItem2 )

		self.m_helpMenuItem3 = wx.MenuItem( self.m_helpMenu, wx.ID_ANY, u"使用規約", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_helpMenu.Append( self.m_helpMenuItem3 )

		self.m_menubar.Append( self.m_helpMenu, u"ヘルプ" )

		self.SetMenuBar( self.m_menubar )

		self.m_wxApplicationToolbar = self.CreateToolBar( wx.TB_HORIZONTAL|wx.TB_TEXT, wx.ID_ANY )
		self.m_wxApplicationToolbar.SetToolSeparation( 8 )
		self.m_wxApplicationToolbar.SetMargins( wx.Size( 1,1 ) )
		self.m_wxApplicationToolbar.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_wxApplicationToolbar.Realize()


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


