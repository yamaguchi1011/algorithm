# 入力文字列sが与えられたとき、単語の順序を逆にする。

# 単語はスペース以外の文字の並びとして定義される。sの単語は少なくとも1つのスペースで区切られる。

# 逆順の単語を1つのスペースで連結した文字列を返す。

# sには、先頭や末尾に空白が含まれていたり、2つの単語の間に複数の空白が含まれていたりする可能性があることに注意。返される文字列は、単語を1つのスペースで区切ったものでなければならない。余分なスペースを含めないでください。

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


# 解答１
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         # 戻り値用のリストを用意
#         reversed_words = []
#         # １単語を保持する
#         word = ""
#         for i in range(len(s)):
#             # sが空白なら（空白が続いている場合は、wordに値が入っていないので、falseになる。）
#             if word and s[i]==" ":
#                 # 戻り値用のリストにwordを追加する
#                 reversed_words.append(word)
#                 # wordを空白に戻して次の単語を保持する準備をする。
#                 word=""
#                 # 空白以外の時
#             elif s[i]!=" ":
#                 word += s[i]
#                 # 走査終了後、wordに文字があれば戻り値用のリストに追加
#         if word:reversed_words.append(word)
#         # リストを逆順にして空白区切りの文字列で返す。
#         return " ".join(reversed_words[::-1])
    
# 解答２（短い書き方）
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
    

    
solution_instance = Solution()

# result = solution_instance.(s = "the sky is blue")
# result = solution_instance.reverseWords( "  hello world  ")
result = solution_instance.reverseWords("a good   example")
print(result)
