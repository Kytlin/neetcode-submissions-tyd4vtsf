class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_posn = {}
        for i, num in enumerate(nums):
            if target - num in diff_posn:
                return [diff_posn[target - num], i]
            diff_posn[num] = i
