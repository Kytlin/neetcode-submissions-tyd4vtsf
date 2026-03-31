class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_count = defaultdict(int)
        for letter in s:
            anagram_count[letter] += 1
        for letter in t:
            anagram_count[letter] -= 1
            if anagram_count[letter] < 0:
                return False
        return set(anagram_count.values()) == {0}