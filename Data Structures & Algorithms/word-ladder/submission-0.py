class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_len = len(beginWord)
        word_lookup = set(wordList)

        if endWord not in word_lookup:
            return 0

        adj_words = defaultdict(list) 
        start_ascii, end_ascii = 97, 123
        for word in [beginWord] + wordList:
            for posn in range(word_len):
                for ord_idx in range(start_ascii, end_ascii):
                    trans_word = word[:posn] + chr(ord_idx) + word[posn+1:]
                    if trans_word != word and trans_word in word_lookup:
                        adj_words[word].append(trans_word)

        visited = set()
        queue = deque()

        queue.append((beginWord, 1))
        visited.add(beginWord)
        while queue:
            word, seq_length = queue.popleft()
            for diff_word in adj_words[word]:
                if diff_word == endWord:
                    return seq_length+1
                if diff_word not in visited:
                    queue.append((diff_word, seq_length+1))
                    visited.add(diff_word)
        return 0
        