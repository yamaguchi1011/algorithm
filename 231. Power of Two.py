# 整数nが与えられます。それが2のべき乗であればtrueを返してください。

# そうでない場合は、falseを返してください。

# 整数nが2のべき乗であるのは、n==2xとなるような整数xが存在するときです。

# 繰り返し処理
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         count = 0
#         # numberは２の何乗かを探すための変数
#         number = 2**count
#         # nがnumber以上であれば繰り返す。つまり与えられた数字分繰り返していく
#         while n >= number:
#             # numberとnが一致した時にtrueを返す。
#             if number == n:
#                 return True
#             # 一回のループごとにcountを１づつ進める
#             count += 1
#             # ２の０乗、２の１乗、２の２乗...と計算した値をnumberに格納して、繰り返しの最初でnumberとnが一致するかを調べている。
#             number = 2**(count)
#         return False


# ビットシフト　繰り返し
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         number = 1
#         while n >= number:
#             if number ==n:
#                 return True
#             # ビットシフト演算子 <<は数字を左に１ビットずらす。(右にずらしたい場合は>>)これにより数値が２倍になる。下一桁に0が追加される
#             number <<= 1
#         return False

# ビットワイズAND演算
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return 0
        return (n&(n-1))==0


solution_instance = Solution()

result = solution_instance.isPowerOfTwo(n = 16)
print(result)

# ビットワイズ演算でnとn-1の最上位ビットを比較している
# ２のべき乗の整数は２進数表現において最上位ビットが立っている。（最も左側の１ビット）
# ２進数表現では2は１０で、４は１００、８は１０００、１６は１００００になる
# つまりnが４だった場合にn-1は３になる。
# ２進数表現では１１になる。
# AND演算は、２進数同士を一つずつ比べて、対応するビットが１なら、１でそれ以外の組み合わせは０になる。それを繰り返していき、返された数字で新たなビットの組み合わせを作って、１０進数にして、値が0かどうかを見ている。

# 例
# 以下に、ビットワイズAND演算の基本的な動作を示します：

# 0 AND 0 は 0 を返します。
# 0 AND 1 は 0 を返します。
# 1 AND 0 は 0 を返します。
# 1 AND 1 は 1 を返します。

# 5 (二進数で 0101) と 3 (二進数で 0011) をAND演算すると、結果は 1 (二進数で 0001) になります。これは5と3の対応するビット位置でAND演算された結果です。

# 6 (二進数で 0110) と 2 (二進数で 0010) をAND演算すると、結果は 2 (二進数で 0010) になります。これも6と2の対応するビット位置でAND演算された結果です。

# 7 (二進数で 0111) と 5 (二進数で 0101) をAND演算すると、結果は 5 (二進数で 0101) になります。これは7と5の対応するビット位置でAND演算された結果です。