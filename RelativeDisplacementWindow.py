# -*- coding: utf-8 -*- 

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WXAgg')

import wx
import wx.xrc

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wx import NavigationToolbar2Wx, wxc
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import cv2

###########################################################################
## Class RelativeDisplacementWindow
###########################################################################

class RelativeDisplacementWindow ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"相対変位ベクトル表示", pos = wx.DefaultPosition, size = wx.Size( 980, 600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        self.dammy1_figure = Figure(figsize=(8, 4.3), dpi=100)
        self.dammy1_canvas = FigureCanvasWxAgg(self, -1, self.dammy1_figure)
        self.dammy1_navigationToolbar = NavigationToolbar2Wx(self.dammy1_canvas)
        self.dammy1_navigationToolbar.Realize()
        self.dammy1_navigationToolbar.update()	

        import configdata
        self.mpoint = configdata.dis.shape[1]
        self.scale = 3000  # 仮設定(表示倍率）
        self.data = configdata.dis.sel(layer=0, features=["dis_x", "dis_y"], stats="mu").values
        self.pxpy = configdata.pxpys.sel(layer=0, features=["x", "y"]).values
        self.bsize = configdata.bss.sel(point=0, layer=0, features="y").values
        self.numframe = self.data.shape[0]

        gSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer34 = wx.BoxSizer( wx.VERTICAL ) # 右上
        bSizer34.Add(self.dammy1_canvas, 0, wx.EXPAND)
        bSizer34.Add(self.dammy1_navigationToolbar, 0, wx.EXPAND)
        gSizer1.Add( bSizer34, 0, wx.EXPAND, 0 )

        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_sliderDD = wx.Slider(self, wx.ID_ANY, 0, 0, self.numframe, wx.DefaultPosition, wx.Size(830, 30), style=wx.SL_LABELS | wx.SL_AUTOTICKS)
        self.m_sliderDD.SetTickFreq(20)
        bSizer19.Add(self.m_sliderDD, 0, wx.ALIGN_BOTTOM | wx.BOTTOM, 50)
        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, u"---", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE)
        bSizer19.Add(self.m_textCtrl3, 0, wx.ALIGN_BOTTOM | wx.BOTTOM, 40)

        gSizer1.Add(bSizer19, 1, wx.ALIGN_BOTTOM, 50)

        self.Bind(wx.EVT_SLIDER, self.m_replotsliderRD)

        self.SetSizer( gSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # 相対変位計算
        configdata.Rdis = self.data[0, :, :].reshape(1, self.data.shape[1], 2)
        for i in range(self.data.shape[0]-1):
            a = self.data[i+1, :, :] -self.data[i, :, :]
            a1 =a.reshape(1, self.data.shape[1], 2)
            configdata.Rdis =np.vstack((configdata.Rdis,a1))
        self.Rdis = configdata.Rdis
        frame = 0
        cv2img = cv2.imread(configdata.image_filelist[0])
        self.im = cv2.cvtColor(cv2img, cv2.COLOR_BGR2RGB)

        self.dammy1_figure.subplots_adjust(left=0.005, right=0.995, bottom=0.1, top=0.9)
        self.dammy1_axes = self.dammy1_figure.add_subplot(111, facecolor='black')

        self.dammy1_axes.minorticks_on()
        self.dammy1_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8,
                                 bottom='on', left='on')
        self.dammy1_axes.grid(True)
        self.dammy1_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.dammy1_axes.set_title('RelativeDisplacement')
        self.dammy1_axes.imshow(self.im)
        self.dammy1_axes.quiver(self.pxpy[:, 0], self.pxpy[:, 1], self.Rdis[frame, :, 0] * self.scale, self.Rdis[frame, :, 1] * self.scale,
                                angles='xy', width=0.005,color='red',scale=self.scale)
        self.dammy1_canvas.draw()

    def m_replotsliderRD(self, event):
        import configdata
        self.mpoint = configdata.dis.shape[1]
        self.scale = 3000  # 仮設定(表示倍率）
        self.data = configdata.dis.sel(layer=0, features=["dis_x", "dis_y"], stats="mu").values
        self.pxpy = configdata.pxpys.sel(layer=0, features=["x", "y"]).values
        self.bsize = configdata.bss.sel(point=0, layer=0, features="y").values
        frame = self.m_sliderDD.GetValue()
        cv2img = cv2.imread(configdata.image_filelist[0])
        if self.dammy1_axes != None:
            self.dammy1_axes.cla()
        self.im = cv2.cvtColor(cv2img, cv2.COLOR_BGR2RGB)
        self.Rdis = configdata.Rdis

        self.dammy1_figure.subplots_adjust(left=0.005, right=0.995, bottom=0.1, top=0.9)
        self.dammy1_axes = self.dammy1_figure.add_subplot(111, facecolor='black')

        self.dammy1_axes.minorticks_on()
        self.dammy1_axes.tick_params(axis='both', which='major', direction='inout', colors="black", labelsize=8,
                                     bottom='on', left='on')
        self.dammy1_axes.grid(True)
        self.dammy1_axes.tick_params(axis='both', which='minor', direction='inout', length=5, colors="black")
        self.dammy1_axes.set_title('RelativeDisplacement')
        self.dammy1_axes.imshow(self.im)
        self.dammy1_axes.quiver(self.pxpy[:, 0], self.pxpy[:, 1], self.Rdis[frame, :, 0] * self.scale, self.Rdis[frame, :, 1] * self.scale,
                                angles='xy', width=0.005, color='red', scale=self.scale)
        self.dammy1_canvas.draw()
