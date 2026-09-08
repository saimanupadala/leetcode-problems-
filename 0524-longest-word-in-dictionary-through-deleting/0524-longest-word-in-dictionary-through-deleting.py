class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        answer = ""

        for word in dictionary:
            i = 0

            # Check if word is a subsequence of s
            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1

            if i == len(word):
                # Update answer
                if len(word) > len(answer):
                    answer = word
                elif len(word) == len(answer) and word < answer:
                    answer = word

        return answer 