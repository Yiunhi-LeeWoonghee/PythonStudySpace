# openpyxlライブラリが必要
# ターミナルにて pip install openpyxl 実行

# no moduleエラー解消（openpyxlライブラリ格納先を明視）
import sys
sys.path.append('c:\\users\\thele\\appdata\\local\\programs\\python\\python37\\lib\\site-packages')

# pythonとexcelの連携ライブラリインポート
import openpyxl
# 複数ファイルを処理するため、globライブラリをインポート
import glob

# ディレクトリ指定
files = glob.glob('.\\excel_test\\*.xlsx')

# フルパス指定
# workbook = openpyxl.load_workbook('D:\\devStudy\\PythonStudySpace\\excel_test\\*.xlsx')
# print(workbook)
