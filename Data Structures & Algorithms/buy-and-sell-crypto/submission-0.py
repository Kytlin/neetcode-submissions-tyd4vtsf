class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit, cur_min = 0, prices[0]
        for j in range(1,len(prices)):
            max_profit = max(max_profit, prices[j]-prices[i])
            if cur_min > prices[j]:
                i = j
                cur_min = prices[i]
        return max_profit