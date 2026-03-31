class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        start = 0
        for end in range(len(prices)):
            res = max(res, prices[end]-prices[start])
            if prices[end] < prices[start]:
                start = end
        return res