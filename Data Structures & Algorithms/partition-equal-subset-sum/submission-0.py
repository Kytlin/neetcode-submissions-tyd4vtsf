class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        n, target = len(nums), sum(nums) // 2
        dp = [[False] * (target + 1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(1,n+1):
            for j in range(1,target+1):
                if dp[i-1][j] or dp[i-1][j-nums[i-1]]:
                    dp[i][j] = True

        return dp[-1][-1]