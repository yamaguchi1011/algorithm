# n個のガスステーションが円状に並んでいます。i番目のガスステーションはgas[i]の値の燃料があります。

# 容量が無限の車を持っており、配列costのi番目の要素から次の要素へ行くには、cost[i]の値の燃料が必要です。あなたは燃料が空の状態でどれかのガスステーションから旅を始めます。

# 2つの配列gas,costが与えられます。もし、燃料切れを起こさずに一周できた場合は、スタート地点のインデックスを返してください。できない場合は-1を返してください。一周できる場合は解がただ一つであることが保証されます。

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # 最初にcostがgasの合計より大きかったら-1を返す。（costの方が多い場合は、絶対に一周できないため）
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0,0
        for i in range(len(gas)):
            #gasで補給できる燃料から、costで消費する燃料を引いて、残った分をfuelに格納する。
            fuel += gas[i] - cost[i]
            # 残った燃料（fuel）が０未満なら、移動できなくなるので、スタート地点を一つ進めて、燃料を０に戻す。その繰り返しで、スタート地点を特定する
            if fuel < 0:
                start = i +1
                fuel = 0
        return start

solution_instance = Solution()

result = solution_instance.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2])
print(result)