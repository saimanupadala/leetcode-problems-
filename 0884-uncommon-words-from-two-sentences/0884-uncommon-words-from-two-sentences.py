
class Solution:
    def uncommonFromSentences(self, s1, s2):
        words = s1.split() + s2.split()

        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        result = []

        for word in freq:
            if freq[word] == 1:
                result.append(word)

        return result
