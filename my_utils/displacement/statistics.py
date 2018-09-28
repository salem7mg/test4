#! env python
# -*- coding: utf-8 -*-
# Date: 2018/04/18
# Filename: statistics

from copy import copy
from functools import partial
from itertools import combinations
from multiprocessing import Pool

import numpy as np
import pandas as pd
from statsmodels import robust

__author__ = 'noda'
__date__ = "2018/04/18"

"""
変位計測の統計処理モジュール
"""


def mad_per_frame(results):
    """
    robust_statistics関数のサブルーチン

    :param results:
    """
    # median
    med = np.median(results, axis=0)
    # MAD
    mad = robust.mad(results, c=0.6745, axis=0)
    # concat
    merged_arr = np.concatenate([med[:, :, np.newaxis], mad[:, :, np.newaxis]], axis=2)
    return merged_arr


def robust_statistics_with_mad(sampling_results):
    """
    MAD（中央絶対偏差）を用いた統計量のロバスト推定

    :param sampling_results:
    """
    with Pool() as p:
        estimation_results = p.map(func=mad_per_frame, iterable=sampling_results)
    return np.array(estimation_results)


def sum_of_euclid_norm(combination, dis):
    """
    時系列データのユークリッドノルムの和を算出する

    :param dis: 変位データ（時間、計測点、変位（x, y)）
    :param combination: 組み合わせ
    :return: 時系列のユークリッドノルムの和
    """
    dis_1 = dis[:, combination[0], :]
    dis_2 = dis[:, combination[1], :]
    euclid_norm_per_time = np.linalg.norm((dis_1 - dis_2), axis=1)
    return np.sum(euclid_norm_per_time)


def similarity_calculation(dis):
    """
    変位データの計測点毎に他の計測点との類似度を算出する

    :param dis: 変位データ（時間、計測点、変位(x, y))
    :return: 類似度マップ （計測点×計測点）行列
    """
    # 組み合わせ
    combination = combinations(range(dis.shape[1]), r=2)
    # 後で同じ順番で結果を取り出すためのコピー
    comb_copy = copy(combination)
    with Pool() as p:
        results = p.map(func=partial(sum_of_euclid_norm, dis=dis), iterable=combination)

    # 結果の取り出し＆格納
    similarity_map = np.zeros((dis.shape[1], dis.shape[1]))
    for res, comb in zip(results, comb_copy):
        similarity_map[comb[0], comb[1]] = res
        similarity_map[comb[1], comb[0]] = res
    return similarity_map


def pickup_top_n_similarity(dis, n):
    """
    計測点毎にの他の計測点との類似度を計算し、その中で上位n%に入る計測点のインデックスを取得する

    :param dis: 変位データ（時間、計測点、変位(x, y))
    :param n: 上位n% パーセントであることに注意!!
    :return: インデックス
    """
    similarity_map = similarity_calculation(dis)
    # DataFrameに変換（後のソートやインデックスの取得が簡単なため）
    df = pd.DataFrame(similarity_map)
    # 取得してくるインデックスの個数
    pickup = np.ceil(len(similarity_map) * n).astype(np.int64)
    # 上位からインデックスを取得
    indices = df.mean().sort_values(ascending=True).index[:pickup]
    return indices.tolist()


if __name__ == "__main__":
    pass
