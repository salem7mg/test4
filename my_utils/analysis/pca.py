#! env python
# -*- coding: utf-8 -*-
# Date: 2018/04/20
# Filename: pca

from typing import Tuple

import numpy as np

__author__ = 'noda'
__date__ = "2018/04/20"

"""
PCA解析用モジュール
"""


def pca(dis, n_comp) -> Tuple[np.ndarray, np.ndarray]:
    """
    PCA解析

    :param dis: 変位データ（時間、計測点、変位）
    :param n_comp: 上位n番目までの主成分
    :return: 固有値D,　固有ベクトルV
    """
    w = np.concatenate((dis[:, :, 0], dis[:, :, 1]), axis=1)
    # 分散共分散行列の算出
    covar = np.cov(w, rowvar=False, bias=True)
    # 固有値、固有ベクトルの算出
    d, v = np.linalg.eig(covar)
    # 寄与率に変換
    d = d.real / sum(d.real)
    return d[:n_comp], v[:, :n_comp]


def eigen_value_sequence(v, dis) -> np.ndarray:
    """
    主成分の時間振幅を算出

    :param v: 固有ベクトルV
    :param dis: 変位データ（時間、計測点、変位）
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


if __name__ == "__main__":
    pass
