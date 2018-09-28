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

###########################################################################
## Class DampedAnalysisWindow 
###########################################################################

class DampedAnalysisWindow ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"空間差分", pos = wx.DefaultPosition, size = wx.Size( 1280, 980 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        self.contribution_figure = Figure(figsize=(8, 4.3), dpi=100)
        self.contribution_canvas = FigureCanvasWxAgg(self, -1, self.contribution_figure)
        self.contribution_navigationToolbar = NavigationToolbar2Wx(self.contribution_canvas)
        self.contribution_navigationToolbar.Realize()
        self.contribution_navigationToolbar.update()	

        self.eigen_figure = Figure(figsize=(8, 4.3), dpi=100)
        self.eigen_canvas = FigureCanvasWxAgg(self, -1, self.eigen_figure)
        self.eigen_navigationToolbar = NavigationToolbar2Wx(self.eigen_canvas)
        self.eigen_navigationToolbar.Realize()
        self.eigen_navigationToolbar.update()	

        self.dammy1_figure = Figure(figsize=(8, 4.3), dpi=100)
        self.dammy1_canvas = FigureCanvasWxAgg(self, -1, self.dammy1_figure)
        self.dammy1_navigationToolbar = NavigationToolbar2Wx(self.dammy1_canvas)
        self.dammy1_navigationToolbar.Realize()
        self.dammy1_navigationToolbar.update()	

        self.dammy2_figure = Figure(figsize=(8, 4.3), dpi=100)
        self.dammy2_canvas = FigureCanvasWxAgg(self, -1, self.dammy2_figure)
        self.dammy2_navigationToolbar = NavigationToolbar2Wx(self.dammy2_canvas)
        self.dammy2_navigationToolbar.Realize()
        self.dammy2_navigationToolbar.update()	

        self.contribution_figure.subplots_adjust(left=0.005, right=0.995, bottom=0.1, top=0.9)
        #self.contribution_axes = self.contribution_figure.add_subplot(111, facecolor='black')
        self.contribution_axes = self.contribution_figure.add_subplot(111, facecolor='white')
        self.contribution_axes.minorticks_on()
        self.contribution_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8, bottom='on', left='on')
        self.contribution_axes.grid(True)
        self.contribution_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.contribution_axes.set_title('contribution ratio')
        self.contribution_axes.plot(np.random.randn(100, 100))

        self.eigen_figure.subplots_adjust(left=0.005, right=0.995, bottom=0.1, top=0.9)
        #self.eigen_axes = self.eigen_figure.add_subplot(111, facecolor='black')
        self.eigen_axes = self.eigen_figure.add_subplot(111, facecolor='white')
        self.eigen_axes.minorticks_on()
        self.eigen_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8, bottom='on', left='on')
        self.eigen_axes.grid(True)
        self.eigen_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.eigen_axes.set_title('eigen value')
        self.eigen_axes.plot(np.random.randn(100, 100))

        self.dammy1_figure.subplots_adjust(left=0.005, right=0.995, bottom=0.1, top=0.9)
        #self.dammy1_axes = self.dammy1_figure.add_subplot(111, facecolor='black')
        self.dammy1_axes = self.dammy1_figure.add_subplot(111, facecolor='white')
        self.dammy1_axes.minorticks_on()
        self.dammy1_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8, bottom='on', left='on')
        self.dammy1_axes.grid(True)
        self.dammy1_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.dammy1_axes.set_title('dammy1')
        self.dammy1_axes.plot(np.random.randn(100, 100))

        self.dammy2_figure.subplots_adjust(left=0.005, right=0.995, bottom=0.1, top=0.9)
        #self.dammy2_axes = self.dammy2_figure.add_subplot(111, facecolor='black')
        self.dammy2_axes = self.dammy2_figure.add_subplot(111, facecolor='white')
        self.dammy2_axes.minorticks_on()
        self.dammy2_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8, bottom='on', left='on')
        self.dammy2_axes.grid(True)
        self.dammy2_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.dammy2_axes.set_title('dammy2')
        self.dammy2_axes.plot(np.random.randn(100, 100))

        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

        bSizer32 = wx.BoxSizer( wx.VERTICAL ) # 左上       
        bSizer32.Add(self.contribution_canvas, 0, wx.EXPAND)   
        bSizer32.Add(self.contribution_navigationToolbar, 0, wx.EXPAND)
        gSizer1.Add( bSizer32, 0, wx.EXPAND)		

        bSizer34 = wx.BoxSizer( wx.VERTICAL ) # 右上
        bSizer34.Add(self.dammy1_canvas, 0, wx.EXPAND)
        bSizer34.Add(self.dammy1_navigationToolbar, 0, wx.EXPAND)				
        gSizer1.Add( bSizer34, 0, wx.EXPAND, 0 )

        bSizer33 = wx.BoxSizer( wx.VERTICAL ) # 左下
        bSizer33.Add(self.eigen_canvas, 0, wx.EXPAND)
        bSizer33.Add(self.eigen_navigationToolbar, 0, wx.EXPAND)				
        gSizer1.Add( bSizer33, 0, wx.EXPAND, 0 )

        bSizer35 = wx.BoxSizer( wx.VERTICAL ) # 右下
        bSizer35.Add(self.dammy2_canvas, 0, wx.EXPAND)
        bSizer35.Add(self.dammy2_navigationToolbar, 0, wx.EXPAND)							
        gSizer1.Add( bSizer35, 0, wx.EXPAND, 0 )

        self.SetSizer( gSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass
