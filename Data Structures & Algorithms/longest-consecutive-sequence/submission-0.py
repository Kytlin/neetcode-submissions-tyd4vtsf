class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_seq = []
        for num in num_set:
            if num - 1 not in num_set:
                seq = [num]
                while num + 1 in num_set:
                    seq.append(num + 1)
                    num += 1
                if len(seq) > len(max_seq):
                    max_seq = seq
        return len(max_seq)