# m x nの整数配列accounts が与えられます。
# accounts[i][j]は、i番目の顧客がj番目の銀行に持っているお金の量です。一番裕福な顧客が持つ総額を返してください。
# 富の総額は、彼らが持っているすべての銀行口座のお金の量です。

# Example 1:

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

# class Solution:
#     def maximumWealth(self, accounts: list[list[int]]) -> int:
#         # 富の最大値を保持する変数
#         richest_customer_wealth = 0
#         # accountsを一巡して走査
#         for i in range(len(accounts)):
#             # 各要素の合計値と、現在の富の最大値を比較して大きい方を記録
#             richest_customer_wealth = max(richest_customer_wealth,sum(accounts[i]))
#             # 富の最大値を返す。
#         return richest_customer_wealth
    

# 1-liner
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(acc) for acc in accounts])
        

solution_instance = Solution()

result = solution_instance.maximumWealth(accounts = [[1,2,3],[3,2,1]])
# result = solution_instance.maximumWealth(accounts = [[1,5],[7,3],[3,5]])
print(result)

# 質問
# pythonで下記はどういう意味？
# accounts[i][j]

# ChatGPT
# accounts[i][j] は、Pythonのリスト（または配列）内の要素にアクセスするための構文です。この構文は2つのインデックス i と j を使用して、2次元のリストや多次元のリスト内の特定の要素にアクセスします。

# i は外側のリスト（または行）のインデックスを指定します。
# j は内側のリスト（または列）のインデックスを指定します。
# 具体的な例を示します。以下は2次元リスト accounts の要素にアクセスする例です。

# python
# Copy code
# accounts = [
#     [1000, 2000, 3000],
#     [1500, 2500, 3500],
#     [1200, 2200, 3200]
# ]

# # accounts[1][2] は 2500 を取得します。
# value = accounts[1][2]

# # accounts[0][0] は 1000 を取得します。
# another_value = accounts[0][0]
# このように、accounts[i][j] は i 番目の行にある j 番目の列の要素にアクセスするために使用されます。この構文は2次元リストだけでなく、3次元リストやそれ以上の多次元リストでも同様に動作します。


# 質問
# ２Dリストや３Dリストを総括すると、リストの入れ子構造のことという認識で間違いない？
# ChatGPT
# はい、あなたの認識は正しいです。2Dリストから3Dリストへと、リストの入れ子構造が次元を表現する方法として使用されています。入れ子リストは、要素がリストであるリストを意味し、これによりデータを多次元の構造で表現できます。

# 2Dリスト（2次元リスト）は、リストを要素とするリストです。これは行列（行と列の組み合わせ）を表現するのに使われます。
# python
# Copy code
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# 3Dリスト（3次元リスト）は、リストを要素とするリストを要素とするリストです。これにより、3つの次元を持つデータ構造を表現できます。
# python
# Copy code
# cube = [
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12],
#     ],
#     [
#         [13, 14, 15],
#         [16, 17, 18],
#     ]
# ]
# このように、リストを入れ子にすることで、データの多次元性を表現できます。それぞれの入れ子レベルが新しい次元を表し、データをより複雑な構造で表現できるようになります。