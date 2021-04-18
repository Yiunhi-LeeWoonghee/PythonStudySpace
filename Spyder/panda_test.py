
"""
PandasでExcelファイルを閲覧・編集する
"""

import sys
# ライブラリ格納先を明視
sys.path.append('c:\\users\\thele\\appdata\\local\\programs\\python\\python37\\lib\\site-packages')
import pandas as pd # Excelライブラリ
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
parser.add_argument('-m', '-multi')
parser.add_argument('input_excel_dir', help='読込むexcelファイルの格納先（相対パス）')
parser.add_argument('input_text_dir', help='読込むテキストファイルの格納先（相対パス）')
parser.add_argument('output_result_dir', help='結果物の出力先（相対パス）')
args = parser.parse_args()

input_excel_dir = args.input_excel_dir
input_text_dir = args.input_text_dir
output_result_dir = args.output_result_dir

# テキストファイル読込みするためのリスト
f_lines = [] # 行のリスト
s_list = [] # 区切りした文字列のリスト
table_list = [] # テーブル名リスト
rCount_list = [] # データ件数リスト

# テキストファイル読込み
f = open(input_text_dir, 'r')
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
df = pd.read_excel(
    io=input_excel_dir, # excel格納先
    sheet_name='テーブル一覧', # シート名指定
    header=0,
    index_col=col_index_list
    )
print(df)
# excelで必要な列だけ読込むための設定
"""
DataFrameで特定の列を取得する

DataFrame(
    data=None, # データオブジェクト
    index: Optional[Axes]=None, # 行
    columns: Optional[Axes]=None, # 列
    header: header=None, # ヘッダーの行（Noneはヘッダーなし）
    dtype: Optional[Dtype]=None, # データ型
    copy: bool=False) # オブジェクトコピー生成の可否

列のindex
1,3,5,6,7,8,9
1 : テーブル名
2 : カラム名
5 : データ型
6 : バイト数
7 : NULL可否
8 : 制約名
9 : 小数点（精度）
"""
"""
col_index_list = [1,3,5,6,7,8,9]

pd.DataFrame(
    data=input_excel_dir,
    columns=col_index_list,
    header=0
    )
"""