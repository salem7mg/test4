# -*- coding: utf-8 -*- 

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WXAgg')

import wx
import wx.xrc

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wx import NavigationToolbar2Wx, wxc
from matplotlib.figure import Figure
import numpy as np
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname='font_1_kokumr_1.00_rls.ttf', size=14)

###########################################################################
## Class DisplacementWindow 
###########################################################################

class DisplacementWindow ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"変位分析", pos = wx.DefaultPosition, size = wx.Size( 1280, 980 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )		
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        self.dispX_figure = Figure(figsize=(8, 4.3), dpi=100)
        self.dispX_canvas = FigureCanvasWxAgg(self, -1, self.dispX_figure)
        self.dispX_navigationToolbar = NavigationToolbar2Wx(self.dispX_canvas)
        self.dispX_navigationToolbar.Realize()
        self.dispX_navigationToolbar.update()	

        self.dispY_figure = Figure(figsize=(8, 4.3), dpi=100)
        self.dispY_canvas = FigureCanvasWxAgg(self, -1, self.dispY_figure)
        self.dispY_navigationToolbar = NavigationToolbar2Wx(self.dispY_canvas)
        self.dispY_navigationToolbar.Realize()
        self.dispY_navigationToolbar.update()	

        self.fftX_figure = Figure(figsize=(8, 4.3), dpi=100)
        self.fftX_canvas = FigureCanvasWxAgg(self, -1, self.fftX_figure)
        self.fftX_navigationToolbar = NavigationToolbar2Wx(self.fftX_canvas)
        self.fftX_navigationToolbar.Realize()
        self.fftX_navigationToolbar.update()	

        self.fftY_figure = Figure(figsize=(8, 4.3), dpi=100)
        self.fftY_canvas = FigureCanvasWxAgg(self, -1, self.fftY_figure)
        self.fftY_navigationToolbar = NavigationToolbar2Wx(self.fftY_canvas)
        self.fftY_navigationToolbar.Realize()
        self.fftY_navigationToolbar.update()	
        
        """
        colorlist = ["r", "g", "b", "c", "m", "y", "k", "w", "r", "g", "b", "c", "m", "y", "k", "w", "r", "g", "b", "c",
                     "m", "y", "k", "w", "r", "g", "b", "c", "m", "y", "k", "w", "r", "g", "b", "c", "m", "y", "k", "w",
                     "r", "g", "b", "c", "m", "y", "k", "w", "r", "g", "b", "c", "m", "y", "k", "w"]
        """
        colorlist = ["r", "g", "b", "c", "m", "y", "k"]


        import configdata
        self.mpoint = configdata.dis.shape[1]
        self.center = int(self.mpoint / 2)
        self.dis_x = configdata.dis.sel(layer=0, features="dis_x", stats="mu").values
        self.dis_y = configdata.dis.sel(layer=0, features="dis_y", stats="mu").values


        self.dispX_figure.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.9)
        #self.dispX_axes = self.dispX_figure.add_subplot(111, facecolor='black')
        self.dispX_axes = self.dispX_figure.add_subplot(111, facecolor='white')
        self.dispX_axes.minorticks_on()
        self.dispX_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8, bottom='on', left='on')
        self.dispX_axes.grid(True)
        self.dispX_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.dispX_axes.set_title('Displacement - X')
#        self.dispX_axes.plot(self.dis_x[:, self.center])
        self.dispX_axes.set_title(u'変位 - X', fontproperties=fp)
        for i in parent.selectPoint :
            #self.dispX_axes.plot(self.dis_x[:, i],color=colorlist[i], alpha=0.7)
            self.dispX_axes.plot(self.dis_x[:, i],color=colorlist[i % 7], alpha=0.7)
        self.dispY_figure.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.9)
        #self.dispY_axes = self.dispY_figure.add_subplot(111, facecolor='black')
        self.dispY_axes = self.dispY_figure.add_subplot(111, facecolor='white')
        self.dispY_axes.minorticks_on()
        self.dispY_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8, bottom='on', left='on')
        self.dispY_axes.grid(True)
        self.dispY_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.dispY_axes.set_title(u'変位  - Y', fontproperties=fp)
