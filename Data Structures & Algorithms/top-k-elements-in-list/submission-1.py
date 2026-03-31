from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
        count_arr = [[] for _ in range(len(nums)+1)]
        for n, count in freq_map.items():
            count_arr[count].append(n)

        res = [item for sublist in count_arr for item in sublist]
        return res[len(res)-k:]