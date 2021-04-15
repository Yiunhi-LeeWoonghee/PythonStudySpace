
"""
PandasでExcelファイルを閲覧・編集する
"""

# ライブラリ格納先を明視
import sys
sys.path.append('c:\\users\\thele\\appdata\\local\\programs\\python\\python37\\lib\\site-packages')
# Excelライブラリ
import pandas as pd
# 複数ファイル処理ライブラリ
# import glob
# コマンドライン解析モジュール
import argparse

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
コマンド : python -m ..excel_test\test1.xlsx ..excel_test\spyder_input_text.txt ..excel_test\spyder_result

$1 : 読込むexcelファイルの格納先（相対パス）
$2 : 読込むテキストファイルの格納先（相対パス）
$3 : 結果物の出力先（相対パス）

その他
-m : モジュール実行オプション
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

