# 0インデックスのn個の要素を持つ整数配列numsが与えられます。はじめにnums[0]に位置しています。

# i番目の要素の値は、i番目の要素からジャンプできる最大距離を表しています。

# つまり、もしnums[i]にいる場合は、あなたはnums[i+j]までジャンプすることができます。

# nums[n-1]までのジャンプの最小回数を返してください。

# テストケースはnums[n-1]までジャンプできるように用意されています。

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2

class Solution:
    def jump(self, nums: list[int]) -> int:
        # 現在位置からの最大ジャンプ距離
        distance = 0
        # ジャンプした回数
        jumps = 0
        # 探索可能な範囲（最大ジャンプ距離）
        end = 0

        for i in range(len(nums)-1):
            # i+nums[i]は右に進んでいることを表しているため、iが１番目なら１だし、２番目なら２
            distance = max(distance, i+nums[i])
            # もし現在位置から到達できる最大の距離（distance）がnumsの最終位置に到達できるなら
            if distance >= len(nums)-1:
                # ジャンプ回数を１追加して
                jumps += 1
                # 回数を返す。
                return jumps
            if i == end:
                jumps += 1
                end = distance
        return jumps

solution_instance = Solution()

result = solution_instance.jump(nums = [2,3,1,1,4])
print(result)