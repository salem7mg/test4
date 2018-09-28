#! env python
# -*- coding: utf-8 -*-

import os
import sys
import wx
import mainWindow

if __name__ == '__main__':
    app = wx.App(False)
    frame = mainWindow.MainWindow(None)
    frame.Show(True)
    app.MainLoop()