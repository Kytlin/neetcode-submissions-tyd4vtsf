class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        lower, upper = min(nums), max(nums)
        array_count = [0] * (upper-lower+1)
        for num in nums:
            array_count[num-lower] += 1

        longest_run, cur_run = 0, 0
        for count in array_count:
            if count > 0:
                cur_run += 1
            else:
                longest_run = max(longest_run, cur_run)
                cur_run = 0
        return max(longest_run, cur_run)