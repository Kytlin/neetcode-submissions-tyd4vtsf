class Solution:
    def isValid(self, s: str) -> bool:
        b_cache = []
        b_map = {")" : "(", "]" : "[", "}" : "{"}
        for bracket in s:
            if b_cache != [] and bracket in b_map and b_map[bracket] in b_cache[-1]:
                b_cache.pop()
            else:
                b_cache.append(bracket)
        return b_cache == []