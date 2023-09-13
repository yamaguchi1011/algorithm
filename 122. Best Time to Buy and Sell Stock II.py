# i番目の要素がi日目の株価を示す整数配列pricesが与えられます。

# 各日で、株を買うか売るかを選ぶことができます。

# 同時に1つだけ保有することができます。

# 同じ日に株を買って売ることができます。

# 利益が最大となるように取引した場合の、最大利益を返してください。

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 0
        sum_profit = 0

        for i in range(len(prices)):
            if prices[right] > prices[left]:
                sum_profit += prices[right] - prices[left]
            left = right
            right += 1
        return sum_profit

solution_instance = Solution()

# result = solution_instance.maxProfit(prices = [7,1,5,3,6,4])
# result = solution_instance.maxProfit(prices = [7,1,5,3,6,4])
result = solution_instance.maxProfit(prices = [7,1,5,3,6,4])
print(result)
