class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        start, max_count = 0, 0
        for end, c in enumerate(s):
            while max_count + k < end - start:
                char_count[s[start]] -= 1
                start += 1
            char_count[c] += 1
            max_count = max(max_count, char_count[c])
        return min(len(s), max_count + k)