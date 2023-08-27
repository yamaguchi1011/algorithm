# 整数の配列numsと整数の変数valが与えられます。numsに含まれるすべてのvalをインプレイス処理で取り除いてください。nums内の各要素の相対的な順番は変わるかもしれません。

# いくつかの言語では配列の長さを変えることはできないため、代わりに配列numsの初めの部分を処理結果で置き換える必要があります。具体的には、除外操作を行った後にk個の要素があれば、配列numsの最初のk個の要素は処理後の最終結果である必要があります。k個目を超えた要素の有無は問いません。

# 配列numsの最初のk個の要素を処理後の結果に置き換えてからkを返してください。

# 別の新たな配列を割り当ててはなりません。O(1)のメモリ空間(?)で、入力された配列のみを使ってインプレイス処理で進めてください。

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
    # 与えられたnumsの中で行う
    # 今回kは重複を省いたnumsの要素の個数を表すもので最初は０として初期化しておく
        k = 0
        # numsの数だけループする
        for i in range(len(nums)):
# numsのi番目の値とvalの値が同じであれば、この後の処理である、kに代入する処理は行わない。
            if nums[i] == val:
                # numsのi番目とvalが同じ時ループの先頭に戻ってループの数を進める。forまで戻る。
                continue
            # numsのk番目にnumsのi番目の値を代入する
            nums[k] = nums[i]
            # kを進める
            k += 1
        return k
        


solution_instance = Solution()

result = solution_instance.removeElement(nums = [3,2,2,3], val = 3)

print(result)  


# インプレイス(in-place)・・・追加のメモリを（ほとんど）使用せずに，入力を置換や入れ替えによって直接上書きすることで所望の結果を得るアルゴリズムのこと