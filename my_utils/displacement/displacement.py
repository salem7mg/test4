#! env python
# -*- coding: utf-8 -*-
# Date: 2017/12/14
# Filename: displacement

import itertools
import math
from functools import partial
from multiprocessing import Pool, cpu_count

import cv2
import numpy as np
from scipy import optimize

__author__ = 'noda'
__date__ = "2017/12/14"


def sad(frame: np.ndarray, base_frame: np.ndarray) -> np.ndarray:
    """
    SAD

    :param frame: 入力画像
    :param base_frame: テンプレート画像
    :return: 類似度マップ
    """
    frame = frame.astype(np.int16)
    base_frame = base_frame.astype(np.int16)
    width = base_frame.shape[1]
    height = base_frame.shape[0]
    shift = frame.shape[0] - height
    res = [np.sum(np.abs(base_frame - frame[j:j + height, i:i + width])) for j in range(shift) for i in range(shift)]
    res = np.array(res)
    res = res.reshape((shift, shift))
    return res


def slide_image(img: np.ndarray, slide: float) -> np.ndarray:
    """
    画素ずらしの画像を作成

    :param img: 入力画像
    :param slide: 移動画素数
    :return: 画素ずらし画像
    """
    img_tmp = np.zeros(img.shape)
    img_tmp[1:, 1:] = img[0:-1, 0:-1]
    imo_slide = (1 - slide) * img + slide * img_tmp
    return np.uint8(imo_slide)


def avoid_zero_division(x, th):
    """
    0割防止用関数

    :param x: 入力
    :param th: スレッショルド
    :return:
    """
    if abs(x) > th:
        return x
    else:
        if x == 0.0:
            return th
        else:
            return th * np.sign(x)


def calc_brightness(image):
    """
    白飛び率を考慮に入れた平均輝度値のスコア

    :param image: input image
    :return: brightness score
    :rtype: float
    """
    mean_brightness = np.mean(image) / 255
    over_expose = np.ones(image.shape)
    over_expose[image >= 254] = 0
    over_expose_score = np.mean(over_expose)
    return mean_brightness * over_expose_score


