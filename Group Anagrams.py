# 文字列strsの配列が与えられたら、アナグラムをグループ化しなさい。答えは任意の順番で返すことができます。
# アナグラムとは、別の単語やフレーズの文字を並べ替えてできた単語やフレーズのことで、通常は元の文字をすべて正確に一度だけ使います
# leetcode内では下記のimportは必要なし
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # defaultdict(list)でキーと値のマッピングを保持する辞書（anagram_map）を作成する。ここでのキーは各ワードをソートした文字列で、値はソートする前の文字列。最終的に値のみを取ってくればそれが解答になる。
        anagram_map = defaultdict(list)
        for word in strs:
            # sorted_wordに文字列（word）をソートして、''で空文字列なしで連結したものを代入する。
            sorted_word = ''.join(sorted(word))
            # anagram_mapの中のsorted_wordをキーとして、ソートする前のワードを値として入れる（append（word)）。
            anagram_map[sorted_word].append(word)
            # valuesでそれぞれのキー（ソートされた文字列）に対応する、値（ソートしていない文字列）を返す。
            # 今回の場合はどちらの方法でreturnしても良い。list()でラップすることで()内で指定した内容を実際のリストとして取得できる。
        # return anagram_map.values()
        return list(anagram_map.values())
    
solution_instance = Solution()
result = solution_instance.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
print(result)



# list() を使用する主な理由は、特定の操作や処理をリストとして行いたい場合に、ビューオブジェクトをリストに変換するためです。ビューオブジェクト自体は反復処理ができますが、リストとしてのメソッドや操作を使用するためには、ビューオブジェクトをリストに変換する必要があります。
# 例えば、次のような場合に list() を使用します：
# anagram_map.values() を直接リストのようにスライスしたり、インデックスを使用したりする場合。
# anagram_map.values() の中身をソートしたい場合。
# anagram_map.values() の中身を他のリストと結合したり、集合演算を行いたい場合。
# リストのメソッドや操作を利用する必要がある場合には、
# list(anagram_map.values()) のようにビューオブジェクトをリストに変換してから処理を行うことで、
# 操作が簡単に行えるようになります。