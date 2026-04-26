class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1)+1, len(word2)+1
        prev_edits, cur_edits = list(range(m)), [0]*m

        for i in range(1,n):
            cur_edits[0] = i
            for j in range(1,m):
                replace = 0 if word1[i-1] == word2[j-1] else 1
                cur_edits[j] = min(cur_edits[j-1]+1,prev_edits[j]+1,prev_edits[j-1]+replace)
            prev_edits, cur_edits = cur_edits, prev_edits
        return prev_edits[-1]