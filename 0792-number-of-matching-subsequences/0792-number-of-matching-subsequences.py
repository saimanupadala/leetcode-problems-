class Solution:
    def numMatchingSubseq(self, s, words):
        n = len(s)

        # next_pos[i][c] = next position of character c
        # at or after index i
        next_pos = [[-1] * 26 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            next_pos[i] = next_pos[i + 1].copy()
            next_pos[i][ord(s[i]) - ord('a')] = i

        count = 0

        # Cache duplicate words
        cache = {}

        for word in words:
            if word in cache:
                count += cache[word]
                continue

            pos = 0
            possible = True

            for ch in word:
                c = ord(ch) - ord('a')

                if pos > n:
                    possible = False
                    break

                nxt = next_pos[pos][c]

                if nxt == -1:
                    possible = False
                    break

                pos = nxt + 1

            cache[word] = 1 if possible else 0
            count += cache[word]

        return count