from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_map = Counter(s)
        for c in t:
            if c not in count_map or count_map[c] == 0:
                return False
            count_map[c] -= 1
        return True