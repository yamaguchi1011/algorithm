# 文字 '(', ')', '{', '}', '[', ']' を含む文字列 s が与えられたとき、その入力文字列が有効かどうかを判定する。
# 入力文字列が有効であるのは、以下の場合である：
# 開き括弧は、同じ種類の括弧で閉じなければならない。
# 開き括弧は正しい順序で閉じなければならない。
# どの閉じ括弧にも、対応する同じ型の開き括弧がある。
# 制約１: 1 <= s.length <= 104 
# 製薬２：sは括弧「()[]{}」のみで構成されます。
# クラスを定義
class Solution:
    def isValid(self, s: str) -> bool:
      # 開き括弧を一時的に保存するためのスタックを用意する
      stack = []
      # 閉じ括弧とそれに対応する開き括弧の対応を辞書で定義する
      mapping = {')':'(','}':'{',']':'['}
      # sから要素を一つずつ取り出しcharに代入する
      for char in s:
      # もしcharがmappiingのキーの中にあるなら（つまり閉じ括弧をキーとしているので閉じ括弧だった場合に言い換えられる）
          if char in mapping:
      # top_elementにstackの一番上の要素を取り出す。もしstackが空なら#を代入する。つまり、一番目でstackに値が入っていない時？
              top_element = stack.pop() if stack else '#'
      # もしmappingのcharをキーとした値がtop_elementと違う場合はfalseを返す。
              if mapping[char] != top_element:
                  return False
      # そうじゃない場合（文字が開きかっこである場合）
          else:
      # 開き括弧をスタックに追加する 
              stack.append(char)
      #  この処理まで辿り着いてstackが空という事は対応する括弧が全てあったと言うことになり、trueが返ってくる。
      return not stack

solution_instance = Solution()

# result = solution_instance.isValid(s = "()")
# result = solution_instance.isValid(s = "(]")
# result = solution_instance.isValid(s = "()[]{}")
# result = solution_instance.isValid(s = ")()")
result = solution_instance.isValid(s = "([])")
print(result)

# 基本的な性質は後入れ先だし。
# stackを使う場面は
# ・かっこの対応チェック
# ・関数呼び出しの履歴
# ・逆ポーランド記法の式評価
# ・ウェブの戻る機能
# ・バックトラッキングアルゴリズム