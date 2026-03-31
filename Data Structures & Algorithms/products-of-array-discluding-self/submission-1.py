class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix_prod = [1] * len(nums)
        suffix_prod = [1] * len(nums)

        for i in range(1,len(nums)):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
            suffix_prod[i] = suffix_prod[i-1] * nums[-i]

        for i in range(len(nums)):
            res.append(prefix_prod[i] * suffix_prod[-i-1])
        return res