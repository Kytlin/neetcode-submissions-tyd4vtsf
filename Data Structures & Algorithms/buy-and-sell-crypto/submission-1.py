class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit, cur_min = 0, prices[0]
        while j < len(prices):
            max_profit = max(max_profit, prices[j]-prices[i])
            if cur_min > prices[j]:
                i, j = j, j + 1
                cur_min = prices[i]
            else:
                j += 1
        return max_profit