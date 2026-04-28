class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[i] for i in range(n)]
        res = nums[0]

        for i, num in enumerate(nums):
            prod_from_i = num
            for j in range(i-1,-1,-1):
                if (prod_from_i > 0 and nums[j] > 0) or (prod_from_i < 0 and nums[j] < 0):
                    dp[i] = prod_from_i * nums[j]
                prod_from_i *= nums[j]
            res = max(res, dp[i])
        return res