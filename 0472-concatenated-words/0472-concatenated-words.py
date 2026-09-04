class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        word_set = set(words)
        result = []

        for word in words:
            n = len(word)

            # dp[i] = True if word[:i] can be formed
            # using one or more smaller words
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    # Make sure the current part is a word
                    if not dp[j]:
                        continue

                    # Prevent using the complete word itself
                    if j == 0 and i == n:
                        continue

                    if word[j:i] in word_set:
                        dp[i] = True
                        break

            if dp[n]:
                result.append(word)

        return result
        