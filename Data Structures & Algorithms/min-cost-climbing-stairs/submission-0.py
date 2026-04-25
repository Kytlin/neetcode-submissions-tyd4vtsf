class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [0] * (len(cost) + 1)
        # dp[1] = cost[0]
        p1, p2 = 0, cost[0]

        for i in range(2, len(cost) + 1):
            # dp[i] = min(dp[i-1], dp[i-2]) + cost[i-1]
            p1, p2 = p2, min(p1, p2) + cost[i-1]

        # return min(dp[-2], dp[-1])
        return min(p1, p2)