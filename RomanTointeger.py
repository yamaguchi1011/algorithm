# ローマ数字は7種類の記号で表される： I、V、X、L、C、D、M。
# 記号 値
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000
# 例えば、2はローマ数字でIIと書き、2つの1を足しただけである。12はXIIと書き、これは単にX＋IIである。27はXXVIIと書き、これはXX＋V＋IIである。
# ローマ数字は通常、左から右に大きいものから小さいものへと書く。しかし、4を表す数字はIIIIではない。代わりに4はIVと書く。1が5の前にあるので、それを引くと4となる。同じ原理が数字の9にも当てはまり、IXと書く。引き算が使われる例は6つある
# ・IをV(5)とX(10)の前に置くと4と9になる。
# ・XをL(50)とC(100)の前に置くと40と90になる。
# ・CをD(500)とM(1000)の前に置くと400と900になる。
# ローマ数字が与えられたら、それを整数に変換しなさい。

# 例1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# 例2
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
class Solution:
    def romanToInt(self, s: str) -> int:
        # ローマ数字の各文字に対応する数値を示す辞書を作る(roman_values) 
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        # ローマ数字に変換するための合計値を格納する変数を定義する。(total)
        total = 0
        # 一つ前の文字の数値を保持する変数を定義する。(prev_value)
        prev_value = 0
        # 文字列sの各文字に対して処理を行う(for c in s:)
        for c in s:
        # roman_valuesの中に与えられた文字が存在すれば文字に対応する値をvalueに代入する。与えられた文字列がローマ数字の記号かどうかを確認する
            if c in roman_values:
                value = roman_values[c]
        # totalにvalueを加算していく。ローマ数字を整数に変換するため
                total += value
        # もしも現在の値（value）が前の値（prev_value）よりも大きければ合計値（total）から前の値（prev_value）を２倍した値を引く
                if value > prev_value:
                    total -= prev_value * 2
        # 前の値（prev_value）に現在の値を代入して、前の値を更新する。
                prev_value = value
        # 文字列sの各文字に対して処理が終わったらreturnで合計値を返す（total）
        return total

solution_instance = Solution()
# result = solution_instance.romanToInt(s="III")
# result = solution_instance.romanToInt(s="LVIII")
result = solution_instance.romanToInt(s="MCMXCIV")
print(result)

