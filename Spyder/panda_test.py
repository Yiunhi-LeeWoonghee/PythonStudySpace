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

execFileName = "panda_test.py" # 起動するpythonファイル指定
excelDir = "D:\\devStudy\\PythonStudySpace\\excel_test" #excelファイル格納先
resultDir = "D:\\devStudy\\PythonStudySpace\\excel_tes\\result" #結果物出力先
#multiexcelExtn = "\\*.xlsx"
excelExtn = "\\test1.xlsx" # 読込むexcelファイル

# excel全てのシートを読込む
ex_multi_sheet = pd.read_excel(excelDir + excelExtn, sheet_name=None, index_col=0)

# シート名出力テスト
for ex_sheet in ex_multi_sheet:
    print(ex_sheet)