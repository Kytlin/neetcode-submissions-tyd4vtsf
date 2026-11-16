class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = defaultdict(int)
        for num in nums:
            freq_count[num] += 1

        freq_list = [(key, val) for key, val in freq_count.items()]
        freq_list.sort(key=lambda entry : entry[1], reverse=True)

        return [ key for key, val in freq_list[:k] ]