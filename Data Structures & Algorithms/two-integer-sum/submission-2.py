class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_posn = {}
        for i, num in enumerate(nums):
            diff_posn[num] = i

        for j, num in enumerate(nums):
            diff = target - num
            i = diff_posn.get(diff)
            if i != None and i != j:
                return [i, j] if i < j else [j, i]
