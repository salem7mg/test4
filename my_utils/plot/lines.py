#! env python
# -*- coding: utf-8 -*-
# Date: 2018/04/20
# Filename: fill_plot 

import matplotlib.pyplot as plt

__author__ = 'noda'
__date__ = "2018/04/20"

"""
ラインプロットモジュール
"""


def fill_plot(data_1d, sigma, sigma_ratio=1, ax=None, alpha=0.3):
    """
    sigmaの範囲を編みかけにして表示

    :param data_1d: 1次元変位データ
    :param sigma: 偏差データ
    :param sigma_ratio: 表示(網掛け)するσの範囲
    :param ax: Axesブジェクト
    :param alpha: 透過度
    """
    x = range(len(data_1d))
    upper = data_1d + sigma * sigma_ratio
    lower = data_1d - sigma * sigma_ratio
    # Axesオブジェクトが渡されていない場合
    if not ax:
        fig = plt.figure()
        ax = fig.add_subplot(111)
    # muをプロット
    ax.plot(data_1d)
    # 網掛け範囲をプロット
    ax.fill_between(x, upper, lower, alpha=alpha)
    plt.show()


if __name__ == "__main__":
    pass
