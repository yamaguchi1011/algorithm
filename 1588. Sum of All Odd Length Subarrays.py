# 正整数の配列 arr が与えられたとき、 arr の奇数番目の部分配列の和を返す。
# (0から始まって配列の最後の番号までで、奇数の部分配列の合計を調べる。)

# 部分配列とは、配列の連続した部分配列のことである。
# Example 1:

# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        answer = 0
        # 各要素を一巡して走査する
        for i in range(len(arr)):
            #1要素,3要素,5要素のように1個飛ばしで要素数を増やしながら奇数個の部分配列を作る。
            #arrの要素が偶数の場合でも、その1つ前の奇数個までの部分配列を取れれば良い。
            for j in range(i,len(arr),2):
                # answerに奇数個の部分配列を追加
                answer += sum(arr[i:j+1])
        return answer
    
solution_instance = Solution()


result = solution_instance.sumOddLengthSubarrays(arr = [1,4,2,5,3])

print(result)