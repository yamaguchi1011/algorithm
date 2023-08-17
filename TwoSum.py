# 整数の nums と整数の target の配列が与えられたとき、それらが target に加算されるような2つの数値の添字を返す。
# 各入力は正確に1つの解を持つと仮定してよく、同じ要素を2度使ってはならない。
# 答えを返す順番は自由で


# 　クラスを定義
class Solution:
    # twosumメソッドを定義、selfはpythonのクラスメソッド、最初のパラメータは常にselfになる.最後のlist[int]で戻り値のヒントを示している。（今回は整数型のリスト）
    def twoSum(self,nums:list[int],target:int) -> list[int]:
# len関数は引数の要素数を返す。range関数は渡された要素数の範囲内の整数のシーケンスを生成する。５を渡されたら（０,5）を生成する。（0,1,2,3,4）を生成するので順にiに代入されて繰り返し処理がされる
        for i in range(len(nums)):
# iの次の値からループする。
            for j in range(i + 1, len(nums)):
                # もしnumsのi番目の数字と、numsのj番目の数字の和がtargetと等しい場合はiとjの組み合わせを返す。
                if nums[i]+nums[j] == target:
                    return[i,j]
solution_instance = Solution()

# テスト用のリストと目標値を指定して twoSum メソッドを呼び出す
result = solution_instance.twoSum([2, 7, 11, 15], 9)
# result = solution_instance.twoSum([3,2,4], 6)
# result = solution_instance.twoSum([3,3], 6)
print(result)