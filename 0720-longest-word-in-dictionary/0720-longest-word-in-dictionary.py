class Solution:
    def longestWord(self, words):
        words.sort()

        built = set()
        answer = ""

        for word in words:
            if len(word) == 1 or word[:-1] in built:
                built.add(word)

                if len(word) > len(answer):
                    answer = word

        return answer