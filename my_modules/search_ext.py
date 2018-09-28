#! env python
# -*- coding: utf-8 -*-
# Date: 2017/12/14
# Filename: search_ext

import glob
import os
from itertools import chain

__author__ = 'noda'
__date__ = "2017/12/14"


def search(search_dir, ext_list):
    """
    指定した拡張子のファイルを検索

    :param search_dir: 検索するフォルダ
    :param ext_list: 検索する拡張子 e.g. ["bmp", "pgm"]
    :return: 選択した拡張子に適合するファイルリスト
    :rtype: list
    """
    file_list = list(chain.from_iterable([glob.glob(os.path.join(search_dir, "*." + ext)) for ext in ext_list]))
    file_list.sort()
    return file_list
