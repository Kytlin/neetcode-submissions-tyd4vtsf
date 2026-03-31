# from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram_map = defaultdict(list)
        anagram_map = {}

        for word in strs:
            sorted_base_letters = sorted(list(word))
            base_word = "".join(sorted_base_letters)

            if base_word in anagram_map:
                anagram_map[base_word].append(word)
            else:
                anagram_map[base_word] = [word]
                
        return anagram_map.values()