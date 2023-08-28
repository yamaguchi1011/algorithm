# 整数配列numsが与えられます。配列内で2回登場する要素があればTrueを返してください。全ての要素が異なる場合はFalseを返して下さい。

# 全探索だとたくさんの要素を渡された時にかなりの時間がかかる
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         # 最初をの値jを定義して、違ったら１づつ進める
#         # j番目の値とi番目の値を比べて同じならtrueを返して終了。
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                   return True
#         return False
￥
# set関数使って、重複のない集合を作成し、その集合の要素数と、元のリストの要素数を比べて、同じであればTrueを返す。

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # _にsetで重複を排除して状態で格納
        _ = set(nums)
        # _とnumsの要素数が異なる場合はTrueを返す
        if len(_) != len(nums):
            return True
        else:
            return False




solution_instance = Solution()

# テスト用のリストと目標値を指定して twoSum メソッドを呼び出す
# result =  solution_instance.containsDuplicate(nums = [1,2,3,1])
# result =  solution_instance.containsDuplicate(nums = [1,2,3,4])
result =  solution_instance.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])
print(result)

# setは順序のない一意の要素を格納するためのデータ構造、集合（集合内に同じ要素はなく、要素の順序は保持されない）
# _が一時的な値を無視するために使用される慣習的な変数名