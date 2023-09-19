# 整数の配列 citations が与えられます。
# citations[i] は、i 番目の論文に対して研究者が受け取った引用回数です。
# 研究者の h 指数を返してください。

# Wikipedia の h 指数の定義によれば、h 指数は、与えられた研究者が少なくとも h 回引用された h 個の論文を出版している最大の h の値です。

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h = i+1
        
        return h
solution_instance = Solution()

result = solution_instance.hIndex(citations = [5,4,3,2,1])
print(result)

# ・5>1 →h=1
# ・4>2 →h=2
# ・3=3 →h=3
# ・2<4 →h=3
# ・1<5 →h=3