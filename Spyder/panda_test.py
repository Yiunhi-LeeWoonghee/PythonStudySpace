# PandasでExcelファイルを閲覧・編集する

from os import path
import os
import datetime as dt
# Excelライブラリ
import pandas as pd
#import openpyxl
import sys
# ライブラリ格納先を明視
sys.path.append('c:\\users\\thele\\appdata\\local\\programs\\python\\python37\\lib\\site-packages')
# import glob # 複数ファイル処理ライブラリ
import argparse # コマンドライン解析モジュール
#import pathlib # パス関連モジュール
import re # 正規表現の標準ライブラリ

execFileName = "panda_test.py" # 起動するpythonファイル指定

"""
# 内部でパスを決める場合
excelDir = "D:\\devStudy\\PythonStudySpace\\excel_test" #excelファイル格納先
resultDir = "D:\\devStudy\\PythonStudySpace\\excel_tes\\result" #結果物出力先
#multiexcelExtn = "\\*.xlsx"
excelExtn = "\\test1.xlsx" # 読込むexcelファイル

# excel全てのシートを読込む

ex_multi_sheet = pd.read_excel(excelDir + excelExtn, sheet_name=None, index_col=0)


# シート名出力テスト
for ex_sheet in ex_multi_sheet:
    print(ex_sheet)
"""

"""
# コマンドラインで引数を受け取る場合
コマンド : python -m ..\excel_test\test1.xlsx ..\excel_test\spyder_input_text.txt ..\excel_test\spyder_result

$1 : モジュール実行オプション（複数のパラメータ）
$2 : 読込むexcelファイルの格納先（相対パス）
$3 : 読込むテキストファイルの格納先（相対パス）
$4 : 結果物の出力先（相対パス）
"""
parser = argparse.ArgumentParser(description=('コマンドで引数受けった上、excel読込み及びファイル出力処理を行う'))
#parser.add_argument('python', 'py')
#parser.add_argument('-m', '-multi')
parser.add_argument('input_excel_dir', help='読込むexcelファイルの格納先（相対パス）')
parser.add_argument('input_text_dir', help='読込むテキストファイルの格納先（相対パス）')
parser.add_argument('output_result_dir', help='結果物の出力先（相対パス）')
args = parser.parse_args()

input_excel_dir = args.input_excel_dir
input_text_dir = args.input_text_dir
output_result_dir = args.output_result_dir

# 結果物フォルダ生成 (日時付き)
dt_now = dt.datetime.now()

# 出力先フォルダ名指定
output_mk_dir = output_result_dir + '\output_' + dt_now.strftime('%Y%m%d%H%M%S')
output_ctl = output_mk_dir + '\ctl' # 制御ファイル格納先
output_csv = output_mk_dir + '\csv' # csvファイル格納先
output_err = output_mk_dir + '\err' # エラーログファイル格納先

# テキストファイル読込みするためのリスト
f_lines = [] # 行のリスト
s_list = [] # 区切りした文字列のリスト
table_list = [] # テーブル名リスト
rCount_list = [] # データ件数リスト


# 結果出力フォルダ生成
os.mkdir(output_mk_dir)
# 制御ファイル格納先生成
os.mkdir(output_ctl)
# csvファイル格納先生成
os.mkdir(output_csv)
# エラーログファイル格納先生成
os.mkdir(output_err)

# テキストファイル読込み
f = open(file=input_text_dir, mode='r')
f_lines = f.read(-1).splitlines()
for f_line in f_lines:
    s_list = re.split('\t', f_line)
    #テーブル名取得
    table_list.append(s_list[0])
    #レコード件数取得
    rCount_list.append(s_list[1])
f.close()

# excelで読込む列のindex
col_index_list = [1,3,5,6,7,8,9]

# excel読込み
"""
DataFrameで特定の列のみ取得する

DataFrame(
    data=None, # データオブジェクト
    index: Optional[Axes]=None, # 行
    columns: Optional[Axes]=None, # 列
    header: header=None, # ヘッダーの行（Noneはヘッダーなし）
    dtype: Optional[Dtype]=None, # データ型
    copy: bool=False) # オブジェクトコピー生成の可否

列のindex
1,3,5,6,8,9
1 : テーブル名
3 : カラム名
5 : データ型
6 : バイト数
8 : 制約名
9 : 小数点（精度）
"""
df = pd.read_excel(
    io=input_excel_dir, # excel格納先
    sheet_name='テーブル一覧', # シート名指定
    header=0,
    usecols=(1,3,5,6,8,9)
    )

"""
取得したexcelの物理テーブル名とテキストファイルのテーブル名を比較する
一致した場合、カラム情報を取得して制御ファイル及びcsvファイルを生成する
"""

table_col_list = [] # カラムリスト
ctl_common_list = ['LOAD DATA\n', 'INFILE ~\n']
table_index_list = 0 # テキスト取得のテーブル名インデックス
def_len = len(df) # 読込んだexcelの行数
table_duplicated_count = 0 # excel内でテーブルごとに名前が一緒の数
total_duplicated_count = 0 # excel内でテーブル名列のインデックス

# excelのカラム名を取る
for i in range(0, def_len):
    # excelのテーブル名とテキストのテーブル名が一致
    if df.iloc[i, 0] == table_list[table_index_list]:
        # テーブル名が重複されている数を求める
        for df_d_c in range(0, def_len):
            if df.iloc[df_d_c, 0] != table_list[table_index_list]:
                break
            # 重複されているテーブル数ほどカウントする
            if df.iloc[df_d_c, 0] == table_list[table_index_list]:
                table_duplicated_count += 1
                total_duplicated_count += 1
        # excelでテーブル名が重複されている数までカラム名を取得
        for k in range(0, total_duplicated_count + table_duplicated_count):
            table_col_list.append(df.iloc[k, 1])
        # 制御ファイル存在チェック
        if not os.path.isfile(output_ctl + '\\' + table_list[table_index_list] + '.ctl'):
            # 制御ファイル書き込み
            ctl_f = open(output_ctl + '\\' + table_list[table_index_list] + '.ctl', 'w')
            # 共通設定リスト書き込み
            ctl_f.writelines(ctl_common_list)
            ctl_f.write('INSERT INTO ' + table_list[table_index_list] + '\n')
            ctl_f.write('(\n')
            for j in range(0, len(table_col_list)):
                # 最後のカラムの場合、カンマを付けない
                if j == len(table_col_list)-1:
                    # データ型がDATEの場合、テキスト追加
                    if df.iloc[j, 2] == 'DATE':
                        ctl_f.write(df.iloc[j, 1] + ' DATE ' + 
                                    'to_char(to_date(:' + df.iloc[j, 1] + '\'YYYY/MM/DD\'))\n')
                    ctl_f.write(')')
                # 最後のカラムじゃない場合
                else:
                    # データ型がDATEの場合、テキスト追加
                    if df.iloc[j, 2] == 'DATE':
                        ctl_f.write(df.iloc[j, 1] + ' DATE ' + 
                                    'to_char(to_date(:' + df.iloc[j, 1] + ',\'YYYY/MM/DD\')),\n')
                    # データ型がDATE以外の場合
                    else:
                        ctl_f.write(df.iloc[j, 1] + ',' + '\n')
            ctl_f.close()
        # 初期化
        table_duplicated_count = 0
        table_col_list = []
        table_index_list = 0
    # excelのテーブル名とテキストのテーブル名が一致しないとスキップ
    else:
        # 初期化
        table_duplicated_count = 0
        table_col_list = []
        # テキストファイルの次のテーブル
        table_index_list += 1