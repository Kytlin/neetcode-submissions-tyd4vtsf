class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(str(len(s)))) + str(len(s)) + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, j, k = 0, 0, 0
        while i < len(s):
            j = int(s[i])
            k = int(s[i+1:i+j+1]) if j > 0 else 1
            i += j+1
            res.append(s[i:i+k])
            i += k
        return res 