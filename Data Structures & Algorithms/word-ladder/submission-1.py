class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def compare(w, v):
            diff = False
            for i in range(len(w)):
                if w[i] != v[i]:
                    if diff: return False
                    diff = True
            return diff

        if endWord not in wordList: return 0

        wordList.append(beginWord)
        adjacency = {}
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if compare(wordList[i], wordList[j]):
                    adjacency.setdefault(wordList[i], set()).add(wordList[j])
                    adjacency.setdefault(wordList[j], set()).add(wordList[i])

        queue = [(beginWord, 1)]
        seen = {beginWord}

        while queue:
            word, path = queue.pop(0)
            if word == endWord:
                return path
            for word2 in adjacency.setdefault(word, set()):
                if word2 not in seen:
                    queue.append((word2, path+1))
                    seen.add(word2)
        
        return 0

        
        