class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(visited, idx):
            if idx == len(nums):
                ans.append(subset.copy())
                return

            for n in nums:
                if n not in visited:
                    subset.append(n)
                    visited.add(n)
                    dfs(visited, idx+1)
                    visited.remove(n)
                    subset.pop()

        dfs(set(), 0)
        return ans