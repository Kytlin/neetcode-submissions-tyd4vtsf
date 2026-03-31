class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        char_map = defaultdict(int)
        for c in s1:
            char_map[c] += 1

        start = 0
        for end, c in enumerate(s2):
            # consume right
            if c in char_map:
                char_map[c] -= 1

            # enforce window size <= len(s1)
            if end - start + 1 > len(s1):
                left = s2[start]
                if left in char_map:
                    char_map[left] += 1
                start += 1

            # check success only at exact window size
            if end - start + 1 == len(s1) and all(v == 0 for v in char_map.values()):
                return True

        return False