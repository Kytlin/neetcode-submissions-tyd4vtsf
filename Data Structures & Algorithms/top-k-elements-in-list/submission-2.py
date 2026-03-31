import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq, freq_dict = [], defaultdict(int)
        for num in nums:
            freq_dict[num] += 1

        for key in freq_dict:
            heapq.heappush(max_freq, (-freq_dict[key], key))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_freq)[1])

        return res