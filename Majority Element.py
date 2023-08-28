# サイズ n の配列 nums を指定すると、過半数の要素を返してください。 
# 過半数とは、⌊n / 2⌋ 回以上出現する要素です。過半数の要素が常に配列内に存在すると想定できます。

#今回の条件の多数派要素とは、⌊n / 2⌋ 回より多く（n/2で出た値は含まない）出現する要素←この部分が大事で、どんな配列でも要素数（n）➗2以上ということなので、中央値は絶対に多数派要素になる。
# nums = [1,2,3,6,6,6,6]
# nums = [1,2,2,2,2,3,4]
# ソートで昇順にして中央値を返せば、今回の条件（n/2より多い）にあうので下記でも実装できる。
# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         nums.sort()
#         return nums[len(nums) // 2]

# hashを用いた書き方
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         m = defaultdict(int)

#         for num in nums:
#             # mのnumキーの値を１増やしている
#             # 例えば、リスト nums が [2, 2, 3, 4, 2] という要素を持つ場合を考えてみましょう。初めて要素 2 を処理すると、m[2] の初期値が0なので、m[2] は 1 になります。2回目に要素 2 を処理すると、m[2] は 2 になります。このようにして、各要素の出現回数が辞書 m 内でカウントされます。
#             m[num] += 1
#         n = n // 2
#         # .itemsでキーと値を取ってくる
#         for key, value in m.items():
#             if value > n:
#                 return key
#         return 0

# (Boyer-Moore Voting Algorithm)ボイヤー・ムーア投票アルゴリズム
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # 初期値を設定する
        count = 0
        candidate = 0
        # numsの値を取ってきて、要素数分、繰り返し処理する
        for num in nums:
            # もしcountが０のときはcandidate(候補者）にnumを代入する
            if count == 0:
                candidate = num
            # もしnumがcandidateと同じならcountをインクリメントする
            if num == candidate:
                count += 1
            # そうじゃない時はcountを１減らす（デクリメント）
            else:
                count -=1
        return candidate

solution_instance = Solution()

# result = solution_instance.majorityElement(nums = [3,2,3])
result = solution_instance.majorityElement(nums = [2,2,1,1,1,2,2])
result = solution_instance.majorityElement(nums = [1,1,1,1,2,3,4,4,4,4,4,1,1])
print(result)  

#(Boyer-Moore Voting Algorithm)ボイヤー・ムーア投票アルゴリズムについて
# このアルゴリズムの考え方は
# リストの数字を順に見ていって
# まずカウントが０の場合、その数字を候補者として選ぶ（その数字が一番多く出てくる数字だと思ってとりあえず候補者にする）
# もし今見ている数字が候補者と同じならカウントを増やす。
# もし今見ている数字が候補者と違うならカウントを減らす。（０になったらその数字を候補者にする）
# 全ての数字を見たあとで、残った候補者が答えになる。つまり一番多く出てきた数字ということ。

# majority elementを多数派要素と訳されたので、全体の中で一番重複している数という認識で考えていたが、正しくは過半数（全体の半分より多い数）を占める要素を知りたいとのことで、やっと理解できた。
# 多数決（多数派）と過半数は全然違う