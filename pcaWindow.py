# -*- coding: utf-8 -*- 

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WXAgg')

import wx
import wx.xrc

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wx import NavigationToolbar2Wx, wxc
from matplotlib.figure import Figure
import mainWindow
import numpy as np
import cv2

###########################################################################
## Class PCAWindow 
###########################################################################

class PCAWindow ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"振動モード分析", pos = wx.DefaultPosition, size = wx.Size( 1280, 980 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )		
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        self.contribution_figure = Figure(figsize=(8, 4.3), dpi=100)
        self.contribution_canvas = FigureCanvasWxAgg(self, -1, self.contribution_figure)
        self.contribution_navigationToolbar = NavigationToolbar2Wx(self.contribution_canvas)
        self.contribution_navigationToolbar.Realize()
        self.contribution_navigationToolbar.update()	

        self.dammy1_figure = Figure(figsize=(8, 4.3), dpi=100)
        self.dammy1_canvas = FigureCanvasWxAgg(self, -1, self.dammy1_figure)
        self.dammy1_navigationToolbar = NavigationToolbar2Wx(self.dammy1_canvas)
        self.dammy1_navigationToolbar.Realize()
        self.dammy1_navigationToolbar.update()	

        import configdata
        self.n_comp = 5   #仮設定(固有値の計算範囲）
        self.p_comp = 1   #仮設定（表示する固有値モード）
        self.scale = 1  #仮設定(表示倍率）
        self.data = configdata.dis.sel(layer=0,features=["dis_x", "dis_y"], stats="mu").values
        self.pxpy = configdata.pxpys.sel(layer=0, features=["x", "y"]).values
        self.x = range(1,self.n_comp+1)
        from eof_analysis import eof
        self.d, self.v = eof(self.data, self.n_comp)
        point = int(self.v.shape[0]/2)
        datavx = self.v[:point,self.p_comp-1]
        datavy = self.v[point:,self.p_comp-1]

        self.contribution_figure.subplots_adjust(left=0.3, right=0.7, bottom=0.1, top=0.8)
        #self.contribution_axes = self.contribution_figure.add_subplot(111, facecolor='black')
        self.contribution_axes = self.contribution_figure.add_subplot(111, facecolor='white')
        self.contribution_axes.minorticks_on()
        self.contribution_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8, bottom='on', left='on')
        self.contribution_axes.grid(True)
        self.contribution_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.contribution_axes.set_title('contribution ratio')
        #self.colorlist = ["r", "g", "b", "c", "m", "y", "k", "w"]
        self.colorlist = ["r", "g", "b", "c", "m", "y", "k"]
        self.contribution_axes.bar(self.x, self.d,color=self.colorlist)

        frame = 0
        cv2img = cv2.imread(configdata.image_filelist[frame])
        self.im = cv2.cvtColor(cv2img, cv2.COLOR_BGR2RGB)
        self.dammy1_figure.subplots_adjust(left=0.1, right=0.995, bottom=0.1, top=0.9)
        #self.dammy1_axes = self.dammy1_figure.add_subplot(111, facecolor='black')
        self.dammy1_axes = self.dammy1_figure.add_subplot(111, facecolor='white')
        self.dammy1_axes.minorticks_on()
        self.dammy1_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8, bottom='on', left='on')
        self.dammy1_axes.grid(True)
        self.dammy1_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.dammy1_axes.set_title('dammy1')
        m = mainWindow.setSt_Dialog2(self)
        param = int(m.getParam2())
        xl = []
        st = int(param / 10)
        for i in range(0 ,param,st):
            xl.append(i)

        self.dammy1_axes.set_xticklabels(xl)
        self.dammy1_axes.imshow(self.im)
        self.dammy1_axes.quiver(self.pxpy[:, 0], self.pxpy[:, 1], datavx, datavy,angles='xy', width=0.005, color='red', scale=self.scale)


        gSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer32 = wx.BoxSizer( wx.VERTICAL ) # 左上       
        bSizer32.Add(self.contribution_canvas, 0, wx.EXPAND)
        bSizer32.Add(self.contribution_navigationToolbar, 0, wx.EXPAND)
        gSizer1.Add( bSizer32, 0, wx.EXPAND)

        bSizer35 = wx.BoxSizer( wx.HORIZONTAL)
        bSizer34 = wx.BoxSizer( wx.VERTICAL ) # 下
        bSizer35.Add(bSizer34, 0, wx.EXPAND)
        bSizer34.Add(self.dammy1_canvas, 0, wx.EXPAND)
        bSizer34.Add(self.dammy1_navigationToolbar, 0, wx.EXPAND)
        bSizer36 = wx.BoxSizer( wx.VERTICAL)
        bSizer35.Add(bSizer36, 0, wx.EXPAND)
       	staticText0 = wx.StaticText(self, wx.ID_ANY, u"  \n  \n  \n   \n    \n", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE)
        bSizer36.Add(staticText0, 0, wx.ALIGN_LEFT)
        array = []
        for i in range(self.n_comp):
            array.append( str(i+1))
        self.combo = wx.ComboBox(self, -1, u'  ', choices=array)
        self.combo.SetSelection(0)
        self.combo.Bind(wx.EVT_COMBOBOX,self.event_combo)
        self.textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer37 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer36.Add(bSizer37, 0, wx.ALIGN_LEFT)
       	staticText1 = wx.StaticText(self, wx.ID_ANY, u"次数：", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE)
        staticText1.SetForegroundColour('#000000')
        bSizer37.Add(staticText1, 0, wx.ALIGN_CENTER)
        bSizer37.Add(self.combo, 0, wx.ALIGN_CENTER)
        bSizer38 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer36.Add(bSizer38, 0, wx.ALIGN_LEFT)
       	staticText2 = wx.StaticText(self, wx.ID_ANY, u"スケール：", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE)
        staticText2.SetForegroundColour('#000000') 
        self.button1 = wx.Button( self, wx.ID_ANY, u"更新", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.button1.Bind(wx.EVT_BUTTON,self.event_scale)
        bSizer38.Add(staticText2, 0, wx.ALIGN_CENTER)
        bSizer38.Add(self.textCtrl1, 0, wx.ALIGN_CENTER)
        bSizer38.Add(self.button1, 0, wx.ALIGN_CENTER)
        gSizer1.Add(bSizer35, 0, wx.EXPAND)
        self.SetSizer( gSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )

    def updateGraph(self):
        point = int(self.v.shape[0]/2)
        datavx = self.v[:point,self.p_comp]
        datavy = self.v[point:,self.p_comp]
        self.dammy1_axes.cla()
        #self.dammy1_axes = self.dammy1_figure.add_subplot(111, facecolor='black')
        self.dammy1_axes = self.dammy1_figure.add_subplot(111, facecolor='white')
        self.dammy1_axes.minorticks_on()
        self.dammy1_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8, bottom='on', left='on')
        self.dammy1_axes.grid(True)
        self.dammy1_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.dammy1_axes.set_title('dammy1')
        m = mainWindow.setSt_Dialog2(self)
        param = int(m.getParam2())
        xl = []
        st = int(param / 10)
        for i in range(0 ,param,st):
            xl.append(i)

        self.dammy1_axes.set_xticklabels(xl)
        self.dammy1_axes.imshow(self.im)
        self.dammy1_axes.quiver(self.pxpy[:, 0], self.pxpy[:, 1], datavx, datavy,angles='xy', width=0.005, color=self.colorlist[self.p_comp], scale=self.scale)
        self.dammy1_canvas.draw()

    def event_combo(self, event):
        self.p_comp =  int(self.combo.GetSelection())
        self.updateGraph()
    
    def event_scale(self, event):
        self.scale = float(self.textCtrl1.GetValue())
        self.updateGraph()

    def __del__( self ):
        pass
