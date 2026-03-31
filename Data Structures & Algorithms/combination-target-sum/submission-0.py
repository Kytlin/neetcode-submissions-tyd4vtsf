class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, comb_sum = [], []

        def dfs(i, remaining_sum):        
            if remaining_sum == 0:
                res.append(comb_sum[:])
            elif remaining_sum >= 0 and i < len(nums):
                # if remaining_sum-nums[i] >= 0:
                remaining_sum -= nums[i]
                comb_sum.append(nums[i])
                dfs(i, remaining_sum)
                # dfs(i+1,remaining_sum)

                remaining_sum += nums[i]
                comb_sum.pop()
                dfs(i+1, remaining_sum)

            return

        dfs(0, target)
        return res