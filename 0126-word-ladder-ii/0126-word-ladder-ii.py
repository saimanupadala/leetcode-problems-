from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        parents = defaultdict(list)
        current_level = {beginWord}
        visited = set()
        found = False
        while current_level and not found:
            visited.update(current_level)
            next_level = set()
            for word in current_level:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word not in wordSet or new_word in visited:
                            continue
                        if new_word == endWord:
                            found = True
                        next_level.add(new_word)
                        parents[new_word].append(word)
            current_level = next_level
        if not found:
            return []
        result = []
        def dfs(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            for parent in parents[word]:
                dfs(parent, path + [parent])
        dfs(endWord, [endWord])
        return result
        