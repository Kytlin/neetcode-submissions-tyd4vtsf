class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] * (len(nums)+1)
        for i, num in enumerate(nums):
            prefix_prod[i+1] = prefix_prod[i] * num

        res = [0] * len(nums)
        right_prod = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = prefix_prod[i] * right_prod
            right_prod *= nums[i]
        return res