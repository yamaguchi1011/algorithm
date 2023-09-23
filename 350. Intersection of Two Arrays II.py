# 2つの整数配列 nums1 と nums2 が与えられたとき、それらの交点の配列を返す。
# 結果の各要素は、両方の配列に含まれる回数だけ出現しなければならず、どのような順序で結果を返してもよい。
from collections import Counter
# brutoforce
# class Solution:
#     def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         answer = []
#         # num1の各要素を一巡するまで繰り返す。
#         for i in nums1:
#             # i(nums1の各要素)がnums２にある場合
#             if i in nums2:
#                 # nums2からiを取り除く
#                 nums2.remove(i)
#                 # answerにiを追加
#                 answer.append(i)
#                 # answerを返す。
#         return answer

# Counterクラスcollectionsモジュールからインポートしている
# リスト内の各要素の出現回数を数える。
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
      #  Counterクラスで要素をキーとして、出現回数をカウントする。
      # Counter(nums1) は {1: 2, 2: 2}
      # Counter(nums2) は {2: 2}
      # &演算子で共通キーの{2}を取得する。(これをセット演算とよび、共通部分を取得するAND演算を行うことにより２を取得する。） 
      # .elements()メソッドは先ほど取得したキー{2}の要素を取得するために必要

        return list ((Counter(nums1) & Counter(nums2)).elements())
        


solution_instance = Solution()

result = solution_instance.intersect(nums1 = [1,2,2,1], nums2 = [2,2])
print(result)