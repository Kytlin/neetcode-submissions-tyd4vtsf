class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i, money in enumerate(nums[2:]):
            dp[i+2] = max(dp[i+1], dp[i]+money)
        return dp[-1]