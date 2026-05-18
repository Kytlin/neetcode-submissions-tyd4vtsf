class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        n = len(nums)
        dp = [0] * n
        dp[1] = nums[0]
        for i in range(2,n):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])

        return max(dp[-1], nums[-1] + dp[-2])