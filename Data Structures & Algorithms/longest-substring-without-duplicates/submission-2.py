class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, substr = 0, set()
        start = 0
        for end in range(len(s)):
            while s[end] in substr:
                res = max(res, end-start)
                substr.remove(s[start])
                start += 1
            substr.add(s[end])
        return max(res, len(s)-start)