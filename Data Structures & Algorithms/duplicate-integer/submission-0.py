from collections import defaultdict 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_seen = defaultdict(int)
        for num in nums:
            if has_seen[num] > 0:
                return True
            has_seen[num] += 1
        return False