class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        word_set = set(wordDict)
        M = max(len(w) for w in wordDict)

        for i in range(1, n + 1):
            for l in range(1, min(M, i) + 1):
                j = i - l
                if dp[j] == True and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]