#! env python
# -*- coding: utf-8 -*-
# Date: 2017/12/18
# Filename: eof_analysis

"""
EOF(PCA)解析
"""

import numpy as np

__author__ = 'noda'
__date__ = "2017/12/18"


def eof(data: np.ndarray, n_comp: int) -> object:
    """
    EOF(PCA)

    :param data: 変位データ
    :param n_comp: 上位n位
    :return: D, V
    """
    x = data[:, :, 0]
    y = data[:, :, 1]
    w = np.concatenate((x, y), axis=1)
    # 分散共分散行列の算出
    covar = np.cov(w, rowvar=False, bias=True)
    # 固有値、固有ベクトルの算出
    d, v = np.linalg.eig(covar)
    # 寄与率に変換
    d = d.real / sum(d.real)
    return d[:n_comp], v[:, :n_comp]


def eigen_sequence(v, dis):
    """
    主成分の時間振幅を算出

    :param v: 固有ベクトル
    :param dis: 変位データ
    :return: 主成分の時間振幅
    """
    v = v.real
    sequence = np.zeros((dis.shape[0], v.shape[1]))
    w = np.concatenate((dis[:, :, 0], dis[:, :, 1]), axis=1)
    # 時間平均を減算
    w -= w.mean(axis=0)
    for i in range(v.shape[1]):
        sequence[:, i] = np.dot(w, v[:, i])
    return sequence
