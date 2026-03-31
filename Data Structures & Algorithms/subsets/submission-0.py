class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def findSubset(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            findSubset(i+1)

            subset.pop()
            findSubset(i+1)

        findSubset(0)
        return res
            