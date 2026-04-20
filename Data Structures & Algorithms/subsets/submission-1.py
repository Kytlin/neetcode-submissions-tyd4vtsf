class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def search(elem, idx):
            if idx == len(nums):
                ans.append(elem)
                return

            search(elem, idx + 1)
            search([nums[idx]] + elem, idx + 1)

        search([], 0)
        return ans