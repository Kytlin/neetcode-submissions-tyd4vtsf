class Solution:
    def uniquePaths(self, m: int, n: int) -> int:  
        dp = [[1] * n for _ in range(m)]
        for y in range(1,m):
            for x in range(1,n):
                dp[y][x] = dp[y][x-1] + dp[y-1][x]
        return dp[-1][-1]