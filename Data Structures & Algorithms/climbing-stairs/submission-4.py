class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]

            if i == 0 or i == 1:
                return 1
            
            res = dfs(i-1) + dfs(i-2)
            memo[i] = res
            return memo[i]

        return dfs(n)