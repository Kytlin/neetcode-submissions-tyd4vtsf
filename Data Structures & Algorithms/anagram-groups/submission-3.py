class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group_dict = defaultdict(list)
        anagram_group_list = []
        
        for word in strs:
            anagram_group_dict["".join(sorted(word))].append(word)

        for anagrams in anagram_group_dict.values():
            anagram_group_list.append(anagrams)

        return anagram_group_list