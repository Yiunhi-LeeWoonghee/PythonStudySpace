# osライブラリ
from os import path
# 正規表現の標準ライブラリ
import re

# 同じディレクトリのtxtファイルを開く
file_path = path.join(path.dirname(__file__), 'Table_list.txt')

# 変数の宣言のみ
line = [] # 行のリスト
s_list = [] # 区切りした文字列のリスト
table_list = [] # テーブル名リスト
rCount_list = [] # データ件数リスト

with open(file_path, 'r') as f:
    # テキストファイルを読み込む
    line = f.read().splitlines()
for reg_str in line:
    s_list = re.split('\t', reg_str)
    # 注意：appendの戻り値はNoneのため、変数で受け取れない（自動でリストに追加される）
    table_list.append(s_list[0]) # テーブル名
    rCount_list.append(s_list[1]) # テーブルのデータ件数

