# 文字列の配列から最長の共通接頭辞文字列を見つける関数を書く。

# 共通の接頭辞がない場合は、空の文字列 "" を返す。

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # srtsの各用紙の文字数が小さい順から並べ替える。sortedは新しいリストを作る非破壊的処理。sortは元のリスト自体を書き換える破壊的処理
        strs = sorted(strs, key=len)
        # strsの全要素で共通する文字を格納する変数resを用意(res = []だと各文字がバラバラに代入されるから今回の回答に合わなくなる)
        res = ""
        # strsの一つ目の要素について１文字目から順に全ての文字をfor文で処理する。(一つ目の要素の文字数分繰り返す)
        for i in range(len(strs[0])):
        # strsの要素全てに対してfor文で処理する。
            for s in strs:
        # iが一つ目の要素の文字数と一致した場合(strsの中で文字数の一番少ない要素の文字数と、対象の要素の文字数)、もしくはs[i]と一つ目の要素のi番目の文字と不一致の場合
                if i == len(s) or s[i] != strs[0][i]:
        # resを返す
                    return res
        # そうでない場合は（一つ目の要素のi番目の文字が全ての要素のi番目の文字と一致した場合はその文字をresに加える）
            res += strs[0][i]
        # 全ての文字が一致した場合はresを返す。
        return res

# 下記ターミナル実行用

solution_instance = Solution()

# テスト用のリストと目標値を指定して twoSum メソッドを呼び出す
result =  solution_instance.longestCommonPrefix(strs = ["flower","flow","flight"])

print(result)