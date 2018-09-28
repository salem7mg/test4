#! env python
# -*- coding: utf-8 -*-
# Date: 2018/05/17
# Filename: draw 

"""
画像描画モジュール
"""

__author__ = 'noda'
__date__ = "2018/05/17"

import colorsys

import cv2
import numpy as np


def draw_displacement(img, dis, pxpys, bss, scale, thickness=1):
    """
    変位結果を描画

    :param img: 入力画像（出力画像）
    :param dis: 変位（軸：計測点、軸)
    :param pxpys: 計測点の座標
    :param bss: ブロックサイズ
    :param scale: 拡大率
    :param thickness: 矢印の太さ
    :type dis: np.ndarray
    :type pxpys: np.ndarray
    :type bss: np.ndarray
    """
    u = dis[:, 0]
    v = dis[:, 1]
    colors = color_from_direction(u, v)
    [cvArrow(img=img, pt1=pxpy + bs / 2, pt2=pxpy + bs / 2 + d * scale, color=color, thickness=thickness)
     for pxpy, bs, d, color in zip(pxpys, bss, dis, colors)]


def draw_eigen_vector(img, V, pxpys, bss, scale, n, thickness=1):
    """
    固有ベクトルを描画

    :param img: 入力画像
    :param V: 固有ベクトル
    :param pxpys: 計測点の座標
    :param bss: ブロックサイズ
    :param scale: 拡大率
    :param n: n番目の固有ベクトルを描画
    :param thickness: 矢印の太さ
    :type pxpys: np.ndarray
    :type bss: np.ndarray
    """
    u = np.array(V[:int(len(V) / 2), n].real)
    v = np.array(V[int(len(V) / 2):, n].real)
    dis = np.hstack((u.reshape((-1, 1)), v.reshape((-1, 1))))
    draw_displacement(img, dis, pxpys, bss, scale, thickness)


def color_from_direction(u, v):
    """
    ベクトルの向きに応じてベクトルの色を変更
    色の割り振りはHSVに準拠

    :param u: x方向, shape=(計測点, 1)
    :param v: y方向, shape=(計測点, 1)
    :return: RGB値, shape=(計測点, 1)
    """
    # 虚数に変換して角度を算出
    j = np.zeros(len(u), dtype=np.complex)
    j.real = u
    j.imag = v
    angle = np.angle(j) + np.pi  # 0~2*pi
    colors = []
    for a in angle:
        h = a / (2 * np.pi)
        rgb = (np.array(colorsys.hsv_to_rgb(h, 1.0, 1.0)) * 255).astype(np.int)
        colors.append(rgb.tolist())
    return colors


def cvArrow(img, pt1, pt2, color, thickness=1, linetype=8, shift=0):
    """
    画像上に矢印を描画
    numpyの配列は関数をまたいでも中身の変更が保存されるため、特に返り値は設定していない

    :param img: 入力画像（出力画像）
    :param pt1: 矢印の始点
    :param pt2: 矢印の終点
    :param color: 矢印の色（RGB)
    :param thickness: 矢印の太さ
    :param linetype: cv2.lineの引数(8-connected line)
    :param shift: cv2.lineの引数(Number of fractional bits in the point coordinates.)
    """
    pt1 = pt1.astype(np.int32)
    pt2 = pt2.astype(np.int32)
    cv2.line(img, tuple(pt1), tuple(pt2), color, thickness, linetype, shift)
    vx = pt2[0] - pt1[0]
    vy = pt2[1] - pt1[1]
    v = np.sqrt(vx ** 2 + vy ** 2)
    ux = vx / v
    uy = vy / v
    # 矢印の幅の部分
    w = 5
    h = 10
    try:
        ptl = (int(pt2[0] - uy * w - ux * h), int(pt2[1] + ux * w - uy * h))
        ptr = (int(pt2[0] + uy * w - ux * h), int(pt2[1] - ux * w - uy * h))
    except:
        ptl = pt2
        ptr = pt2
    # 矢印の先端を描画する
    cv2.line(img, tuple(pt2), tuple(ptl), color, thickness, linetype, shift)
    cv2.line(img, tuple(pt2), tuple(ptr), color, thickness, linetype, shift)


if __name__ == "__main__":
    pass
