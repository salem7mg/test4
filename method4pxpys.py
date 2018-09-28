#! env python
# -*- coding: utf-8 -*-
# Date: 2017/12/14
# Filename: method4pxpys

"""
    計測点を選択するための関数
"""

import itertools

import numpy as np
from PyQt5.QtGui import *

__author__ = 'noda'
__date__ = "2017/12/14"

def debug(message):
    import sys
    import inspect
    callerframerecord = inspect.stack()[1]
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    print(info.filename, 'func=%s' % info.function, 'line=%s:' % info.lineno, message)

class Method(object):
    def __init__(self, initial_mode):
        debug('')
        self.mode = initial_mode
        self.pxpys = []
        self.bss = []
        self.pxpys_background = []
        self.bss_background = []
        self.params = {}
        self.bs = None
        self.scale = None
        self.press_count = False
        self.first_pos = []
        self.is_background = False  # background選択フラグ

    def set_pxpys(self, pxpy):
        """
        pxpysのセッター

        :param pxpy:
        """
        debug('')
        if self.is_background:
            self.pxpys_background.append(pxpy)
        else:
            self.pxpys.append(pxpy)

    def set_bss(self, bs):
        """
        bssのセッター

        :param bs:
        """
        debug('')
        if self.is_background:
            self.bss_background.append(bs)
        else:
            self.bss.append(bs)

    def mousePressEvent(self):
        """
        マウスクリック時のイベント
        modeによって挙動をスイッチ

        :return: None
        """
        debug('')
        if self.mode == 0:
            return self.free
        elif self.mode == 1:
            return self.line
        elif self.mode == 2:
            return self.area

    def free(self, event: QMouseEvent):
        """
        １点ずつクリックで選択

        :param event: QMouseEvent
        """
        debug('')
        pxpy = np.array([event.x(), event.y()]) / self.scale
        pxpy = pxpy.astype(np.int)
        self.set_pxpys(pxpy)
        self.set_bss(self.bs)

    def line(self, event: QMouseEvent):
        """
        ２点をクリックして直線上に選択点を配置

        :param event: QMouseEvent
        """
        debug('')
        if not self.press_count:
            self.first_pos = (np.array([event.x(), event.y()]) / self.scale).astype(np.int)
            self.press_count = True
        elif self.press_count:
            distance_x = int((event.x() / self.scale - self.first_pos[0]) / self.params["num_block"])
            distance_y = int((event.y() / self.scale - self.first_pos[1]) / self.params["num_block"])
            for i in range(self.params["num_block"]):
                pxpy = [self.first_pos[0] + i * distance_x,
                        self.first_pos[1] + i * distance_y]
                self.set_pxpys(pxpy)
                self.set_bss(self.bs)
            self.press_count = False

    def area(self, event: QMouseEvent):
        """
        ２点をクリックして領域内を選択点で埋める

        :param event: QMouseEvent
        """
        debug('')
        if not self.press_count:
            self.first_pos = (np.array([event.x(), event.y()]) / self.scale).astype(np.int)
            self.press_count = True
        elif self.press_count:
            pxs = range(self.first_pos[0], int(event.x() / self.scale), self.params["stride_x"])
            pys = range(self.first_pos[1], int(event.y() / self.scale), self.params["stride_y"])
            for pxpy in itertools.product(pxs, pys):
                self.set_pxpys(pxpy)
                self.set_bss(self.bs)
            self.press_count = False
