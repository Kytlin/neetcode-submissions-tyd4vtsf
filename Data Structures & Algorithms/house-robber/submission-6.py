class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev, cur = 0, 0

        for i in range(n):
            prev, cur = cur, max(cur, prev + nums[i])

        return cur