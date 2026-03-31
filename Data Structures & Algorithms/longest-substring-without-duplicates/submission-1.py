from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        char_in_substr = defaultdict(int)
        start = 0
        for end, c in enumerate(s):
            if c in char_in_substr:
                while s[start] != c and start < end:
                    del char_in_substr[s[start]]
                    start += 1
                start += 1
            char_in_substr[c] = 1
            if maxlen < end-start+1:
                print(start,end)
                maxlen = max(maxlen, end-start+1)
        return maxlen