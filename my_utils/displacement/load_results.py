#! env python
# -*- coding: utf-8 -*-
# Date: 2018/04/12
# Filename: load_results

import pickle
import sys

from PyQt5.QtWidgets import QApplication, QFileDialog

__author__ = 'noda'
__date__ = "2018/04/12"

"""
変位計測結果を読み込むモジュール
"""


def load(file_path=None):
    """
    file pathのpickleファイルを読み込み
    file pathを渡していなければファイル選択ダイアログが起動

    :param file_path: 読み込みたいファイルパス
    :return: pickle.load()結果
    """
    if not file_path:
        # すでにアプリケーションが立ち上がっているか確認
        app = QApplication.instance()
        if not app:
            _ = QApplication(sys.argv)
        fd = QFileDialog()
        file_path = fd.getOpenFileName(filter="pickle (*.pickle)")[0]
    with open(file_path, "rb") as f:
        results = pickle.load(f)
    return results


if __name__ == "__main__":
    pass
