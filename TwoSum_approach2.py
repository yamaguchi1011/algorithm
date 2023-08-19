class Solution:
    def twoSum(self, nums:list[int],target:int)->list[int]:
      # 空のハッシュマップを作成する。要素をキーとして、その要素のインデックスを保存する。
        hashmap = {}
      #rangeで要素数分シーケンス（pythonにおいて順番に並んだ要素の集合）を作成し格納してループさせる
        for i in range(len(nums)):
      #各要素（num[i]）をキーとして、対応するインデックスiを値として、hashmapに格納する。もう一度言うぞ、要素をキーとして、インデックスを値として格納する。
            hashmap[nums[i]] = i
      #もう一度ループ
        for i in range(len(nums)):
      # numsのループする中で、numsの中にtargetからi番目のnumsを引いた数字（complement（補数））と等しい値があるかどうかを後のコードで見るので、complementを定義する
            complement = target - nums[i]
      # もしcomplementがhashmap内に存在し、かつcomplementのインデックスが現在のインデックスiと異なる場合は、returnでその条件を満たすインデックスを返す。
            if complement in hashmap and hashmap[complement]!=i:
                return[i,hashmap[complement]]
    # テスト用のリストと目標値を指定して twoSum メソッドを呼び出す

# 下記ターミナル実行用
solution_instance = Solution()

# テスト用のリストと目標値を指定して twoSum メソッドを呼び出す
result = solution_instance.twoSum([2, 7, 11, 15], 9)
# result = solution_instance.twoSum([3,2,4], 6)
# result = solution_instance.twoSum([3,3], 6)
print(result)