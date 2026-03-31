from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_base_letters = sorted(list(word))
            anagram_map[tuple(sorted_base_letters)].append(word)
                
        return anagram_map.values()