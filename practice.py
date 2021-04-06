#### シャープ数によるコメントの意味
### 3つ：チャプター（章）
## 2つ：関数やメソッドなどの解説
# 1つ：コード

### 2021/04/04
### 出力
# print('chouchou')
# print("バクシン" * 5)

## True / False
# print(5>10)
# print(5<10)
# print(not True)
# print(not (5>10))

### 変数
# animal = "犬"
# name = "ポンター"
# age = 4
# hobby = "散歩"
# is_adult = age >= 3

# print('うちの' + animal + 'の名前は' + name + 'です')
## 数字と文字列は自動で変換されて繋がらないので、str()を使って文字列型に変換する
# print(name + 'は' + str(age) + '歳で、' + hobby + 'が大好きです')
# # カンマで繋がると、数字やブーリアンもstrを使わずに文字列に繋げる
# print(name, 'は大人ですか？', is_adult)

'''2行以上の
コメント
処理
'''

## 一括コメント化のショートカット
# Ctrl + /
# a
# b
# c

## 計算式
# print(5//3) # 1、商（しょう）
# print(5%3) # 2、余り（あまり）

### 色んな数式
# print(pow(4, 2)) # 4^2 = 4*4 = 16 
# print(sqrt(16)) # 16のルートのため、4
# print(max(5, 12)) # 12
# print(min(5, 12)) # 5

### ランダム
# from random import *
# print(int(random() * 10) + 1) # 1～10以下の任意の値を生成
# print(randint(1, 10)) # 1～10以下の任意の値を生成

### 文字列
# sentence = """
# 2行まで書いてみる
# もう2行だよ
# """
# print(sentence)

### 文字の区切り
# zipCode = "000-999"
# print(zipCode[0:3]) # 000

### 文字列の関数
# py = "py is good"
# print(len(py)) # 文字列の長さ
# print(py.replace("py", "ramen")) # "ramen is good"

### 文字列のフォーマット（他の方法）
#print("私は {age}歳です。{color}色が好きです。".format(age = 20, color = "赤い"))
# 他の方法2（v3.6以上）
# age = 20
# color = "赤い"
# print(f"私は {age}歳です。{color}色が好きです。")

### 2021/04/05
### エスケープ文字
# \n：改行
# 「私は"a"です」を出力
# 方法1：print('私は"a"です')
# print("私は\"a\"です")
# \"又は\'：文字列内でダブルコーテーション
# \\：文字列内で\（バックスラッシュ）
# \r：カーソルを前に移動

### リスト
## 宣言方法
# numlist = [10, 20, 30]
# print(numlist) -> Pythonはリストのまま出力する [10, 20, 30]
## インデックス
# strlist = ["a", "b", "c"]
# print(strlist.index("b")) -> 戻り値は1
## リスト追加
# strlist.append("d") -> 最後に追加
## リスト挿入
# strlist.insert(1, "e") -> "a"と"b"の間に"e"が入る
## リストを後ろから削除
# strlist.pop()
## 同じ値があるかチェック
# strlist.append("a")
# strlist.count() -> 2
## リストの整列
# numlist2 = [5, 4, 2, 3, 1]
# numlist2.sort() -> [1, 2, 3, 4, 5]
## リストを反転させる
# numlist2.reverse() -> [5, 4, 3, 2, 1]
## リストを全部消す
# numlist2.clear() -> []
## Pythonのリストはデータ型に関係せず挿入できる
# mixlist = ["a", 1, false]
## リストを拡張する
# newlist = [3, 4]
# mixlist.extend(newlist) -> ["a", 1, false, 3, 4]

### 辞書型（ディクショナリー型）
## キーは中腹ができない
## 宣言は、dict = {key:value, key2:value2...}
## keyのデータ型は、数字型、文字型、
# print(dict[key2]) -> value2
# print(dict.get(key2)) -> 上の結果と一致
# print(dict.get(key9, "NULL")) -> key9のvalueがないと"NULL"を出力
# print(key in dict) -> true
# print(key9 in dict) -> false
## 辞書型にデータを追加
# dict["key3"] = "value3"
## 同じキーに他の値を代入すると、値が変わる
# dict[key1] = "new value"
## 辞書型のデータ削除
# del dict["key3"]
## キーのみ出力
# dict.keys()
## バリューのみ出力
# dict.values()
## キーとバリューを出力
# dict.items()

### tuple（タプル）
## 内容の変更や追加は不可能だが、検索がリストより速い
# menu = ("かつ丼", "牛丼")
# print(menu[0]) -> かつ丼
## エラー
# menu.add("うどん") ⇒ AttributeError: tuple object has no attribute 'add'
## タプルのメリット
# (a, b, c) = (1, 2, 3) -> 一括生成が可能

### set型（集合型）
## 中腹不可能、順序なし
## ※注意：出力順は保証されない
# exset = {1,4,5,5,5} -> {1,4,5}出力
# exset2 = set([1,2,3]) -> これもOK、リストをset化する
## 積集合（共通集合）
# print(exset & exset2)
# print(exset.intersection(exset2))
## 和集合（合併集合）
# print(exset | exset2)
# print(exset.union(exset2))
## 差集合
# print(exset - exset2)
# print(exset.difference(exset2))
## 追加
# exset.add(6)
## 削除
# exset.remove(6)

### オブジェクトの型変換
## 変換は自由に可能（リスト⇔辞書型⇔タプル⇔リスト）
# drinks = {"コーヒー","牛乳","ジュース"}
# print(drinks, type(drinks)) -> {"コーヒー","牛乳","ジュース"} <class 'set'>
# drinks = list(drinks)
# drinks(drinks, type(drinks)) -> ["コーヒー","牛乳","ジュース"] <class 'list'>
# drinks = tuple(drinks)
# drinks(drinks, type(drinks)) -> ("コーヒー","牛乳","ジュース") <class 'tuple'>

### 2021/04/06
### if
## Pythonのifの基本構造
## if 論理式: -> elif 論理式2: -> else:
## if A又はB -> if "A" or "B"
# temp = int(input("気温を入力"))
# if 30 <= temp:
#   print("hot")
# elif 10 <= temp and temp < 30:
#   print("OK")
# elif 0 <= temp < 10:  -> これも可能
#   print("wear a coat")
# else:
#   print("cold")

## ユーザの値入力を待つ関数
# input()

### for文
## 基本構成
## for sth in [list]
# for num in [0,1,2,3]
#   print("result : {0}".format(num))
## range(n, m) -> nからm-1まで順番的に生成
# for num in range(3) -> 0,1,2,3

### whileは省略

### 関数
## 基本構成
# def 関数名():
## パラメータと戻り値付きの関数
# def 関数名2(a, b):
#   <ロジック>
#   return 戻り値
## デフォルト値の設定
# def examFunc(a=1, b="2"):
## キーワード引数
# def examFunc2(a, b):
# examFunc2(a=1, b="2")
## 可変長引数
# def exFunc3(a, b, *c):
#   for cc in c:
#       print(cc, end=" ") -> end
# exFunc3("a","b","c","d")