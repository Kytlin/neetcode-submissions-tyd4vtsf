class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        res = ""
        for i in range(min(n,m)):
            res += word1[i]
            res += word2[i]
        
        return res + word2[n:] if n < m else res + word1[m:]