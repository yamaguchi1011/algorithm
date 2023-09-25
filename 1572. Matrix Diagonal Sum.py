
# 行列matが与えられるので、対角線上の要素の合計を返してください。

# 行列の中央の要素は2回加算されないようにしてください。

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        # 左上から右下にかけての対角線の合計を持つ変数
        primary_sum = 0
        # 右上から左下にかけての対角線の合計を持つ変数
        secondary_sum = 0
        # 列（内側の要素）のインデックス
        primary_column = secondary_column = 0

        for i in range(len(mat)):
            # 右端から左端へ向けてインデックスを動かす。
            secondary_column -= 1
            # 二つの対角線に値を与える
            primary_sum += mat[i][secondary_column]
            secondary_sum += mat[i][primary_column]
            # 左端から右端に向けてインデックスを動かす
            primary_column += 1
        # 2つの対角線を合計する
        answer = primary_sum + secondary_sum
        # 行列中央の要素が２回加算されるのは、行と列が奇数かつ同じ数の場合
        if len(mat)%2==1 and len(mat)==len(mat[0]):
          # 二次元配列の中央値にアクセスするには行と列を２で割って中央値を求める。(//は小数点以下を切り捨てする 
            answer -= mat[len(mat)//2][len(mat)//2]
        # 回答を返す
        return answer


solution_instance = Solution()

result = solution_instance.diagonalSum( mat = [[1,2,3],
              [4,5,6],
              [7,8,9]])
print(result)