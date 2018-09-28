#! env python
# -*- coding: utf-8 -*-
# Date: 2018/05/15
# Filename: save 

"""
各種ファイルセーブ用モジュール
"""

import pickle
import sys

import cv2
from PyQt5.QtWidgets import QApplication, QFileDialog

__author__ = 'noda'
__date__ = "2018/05/15"


def save_pickle(data):
    """
    pickle形式でデータを保存

    :param data: 保存するデータ
    """
    # すでにアプリケーションが立ち上がっているか確認
    app = QApplication.instance()
    if not app:
        _ = QApplication(sys.argv)
    # ファイル名を入力
    fp = QFileDialog.getSaveFileName(directory="data.pickle", filter="pickle(*.pickle)")[0]
    with open(fp, "wb") as f:
        pickle.dump(data, f)


def save_image(image):
    """
    画像を保存

    :param image: 保存する画像
    """
    # すでにアプリケーションが立ち上がっているか確認
    app = QApplication.instance()
    if not app:
        _ = QApplication(sys.argv)
    # ファイル名を入力
    fp = QFileDialog.getSaveFileName(directory="image.png",
                                     filter="Image (*.bmp *.pgm *.png *.jpg)")[0]
    # 画像の保存
    cv2.imwrite(fp, image)


if __name__ == "__main__":
    pass
