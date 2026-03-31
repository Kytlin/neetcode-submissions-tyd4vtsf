class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_seen = set()
        for num in nums:
            if num not in has_seen:
                has_seen.add(num)
            else:
                return True
        return False