# 符号なし整数の2進表現を取り、それが持つ'1'ビットの数（ハミング重みとしても知られている）を返す関数を書きなさい。

# 注意
# Javaのように符号なし整数型がない言語もある。この場合、入力は符号付き整数型として与えられる。整数の内部バイナリ表現は符号ありでも符号なしでも同じなので、実装に影響を与えることはない。

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n:
            count += n & 1
            n >>= 1
        return count

solution_instance = Solution()
result = solution_instance.hammingWeight(n = 0b00000000000000000000000000001011)
print(result)