class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        start, end = 0, 1
        while end < len(prices):
            if prices[end] < prices[start]:
                start, end = end, end + 1
            else:
                res = max(res, prices[end]-prices[start])
                end += 1
        return res