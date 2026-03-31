from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            canonical_anagram = "".join(sorted(word))
            anagram_map[canonical_anagram].append(word)
            
        res = []
        for anagram_list in anagram_map.values():
            res.append(anagram_list)
        return res