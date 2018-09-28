#! env python
# -*- coding: utf-8 -*-
# Date: 2018/05/15
# Filename: load

"""
各種ファイルロード用モジュール
"""

import cv2
import pickle
import sys

from PyQt5.QtWidgets import QApplication, QFileDialog

__author__ = 'noda'
__date__ = "2018/05/15"


def load_pickle(return_path=False):
    """
    pickleファイル読み込み関数

    :param return_path: True: パスも返り値に追加
    :return: pickle解凍データ
    """
    # すでにアプリケーションが立ち上がっているか確認
    app = QApplication.instance()
    if not app:
        _ = QApplication(sys.argv)
    fp = QFileDialog.getOpenFileName(filter="pickle(*.pickle)")[0]
    with open(fp, "rb") as f:
        data = pickle.load(f)
    if return_path:
        return data, fp
    else:
        return data


def load_image(color=True, return_path=False):
    """
    画像読み込み関数

    :param color: True: カラースケール, False: グレースケール
    :param return_path: True: パスも返り値に追加
    :return: image(openCV)
    """
    # すでにアプリケーションが立ち上がっているか確認
    app = QApplication.instance()
    if not app:
        _ = QApplication(sys.argv)
    fp = QFileDialog.getOpenFileName(filter="Image (*.bmp *.pgm *.png *.jpg)")[0]
    if color:
        image = cv2.imread(fp)
    else:
        image = cv2.imread(fp, cv2.IMREAD_GRAYSCALE)
    if return_path:
        return image, fp
    else:
        return image


if __name__ == "__main__":
    pass
