#! env python
# -*- coding: utf-8 -*-
# Date: 2018/01/09
# Filename: fft_image

import numpy as np

__author__ = 'noda'
__date__ = "2018/01/09"


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


if __name__ == "__main__":
    pass
