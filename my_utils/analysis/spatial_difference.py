#! env python
# -*- coding: utf-8 -*-
# Date: 2018/04/25
# Filename: spatial_difference

import numpy as np
import xarray as xr

__author__ = 'noda'
__date__ = "2018/04/25"

"""
変位の空間差分を算出するモジュール
"""


def calc_dis_diff(dis, dis_diff, index, index_ij1):
    """
    変位結果の差分を計算する関数
    平均については引き算、偏差については足し算

    :param dis: 変位結果
    :param dis_diff: 差分結果
    :param index: 基準となる計測点の番号
    :param index_ij1: 差分をとる計測点の番号
    :return:
    """
    tmp_shape = (dis.shape[0], 1, dis.shape[2], dis.shape[3])
    tmp = xr.DataArray(np.empty(shape=tmp_shape), coords=dis.coords, dims=dis.dims)

    # mu
    # 変位は引き算
    tmp.loc[dict(features=["dis_x", "dis_y"], stats="mu")] = \
        dis.sel(point=index, features=["dis_x", "dis_y"], stats="mu") - \
        dis.sel(point=index_ij1, features=["dis_x", "dis_y"], stats="mu")
    # 相関係数は平均
    tmp.loc[dict(features="max_corr", stats="mu")] = \
        (dis.sel(point=index, features="max_corr", stats="mu") +
         dis.sel(point=index_ij1, features="max_corr", stats="mu")) / 2

    # sigma
    # 偏差は足し算
    tmp.loc[dict(stats="sigma")] = \
        dis.sel(point=index, stats="sigma") + dis.sel(point=index_ij1, stats="sigma")

    # concat
    dis_diff = xr.concat([dis_diff, tmp], dim="point")
    return dis_diff


def calc_pxpys_diff(pxpys, pxpys_diff, index, index_ij1):
    """
    ２点間の中心を計算する関数
    差分計測点の座標は２点間の中心とする

    :param pxpys: 元の計測点の座標
    :param pxpys_diff: 差分計測点の座標
    :param index: 基準となる計測点の番号
    :param index_ij1: 差分をとる計測点の座標
    :return:
    """
    # 座標の平均
    tmp = (pxpys.sel(point=index) + pxpys.sel(point=index_ij1)) / 2
    # concat
    pxpys_diff = xr.concat([pxpys_diff, tmp], dim="point")
    return pxpys_diff


def adjacent_diff(dis, pxpys):
    """
    変位結果の空間差分を計算する関数
    ただし計測点はメッシュ的に並べられている前提

    :param dis: 変位結果（軸：時間、計測点、特徴量、統計量）
    :param pxpys: 計測点（軸：計測点、xy）
    :return:
    """
    # x, yそれぞれのユニークな座標
    px_unique = np.unique(pxpys[:, 0])
    py_unique = np.unique(pxpys[:, 1])

    # 結果を保持するための仮データを作成
    shape = (dis.shape[0], 0, dis.shape[2], dis.shape[3])
    dis_diff = xr.DataArray(np.empty(shape), coords=dis.coords, dims=dis.dims)
    pxpys_diff = xr.DataArray(np.empty((0, 2)), coords=pxpys.coords, dims=pxpys.dims)
    for i in range(len(px_unique)):
        for j in range(len(py_unique)):
            # 基準となる座標をとる計測点の番号を取得
            index = np.where((pxpys[:, 0] == px_unique[i]) & (pxpys[:, 1] == py_unique[j]))[0]
            # i+1(左隣）
            if i < len(px_unique) - 1:
                index_i1 = np.where((pxpys[:, 0] == px_unique[i + 1]) & (pxpys[:, 1] == py_unique[j]))[0]
                dis_diff = calc_dis_diff(dis, dis_diff, index, index_i1)
                pxpys_diff = calc_pxpys_diff(pxpys, pxpys_diff, index, index_i1)

            # j+1（下隣）
            if j < len(py_unique) - 1:
                index_j1 = np.where((pxpys[:, 0] == px_unique[i]) & (pxpys[:, 1] == py_unique[j + 1]))[0]
                dis_diff = calc_dis_diff(dis, dis_diff, index, index_j1)
                pxpys_diff = calc_pxpys_diff(pxpys, pxpys_diff, index, index_j1)
    return dis_diff, pxpys_diff


if __name__ == "__main__":
    pass
