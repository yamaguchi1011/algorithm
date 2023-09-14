# 配列numsが与えられます。最初に配列arrayの1番目の要素にいます。

# 各要素はあなたがジャンプできる最大距離を示します。

# 最後の要素までジャンプできる場合はTrue、そうでなければFalseを返してください。

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # currentに最初の要素の値を入れる
        current = nums[0]
        # １から要素数ぶん繰り返す
        for i in range(1,len(nums)):
            # もしcurrentが０ならその時点で Falseを返す。
            if current == 0:
                return False
            # ０でない場合は、currentから１を引いたものをcurrentに入れる(右に一つ進むという意味)
            current -= 1
            # 右に一つ進んだ結果と、今いる要素の数字を比べて、大きい方をジャンプ最大値に設定する。（辿り着けばいいだけなので、最大値を取っていく右に進んでいくにつれて、マイナス１ずつ減っていくが、０になればそこで終了。）
            current = max(current, nums[i])
        return True




solution_instance = Solution()


result = solution_instance.canJump(nums = [1,3,0,0,4])
print(result)

# 貪欲法（Greedy Algorithm）は、問題を解決するアルゴリズムの一種で、各ステップで局所的に最適な選択を行い、その結果を積み重ねて最終的な解を得る方法です。貪欲法は、その名前が示す通り、「貪欲に（greedily）」最適な選択をするという特徴があります。つまり、各ステップで最も有望な選択を選んで進むため、必ずしも最適な結果が得られるわけではないことがありますが、簡潔で高速なアルゴリズムを提供することがあります。

# 貪欲法の特徴として以下の点が挙げられます：

# 局所的な最適性: 貪欲法は各ステップで局所的に最適な選択を行います。つまり、その時点での最適な選択を優先的にします。しかし、それが全体の最適解につながる保証はありません。

# 効率性: 貪欲法は一般的に計算コストが低いため、高速に問題を解決できることがあります。このため、大規模な問題やリアルタイム性が求められる問題に適しています。

# 最適性の保証がない: 貪欲法は必ずしも最適解を見つけるわけではなく、最適性を保証するものではありません。問題によっては、貪欲法によって得られた解が最適でないことがあります。

# 貪欲法は、以下のような問題に適していることがあります：

# コインのおつりを最小限の枚数で支払う問題（貪欲法は通常有効です）。
# グラフ上での最短経路問題（ダイクストラ法などが貪欲法の一種です）。
# スケジューリング問題（終了時刻が早い順に仕事を選ぶなど）。
# しかし、貪欲法を使用する前に、問題の性質に合わせて適切なアルゴリズムが存在しないか、最適性を保証する方法を検討することが重要です。貪欲法はシンプルで理解しやすいため、多くの場合、初めに試す価値があります。




