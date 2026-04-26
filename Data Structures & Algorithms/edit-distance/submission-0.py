class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1)+1, len(word2)+1
        edits = [[0] * m for _ in range(n)]

        for i in range(1,n):
            edits[i][0] = i
        for j in range(1,m):
            edits[0][j] = j

        for i in range(1,n):
            for j in range(1,m):
                replace = 0 if word1[i-1] == word2[j-1] else 1
                edits[i][j] = min(edits[i-1][j]+1,edits[i][j-1]+1,edits[i-1][j-1]+replace)
        return edits[-1][-1]