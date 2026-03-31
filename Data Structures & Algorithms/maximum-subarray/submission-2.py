class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        
        cur_sum, max_sum = 0, 0
        for num in nums:
            cur_sum += num
            if cur_sum < 0:
                cur_sum = 0
            else:
                max_sum = max(max_sum, cur_sum)
                
        return max_sum