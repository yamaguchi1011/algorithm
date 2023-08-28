# 2 つの文字列 s と t を指定すると、
# t が s のアナグラムである場合は true を返し、そうでない場合は false を返します。 
# アナグラムは、通常は元の文字をすべて 1 回だけ使用して、別の単語またはフレーズの文字を再配置することによって形成された
# 単語またはフレーズです。

# ソートで処理する場合
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         sorted_s = sorted(s)
#         sorted_t = sorted(t)
#         if sorted_s == sorted_t:
#             return True
#         return False

# ハッシュテーブルを使う場合、こちらが3つの中では最適解
# leetcode内では下記のimportは必要なし
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # pythonの標準ライブラリで提供されているcollectionモジュールのdefaultdictクラスを使う
        # デフォルト値を持つ辞書を作成する。通常のdictとは違い、
        # デフォルト値を持つ（int引数はデフォルト値は0）ので存在しないキーが出てきた時に（dictはKeyErrorが出る。キーがないよーって）
        # そのキーに対する値が自動的にint()によって初期化され辞書に追加される
        count = defaultdict(int)

        for x in s:
            count[x] += 1
        for x in t:
            count[x] -= 1
        for val in count.values():
            if val != 0:
                return False
        return True
    
# ０から２５の数字をキーに持つ配列を使う方法。unicodeポイントを使用(old()関数を使う)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # 0から２５までの配列を作成する
#         count = [0] * 26
#         # ordは Unicodeポイントを返す。
#         for x in s:
#             # count[ord(x) - ord('a')]で最初に作った配列のキーを示して、1を追加する。
#             # その文字出るたびに１プラスされていくので、何回出てきたかをカウントしている。
#             # （もう一個の文字列で同じことをやるが、文字が出てくるたびにマイナスになるので、最終的に配列（count）の値（val）が全て０の場合にアナグラムだと判断する）
#             count[ord(x) - ord('a')] += 1
#         for x in t:
#             count[ord(x) - ord('a')] -= 1
        
#         # ０以外の値を持つかどうかを調べる。持っていたら、アナグラムではないのでFalseを返す。
#         for val in count:
#             if val != 0:
#                 return False
        
#         return True
    
solution_instance = Solution()
# result = solution_instance.isAnagram(s = "anagram", t = "nagaram")
result = solution_instance.isAnagram(s = "rat", t = "car")
print(result)

#  Unicodeポイント
# old()関数を使うと与えられた文字のUnicodeポイントを整数値として返すための
# Pythonの組み込み関数です。
# 関数名 "ord" は "ordinal" の略で、文字を数値的な位置や順序として扱うためのものです。
# Pythonのord()関数を使用すると、文字や記号などのテキストデータを内部的には数値として扱えるため、
# テキスト処理や文字列の比較などの操作が簡単に行えるようになります。
# また、文字の順序や位置を判定したり、テキストの操作を行ったりする際にも役立ちます。


# count = defaultdict(int) 
# は、Pythonの標準ライブラリで提供されている collections モジュールの defaultdict クラスを使用して、デフォルト値を持つ辞書を作成する操作です。int という引数は、デフォルト値として整数 0 を指定しています。
# 以下で詳しく説明します。
# defaultdict クラスは通常の辞書と似ていますが、キーが存在しない場合にもデフォルト値を返すことができます。これは特に、カウンターやグルーピングなどの操作を行う際に便利です。
# int は Python の組み込み型の一つで、整数を表します。defaultdict(int) を作成することで、新しいキーが辞書に追加されると、そのキーに対する値として自動的に int() を呼び出して初期化されます。int() は整数型のデフォルト値である 0 を返すため、この場合は新しいキーの初期値として 0 が設定されます。
# 例えば、以下のコードを考えてみましょう。


# .valuesで値を全て取ってこれる