class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        res = nums[0]
        for start in range(len(nums)):
            for end in range(start,len(nums)):
                res = max(res, prefix_sum[end+1] - prefix_sum[start])

        return res