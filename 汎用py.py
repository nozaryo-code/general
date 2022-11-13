# 処理・動作系
import os # ファイルパス操作
import glob # ファイル検索
import shutil # ファイル・ディレクトリ操作（コピーなど）
import re # 正規表現
import sys # コード実行の強制終了
import argparse # コマンドライン引数の取得

import datetime as dt
import random
import pprint as pprint # 辞書を見やすく表示
# importlib.reload(モジュール名)

# 分析系
import pandas as pd
import numpy as np

# 可視化系
import matplotlib as mpl
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
sns.set()

# 設定
pd.options.display.precision = 2 # 小数点以下桁数指定
pd.set_option("display.max_rows", 50) # dfの表示行数
pd.set_option("display.max_columns", 100) # dfの表示カラム数


def main():
    """main処理
    """

    # 変数指定
    # --------------------------------
    # 対象日
    TGT_DATE = 'auto'

    # 実行設定
    exec_dict = {
        'A':True
    }

    # ファイルパス設定
    fpath_dict = {}
    # --------------------------------
    print(f'《input variables》')
    print(f'\tTGT_DATE：{TGT_DATE}')
    print(f'\texec_dict：{exec_dict}')
    print(f'\fpath_dict：{fpath_dict}')
    print()

    tgt_date, exec_dict, fpath_dict = process_variables(
                                                tgt_date = TGT_DATE,
                                                exec_dict = exec_dict,
                                                fpath_dict = fpath_dict)

    # title
    if exec_dict['A'] is True:

        # title
        print('【A】')
        print()


def process_variables(tgt_date, exec_dict, fpath_dict):
    """入力した変数の変換、検証、加工をする

    Args:
        tgt_date (str): 入力変数
        exec_dict (dict): 入力変数
        fpath_dict (dict): 入力変数

    Returns:
        _ : 変換、加工された入力変数
    """

    tgt_date = interpret_tgt_date(tgt_date) # auto → 自動計算
    validate_variables(tgt_date) # 手入力したtgt_dateが正しいかを検証

    date_dict = create_date_dict(tgt_date)

    return tgt_date, date_dict, fpath_dict


def interpret_tgt_date(tgt_date):
    """tgt_dateがautoの場合に日付を自動取得する関数

    Args:
        tgt_date (str): yyyymmdd or "auto"を想定

    Returns:
        yyyymmdd: 新商品販売開始日(火曜)
    """
    if tgt_date == 'auto':

        date_diff = (dt.datetime.now().weekday() + 3) % 7

        base_date = dt.datetime.now() - dt.timedelta(days = date_diff)

        tgt_date = base_date + dt.timedelta(days = 18)
        tgt_date = tgt_date.strftime('%Y%m%d')

    return tgt_date


def validate_variables(tgt_date):
    """変数が問題ないかを確認する

    Args:
        tgt_date (str): yyyymmdd
    """

    print(f'〈validate variables〉')

    if re.search('^[0-9]{8}$',tgt_date) is None:
        print('tgt_dateには yyyymmdd(半角) or "auto"を入力してください')
        print('process END')
        sys.exit()

    if dt.datetime.strptime(tgt_date, '%Y%m%d').weekday() != 1:
        print('tgt_dateには火曜日（新商品発売日）を入力してください')
        print('process END')
        sys.exit()

    print(f'\t >> no problems')
    print()


def get_different_date(date_str, date_delta):
    """起算日から一定日数異なる日付を返す

    Args:
        date_str (str): 起算日
        date_delta (int)): 差

    Returns:
        str: 計算された日付
    """

    date_dt = dt.datetime.strptime(date_str,'%Y%m%d')
    different_date_str  = (date_dt + dt.timedelta(days = date_delta)).strftime('%Y%m%d')

    return different_date_str


def create_date_dict(tgt_date):
    """tgt_dateを基準として計算した日付を要素に持つdictを格納する

    Args:
        tgt_date (str): yyyymmdd

    Returns:
        dict:様々な日付を要素に持つdict
    """

    date_dict = {}

    date_dict['tgt_date'] = tgt_date
    date_dict['tgt_date_1w_past'] = get_different_date(tgt_date, -7)
    date_dict['today'] = dt.datetime.now().strftime('%Y%m%d')

    print('〈calculated date〉')
    print(f'\t{date_dict}')
    print()

    return date_dict


if __name__ == '__main__':

    main()





