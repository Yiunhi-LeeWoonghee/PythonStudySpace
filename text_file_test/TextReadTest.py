# osライブラリ
from os import path

# 同じディレクトリのtxtファイルを開く
file_path = path.join(path.dirname(__file__), 'Table_list.txt')
with open(file_path, 'r') as f:
    # テキストファイルを読み込む
    s = f.read().splitlines()
    print(s)
