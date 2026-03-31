class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pair_sum = defaultdict(list)
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                pair_sum[num1 + num2].append((i,i+j+1))
        
        res = set()
        for i, num in enumerate(nums):
            if -num in pair_sum:
                for pair in pair_sum[-num]:
                    if i != pair[0] and i != pair[1]:
                        res.add(tuple(sorted((num, nums[pair[0]], nums[pair[1]]))))
        return list(res)