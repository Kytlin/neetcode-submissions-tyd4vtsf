class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start_pos = 0
        while start_pos < len(s):
            delimiter_pos = s.find('#', start_pos)
            cur_word_len = int(s[start_pos:delimiter_pos])
            res.append(s[delimiter_pos+1:delimiter_pos+cur_word_len+1])
            start_pos = delimiter_pos+cur_word_len+1
        return res