class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for c in coins:
            if c <= amount:
                dp[c] = 1
        
        for i in range(1,amount+1):
            for c in coins:
                if i-c >= 0 and dp[i] > dp[i-c] + 1:
                    dp[i] = dp[i-c] + 1

        return dp[amount] if dp[amount] <= amount else -1