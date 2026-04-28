class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos_prod = neg_prod = res = nums[0]

        for num in nums[1:]:
            candidates = (num, pos_prod * num, neg_prod * num)
            pos_prod, neg_prod = max(candidates), min(candidates)
            res = max(res, pos_prod)
        return res