def crop_image_after_displacement(image, pxpy, bs, dx, dy):
    """
    変位先の画像を切り出す

    :param image: 入力画像
    :param pxpy: 計測点の座標
    :param bs: ブロックサイズ
    :param dx: x変位量
    :param dy: y変位量
    :return: 切りだされた画像
    """
    px = pxpy[0]
    py = pxpy[1]

    # 四捨五入関数
    def my_round(x):
        return int((x * 2 + 1) // 2)

    dx = my_round(dx)
    dy = my_round(dy)

    cropped_image = image[py + dy: py + dy + bs[1], px + dx: px + dx + bs[1]]
    return cropped_image


def correlation_curve(res, peak_x, peak_y, fit_range):
    """
    フィッティングレンジ内での相関係数およびその時のxy座標を取得

    :param res: 相関マップ
    :param peak_x: 最大値を取るx座標
    :param peak_y: 最大値を取るy座標
    :param fit_range: フィッティングレンジ
    :return: 相関係数、xyの座標値
    """
    # 相関関数
    corr_curve_x = res[peak_y, max(0, peak_x - fit_range):min(res.shape[1], peak_x + fit_range + 1)]
    corr_curve_y = res[max(0, peak_y - fit_range):min(res.shape[0], peak_y + fit_range + 1), peak_x]
    # xおよびyの座標値
    x = np.arange(res.shape[1])[max(0, peak_x - fit_range):min(res.shape[1], peak_x + fit_range + 1)]
    y = np.arange(res.shape[0])[max(0, peak_y - fit_range):min(res.shape[0], peak_y + fit_range + 1)]
    return corr_curve_x, corr_curve_y, x, y


def add_gaussian_noise(image, sigma_ratio=1.4*10**(-2)):
    """
    画像にガウスノイズを付与
    偏差は光ショットノイズの実測値から算出 (sigma^2 = (2.8 / 200) * 輝度値)

    :param image: 入力画像
    :param sigma_ratio: 光ショットノイズの係数
    :return: ノイズ付与後の画像
    """
    # 画素毎の輝度値によるノイズの偏差
    sigma = np.sqrt(image * sigma_ratio)
    # floatへ型変換(マイナスへの対応）
    image_float = image.astype(np.float)
    # 偏差sigmaのガウスノイズを生成
    noise = np.random.normal(loc=0.0, scale=sigma, size=image.shape)
    # 0~255の範囲にクリップしつつ、四捨五入
    noised_image = np.round(np.clip(image_float + noise, a_min=0, a_max=255))
    return noised_image.astype(np.uint8)


class Fitting(object):
    """
    サブピクセル推定時のフィッティング方法を管理するクラス
    """

    def __init__(self, fit_method, fit_range, shift):
        """

        :param fit_method: フィッティング方法
        :param fit_range: フィッティングレンジ
        :param shift: 探索範囲
        """
        self.fit_method = fit_method
        self.fit_range = fit_range
        self.shift = shift

    def parabola_fit(self, res, peak_x, peak_y):
        """
        1次元のパラボラフィッティング

        :param res: 相関マップ
        :param peak_x: 最大値を取るx座標
        :param peak_y: 最大値を取るy座標
        :return: 変位
        """
        corr_curve_x, corr_curve_y, x, y = correlation_curve(res, peak_x, peak_y, self.fit_range)
        # 二次関数フィッティング
        poly_x = np.polyfit(x, corr_curve_x, 2)
        poly_y = np.polyfit(y, corr_curve_y, 2)
        # 0割防止
        a_x = avoid_zero_division(poly_x[0], 1e-5)
        a_y = avoid_zero_division(poly_y[0], 1e-5)
        # 極値を取る値を算出
        peak_x_fit = -poly_x[1] / (2 * a_x)
        peak_y_fit = -poly_y[1] / (2 * a_y)
        # 変位に換算
        dx = (peak_x_fit - self.shift * self.fit_range) / self.fit_range
        dy = (peak_y_fit - self.shift * self.fit_range) / self.fit_range
        return dx, dy

    def parabola_2dfit(self, res, peak_x, peak_y):
        """
        2次元同時パラボラフィッティング

        :param res: 相関マップ
        :param peak_x: 最大値を取るx座標
        :param peak_y: 最大値を取るy座標
        :return: 変位
        """

        def func2d(_x, _y, a1, a2, a3, a4, a5, a6):
            """
            2変数による曲面 : z = a1x**2 + a2y**2 a3xy + a4x + a5y + a6
            """
            return a1 * _x ** 2 + a2 * _y ** 2 + a3 * _x * _y + a4 * _x + a5 * _y + a6

        def resfunc_2d(param, _x, _y, _z):
            """
            コスト関数
            """
            residual = _z - func2d(_x, _y, param[0], param[1], param[2], param[3], param[4], param[5])
            return residual

        def dxdy(r, fit_range, shift):
            """
            曲面の極値を求めて、変位に変換
            """
            _dx = - (2 * r[1] * r[3] - r[2] * r[4]) / (4 * r[0] * r[1] - r[2] ** 2)
            _dy = - (2 * r[0] * r[4] - r[2] * r[3]) / (4 * r[0] * r[1] - r[2] ** 2)
            _dx = (_dx - shift * fit_range) / fit_range
            _dy = (_dy - shift * fit_range) / fit_range
            return _dx, _dy

        z = res[max(0, peak_y - self.fit_range):min(res.shape[0], peak_y + self.fit_range + 1),
                max(0, peak_x - self.fit_range):min(res.shape[1], peak_x + self.fit_range + 1)]
        x = np.arange(res.shape[1])[max(0, peak_x - self.fit_range):min(res.shape[1], peak_x + self.fit_range + 1)]
        y = np.arange(res.shape[0])[max(0, peak_y - self.fit_range):min(res.shape[0], peak_y + self.fit_range + 1)]

        # flatten
        z = z.flatten()
        xy = np.array(list(itertools.product(y, x)))
        x = xy[:, 1]
        y = xy[:, 0]

        # fit
        param_init = np.array([-0.001, -0.001, -0.001, -0.001, -0.001, -0.001])
        result = optimize.leastsq(resfunc_2d, param_init, args=(x, y, z))
        dx, dy = dxdy(result[0], self.fit_range, self.shift)
        return dx, dy

    def fit(self):
        """
        methodに応じてフィッティング関数を返す

        :return: フィッティング関数
        """
        if self.fit_method == "para":
            return self.parabola_fit
        elif self.fit_method == "para2d":
            return self.parabola_2dfit


def crop_image(frame, pxpy, bs, shift):
    """
    画像を切り出して拡大

    :param frame: 入力画像
    :param pxpy: 計測点の座標（１点）
    :param bs: ブロックサイズ（１点）
    :param shift: 探索範囲
    :return:
    """
    px, py = pxpy
    bsx, bsy = bs
    # image の切り出し
    image = frame[py - shift: py + bsy + shift, px - shift: px + bsx + shift]
    return image


def resize_image(images: list, scale: int) -> list:
    """
    画像を拡大する

    :param images: 画像リスト
    :param scale: 拡大率
    :return: 拡大画像リスト
    """
    scaled_images = [cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
                     for image in images]
    return scaled_images


class Displacement(object):
    """
    変位計測用クラス
    """

    def __init__(self, image_list, base_num, pxpys, bss, scale, shift, fit_method="para", eec=True, method="abs"):
        """

        :param image_list: 画像のファイルパスリスト
        :param base_num: 基準フレームの番号
        :param pxpys: 計測点の座標
        :param bss: ブロックサイズ
        :param scale: 画像拡大率
        :param shift: 探索範囲
        :param fit_method: フィッティング手法
        :param eec: Estimate Error Cancellation
        :param method: 基準フレームからの絶対変位 or 前後フレームでの相対変位
        """
        self.image_list = image_list
        self.base_num = base_num
        self.pxpys = pxpys
        self.bss = bss
        self.scale = scale
        self.shift = shift
        self.method = method
        self.fit = Fitting(fit_method=fit_method, shift=self.shift, fit_range=self.scale).fit()
        # EEC or not EEC
        self.one_point_calculation = self.with_eec if eec else self.without_eec
        # multiprocess時のchunk size設定
        self.chunk_size = math.ceil(len(self.image_list) / cpu_count() / 4)

    def subpixel_estimation(self, src_image, template_image):
        """
        サブピクセル変位推定

        :param src_image: 入力画像
        :param template_image: テンプレート画像
        :return: x変位, y変位, 相関係数の最大値
        """
        # znccによるテンプレートマッチ
        res = cv2.matchTemplate(src_image, template_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, _, max_loc = cv2.minMaxLoc(res)
        peak_x = max_loc[0]
        peak_y = max_loc[1]
        # サブピクセル推定
        dx, dy = self.fit(res, peak_x, peak_y)
        return np.clip(dx, -self.shift, self.shift), np.clip(dy, -self.shift, self.shift), max_val

    def with_eec(self, frame, base_frame, pxpy, bs):
        """
        EEC ON 時の変位計測（画像１ペア, 計測点１点）

        :param frame: 入力画像
        :param base_frame: 基準画像
        :param pxpy: 計測点の座標
        :param bs: ブロックサイズ
        :return: 変位, 相関係数の最大値
        """
        # 画像の切り出し
        src_image = crop_image(frame, pxpy, bs, shift=self.shift)
        template_image = crop_image(base_frame, pxpy, bs, shift=0)
        eec_image = slide_image(src_image, 0.5)
        # 画像拡大
        src_image_scaled, template_image_scaled, eec_image_scaled = resize_image([src_image,
                                                                                  template_image,
                                                                                  eec_image],
                                                                                 self.scale)
        # サブピクセル推定
        dx_eec, dy_eec, max_val1 = self.subpixel_estimation(src_image_scaled, template_image_scaled)
        dx, dy, max_val2 = self.subpixel_estimation(eec_image_scaled, template_image_scaled)
        # EEC処理（平均）
        dx = (dx + dx_eec - 0.5) / 2
        dy = (dy + dy_eec - 0.5) / 2
        max_val = (max_val1 + max_val2) / 2
        return dx, dy, max_val

    def without_eec(self, frame, base_frame, pxpy, bs):
        """
        EEC OFF 時の変位計測（画像１ペア, 計測点１点）

        :param frame: 入力画像
        :param base_frame: 基準画像
        :param pxpy: 計測点の座標
        :param bs: ブロックサイズ
        :return: 変位, 相関係数の最大値
        """
        # 画像の切り出し
        src_image = crop_image(frame, pxpy, bs, shift=self.shift)
        template_image = crop_image(base_frame, pxpy, bs, shift=0)
        # 画像拡大
        src_image_scaled, template_image_scaled = resize_image([src_image, template_image], scale=self.scale)
        # サブピクセル推定
        dx, dy, max_val = self.subpixel_estimation(src_image_scaled, template_image_scaled)
        return dx, dy, max_val

    def one_pair_calculation(self, image_paths):
        """
        画像１ペア分の変位計測

        :param image_paths: 画像パス
        :return: １ペア分の変位計測結果
        """
        base_frame = cv2.imread(image_paths[0], cv2.IMREAD_GRAYSCALE)
        frame = cv2.imread(image_paths[1], cv2.IMREAD_GRAYSCALE)
        # 全計測点を処理
        result_one_pair = [self.one_point_calculation(frame, base_frame, pxpy, bs)
                           for pxpy, bs in zip(self.pxpys, self.bss)]
        return np.array(result_one_pair)

    def run(self):
        """
        変位計測の実行

        :return: Pool.imapオブジェクト
        """
        iterable = None
        # 絶対変位
        if self.method == "abs":
            iterable = [[self.image_list[self.base_num], self.image_list[i]]
                        for i in range(len(self.image_list))]
        # 相対変位
        elif self.method == "rel":
            iterable = [[self.image_list[i], self.image_list[i + 1]] for i in range(len(self.image_list) - 1)]
        func = self.one_pair_calculation
        p = Pool(processes=cpu_count())
        it = p.imap(func=partial(func), iterable=iterable, chunksize=self.chunk_size)
        p.close()
        return it


class Bayesian(Displacement):
    """
    ベイズ的変位計測クラス
    """

    def __init__(self, image_list, base_num, pxpys, bss, scale, shift, fit_method="para", eec=True, method="abs",
                 n_samples=100, sigma=2):
        """

        :param n_samples: サンプリング回数
        :param sigma: ノイズの分散
        """
        # Displacementクラスの継承
        super().__init__(image_list, base_num, pxpys, bss, scale, shift, fit_method, eec, method)
        self.n_samples = n_samples
        self.sigma = sigma

    def one_pair_calculation(self, image_paths):
        """
        画像１ペア分の変位計測

        :param image_paths: 画像パス
        :return: １ペア分の変位計測結果
        """
        base_frame = cv2.imread(image_paths[0], cv2.IMREAD_GRAYSCALE)
        frame = cv2.imread(image_paths[1], cv2.IMREAD_GRAYSCALE)
        # ガウスノイズを付与
        noised_base_frame = add_gaussian_noise(base_frame, self.sigma)
        noised_frame = add_gaussian_noise(frame, self.sigma)
        # 全計測点を処理
        result_one_pair = [self.one_point_calculation(noised_frame, noised_base_frame, pxpy, bs)
                           for pxpy, bs in zip(self.pxpys, self.bss)]
        return np.array(result_one_pair)

    def one_frame_calculation(self, image_paths):
        """
        1フレーム間の変位計測
        n_samples分サンプリングを行う

        :param image_paths: image_paths[0]: base_frame_path, image_paths[1]: frame_path
        :return: 1フレーム間の変位計測結果
        """
        # n_samples分ノイズをランダムに付与して計測
        result_one_frame = [self.one_pair_calculation(image_paths) for _ in range(self.n_samples)]
        return np.array(result_one_frame)

    def run(self):
        """
        変位計測の実行

        :return: pool.imapオブジェクト
        """
        iterable = None
        if self.method == "abs":
            iterable = [[self.image_list[self.base_num], self.image_list[i]]
                        for i in range(len(self.image_list))]
        elif self.method == "rel":
            iterable = [[self.image_list[i], self.image_list[i + 1]] for i in range(len(self.image_list) - 1)]
        func = self.one_frame_calculation
        p = Pool(processes=cpu_count())
        it = p.imap(func=partial(func), iterable=iterable, chunksize=self.chunk_size)
        return it


if __name__ == '__main__':
    pass
