import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        negated_nums = [-num for num in self.nums]
        heapq.heapify(negated_nums)

        for _ in range(self.k-1):
            heapq.heappop(negated_nums)
        return -negated_nums[0]