#        self.dispY_axes.plot(self.dis_y[:, self.center])
        for i in parent.selectPoint :
            #self.dispY_axes.plot(self.dis_y[:, i],color=colorlist[i], alpha=0.7)
            self.dispY_axes.plot(self.dis_y[:, i],color=colorlist[i % 7], alpha=0.7)

        from fft_analysis import fft
        self.flamefps = 350  #仮設定
        freq = float(self.flamefps)
        #amp_x, freq_list = fft(self.dis_x[:, self.center], freq)
        #amp_y, freq_list = fft(self.dis_y[:, self.center], freq)

        self.fftX_figure.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.9)
        #self.fftX_axes = self.fftX_figure.add_subplot(111, facecolor='black')
        self.fftX_axes = self.fftX_figure.add_subplot(111, facecolor='white')
        self.fftX_axes.minorticks_on()
        self.fftX_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8, bottom='on', left='on')
        self.fftX_axes.grid(True)
        self.fftX_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.fftX_axes.set_title('FFT - X')
        for i in parent.selectPoint :
            amp_x, freq_list = fft(self.dis_x[:, i], freq)
            #self.fftX_axes.plot(freq_list, amp_x, color=colorlist[i], alpha=0.7)
            self.fftX_axes.plot(freq_list, amp_x, color=colorlist[i % 7], alpha=0.7)
        self.fftY_figure.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.9)
        #self.fftY_axes = self.fftY_figure.add_subplot(111, facecolor='black')
        self.fftY_axes = self.fftY_figure.add_subplot(111, facecolor='white')
        self.fftY_axes.minorticks_on()
        self.fftY_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8, bottom='on', left='on')
        self.fftY_axes.grid(True)
        self.fftY_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        #self.fftY_axes.set_title('FFT - Y')
        #self.fftY_axes.plot(freq_list, amp_y)
        self.fftY_axes.set_title('FFT - Y')
        for i in parent.selectPoint :
            amp_y, freq_list = fft(self.dis_y[:, i], freq)
            #self.fftY_axes.plot(freq_list, amp_y, color=colorlist[i], alpha=0.7)
            self.fftY_axes.plot(freq_list, amp_y, color=colorlist[i % 7], alpha=0.7)
        gSizer1 = wx.GridSizer( 2, 2, 0, 0 )		

        bSizer32 = wx.BoxSizer( wx.VERTICAL ) # 左上       
        bSizer32.Add(self.dispX_canvas, 0, wx.EXPAND)   
        bSizer32.Add(self.dispX_navigationToolbar, 0, wx.EXPAND)
        gSizer1.Add( bSizer32, 0, wx.EXPAND)		

        bSizer34 = wx.BoxSizer( wx.VERTICAL ) # 右上
        bSizer34.Add(self.fftX_canvas, 0, wx.EXPAND)
        bSizer34.Add(self.fftX_navigationToolbar, 0, wx.EXPAND)				
        gSizer1.Add( bSizer34, 0, wx.EXPAND, 0 )

        bSizer33 = wx.BoxSizer( wx.VERTICAL ) # 左下
        bSizer33.Add(self.dispY_canvas, 0, wx.EXPAND)
        bSizer33.Add(self.dispY_navigationToolbar, 0, wx.EXPAND)				
        gSizer1.Add( bSizer33, 0, wx.EXPAND, 0 )

        bSizer35 = wx.BoxSizer( wx.VERTICAL ) # 右下
        bSizer35.Add(self.fftY_canvas, 0, wx.EXPAND)
        bSizer35.Add(self.fftY_navigationToolbar, 0, wx.EXPAND)							
        gSizer1.Add( bSizer35, 0, wx.EXPAND, 0 )

        self.SetSizer( gSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass
