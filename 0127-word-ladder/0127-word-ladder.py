from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in wordSet:
                        queue.append((new_word, length + 1))
                        wordSet.remove(new_word)   # Mark as visited
        return 0
        