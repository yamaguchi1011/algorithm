# 整数配列 nums が与えられたとき、0 以外の要素の相対順序を維持したまま、すべての 0 を配列の末尾に移動する。

# これは、配列のコピーを作成せずにインプレースで行わなければならないことに注意。
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        move_count = 0
        for i in range(len(nums)):
            # もし０だと、削除して、numsの末尾に追加する。そして、move_countを＋１する。
            # なぜ＋１するのかは、0を取り除くと、配列の並びが変わり、０が連続して配列に存在していた場合、逃してしまう場合があるから。
            if nums[i-move_count] == 0:
                nums.append(nums.pop(i-move_count))
                move_count += 1
solution_instance = Solution()

result = solution_instance.moveZeroes(nums = [0,1,0,3,12])
print(result)