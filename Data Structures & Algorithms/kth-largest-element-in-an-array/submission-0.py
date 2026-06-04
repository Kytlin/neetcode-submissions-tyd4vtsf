class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest_elems = []
        for i, num in enumerate(nums):
            if i < k or num > largest_elems[0]:
                if i >= k:
                    heapq.heappop(largest_elems)
                heapq.heappush(largest_elems, num)
        return largest_elems[0]