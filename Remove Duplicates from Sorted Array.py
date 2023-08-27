# 問題文がわかりにくいので、要するに、与えられた非降順のソート済み配列から、重複を除いた要素を前方に詰めてその要素数を答える。要素数を数えるプロセスを実装する必要があります。その際に、要素の順序は保持されなければなりません。

# 下記問題文
# 非降順でソートされた数値型の配列numsが与えられます。各要素が1度だけ出現するように重複を除外してください。要素同士の相対的な順序は同じ状態を保ってください。

# いくつかの言語では配列の長さを変えられないため、配列numsの最初の部分に結果を入れなければなりません。

# もし重複除外後にk個の要素がある場合、配列numsの最初のk個の要素は最終結果を持っていなければなりません。k個より先の要素は残していても問題ありません。

# numsの配列の最初のk個に最終結果を入れて、kを返してください。

# 別の配列は用意してはいけません。

# ジャッジは、以下のコードであなたの解をテストする：

# int[] nums = [...]; // 入力配列
# int[] expectedNums = [...]; // 正しい長さの期待される答え

# int k = removeDuplicates(nums); // 実装を呼び出します。

# assert k == expectedNums.length；
# for (int i = 0; i < k; i++) { { nums[i] == expectedNums.
#     assert nums[i] == expectedNums[i]；
# }
# すべてのアサーションがパスすれば、あなたのソリューションは受け入れられる。
# 例1：

# 入力： nums = [1,1,2］
# 出力： 2, nums = [1,2,_] です。
# 説明 あなたの関数はk = 2を返すべきで、numsの最初の2つの要素はそれぞれ1と2である。
# 返されたkの後ろに何を残してもかまわない（だからアンダースコアなのだ）。

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
      # 与えられたnumsを使って並び替えている。
      # jを１スタートにするのは、０番目の値は新しいリストに必ず含まれる（非降順でソートされており、一番最初は重複を気にしなくていいため）から２番目にある値（配列では０から始まる）が新しいリストの値と重複しているかを比べる必要がある。
        j = 1
        # rangeは１からスタートしてlenで要素数までの整数を作成する
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:#ここでiが１としたら、i-1で０になるので、numsの１番目と０番目の値を比べている。つまり、対象の値の一つ前の値と比べている。
                nums[j] = nums[i]#もし上記のif文がtrueのとき（iとi-1が同じでない時）nums[j]（j初期値を１に設定しているので最初は１）にnums[i]の値を入れる。
                j += 1 #jを一つ進める
        return j

solution_instance = Solution()

result = solution_instance.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]
)

print(result)    