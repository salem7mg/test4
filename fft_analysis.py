#! env python
# -*- coding: utf-8 -*-
# Date: 2017/12/18
# Filename: fft_analysis

"""
周波数解析のモジュール群
"""

import cv2
import numpy as np
from scipy.signal import firwin, lfilter

__author__ = 'noda'
__date__ = "2017/12/18"


def fir_filter(x, fs, numtaps, cutoff, method):
    """
    FIRフィルター

    :param x: Input
    :param fs: 周波数
    :param numtaps: タップ数
    :param cutoff: カットオフ周波数
    :param method: "lowpass", "bandstop", "highpass" or "bandpass"
    :return: Output
    """
    nyq = fs / 2.0  # ナイキスト周波数
    fe = cutoff / nyq  # カットオフ周波数
    pass_zero = None

    if "lowpass" in method or "bandstop" in method:
        pass_zero = True
    elif "highpass" in method or "bandpass" in method:
        pass_zero = False

    b = firwin(numtaps, fe, pass_zero=pass_zero)

    # FIRフィルタ
    y = lfilter(b, [1], x)
    return y


def fft(data: np.ndarray, fs: float) -> object:
    """
    1D FFT

    :param data: 1D ndarray
    :param fs: frequency
    :return: Amplitude spectrum, Frequency list
    """
    n = len(data)
    hamming = np.hamming(n)
    # hamming window
    data_window = data * hamming

    x = np.fft.fft(data_window)
    frequency = np.fft.fftfreq(n, d=1.0 / fs)

    amplitude = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in x]

    return amplitude[:int(n / 2)], frequency[:int(n / 2)]


def fft2d(img):
    """
    周波数画像の作成

    :param img: Input image
    :return: FFT image
    :rtype: np.ndarray
    """
    x = np.fft.fft2(img)
    x = np.fft.fftshift(x)
    x_abs = np.absolute(x)
    x_abs[x_abs < 1] = 1  # Assign 1 to elements(<1)
    p = np.log10(x_abs)  # Power spectrum

    # Normalize
    p_norm = p / np.amax(p)
    return p_norm


def high_pass(img_fft, cut_off):
    """
    ハイパスした領域の平均振幅を計算

    :param img_fft: Input FFT image
    :param cut_off: Cutoff frequency, e.g. 2, 4, 8...
    :return: Power x, Power y
    """
    center = (np.array(img_fft.shape) / 2).astype(np.int64)
    w = int(img_fft.shape[1] / 2 * (cut_off - 1) / cut_off)
    h = int(img_fft.shape[0] / 2 * (cut_off - 1) / cut_off)
    low_power_x = np.sum(img_fft[:, center[1] - w:center[1] + w])  # x方向
    low_power_y = np.sum(img_fft[center[0] - h:center[0] + h, :])  # y方向
    n_low_x = img_fft.shape[0] * 2 * w  # 画素数(x)
    n_low_y = img_fft.shape[1] * 2 * h  # 画素数(y)

    high_power_x = np.sum(img_fft) - low_power_x
    high_power_y = np.sum(img_fft) - low_power_y
    n_high_x = img_fft.shape[0] * img_fft.shape[1] - n_low_x
    n_high_y = img_fft.shape[0] * img_fft.shape[1] - n_low_y
    high_power_norm_x = high_power_x / n_high_x
    high_power_norm_y = high_power_y / n_high_y
    return high_power_norm_x, high_power_norm_y


def fft_score(pxpy, bs, image):
    """
    fft score計算用サブルーチン

    :param pxpy: 座標値
    :param bs: ブロックサイズ
    :param image: 入力画像
    :return: x, y方向のfft score
    :rtype: float, float
    """
    px, py = pxpy
    bsx, bsy = bs
    crop_image = image[py:py + bsy, px:px + bsx]
    img_fft = fft2d(crop_image)
    fft_x, fft_y = high_pass(img_fft, cut_off=2)
    return fft_x, fft_y


def cal_fft_score(pxpys, bss, img_path):
    """
    fft score計算

    :param pxpys: 全ブロックの座標値
    :param bss: 全ブロックのブロックサイズ
    :param img_path: 画像パス
    :return: 計算結果
    :rtype: np.ndarray
    """
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    fft_xy = [fft_score(pxpy, bs, image) for pxpy, bs in zip(pxpys, bss)]
    return np.array(fft_xy)
