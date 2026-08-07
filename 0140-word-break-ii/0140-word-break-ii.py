class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)
        result = []
        def backtrack(start, sentence):
            if start == len(s):
                result.append(" ".join(sentence))
                return
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    sentence.append(word)
                    backtrack(end, sentence)
                    sentence.pop()     
        backtrack(0, [])
        return result
        