
from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        queue = deque([(s1, 0)])
        visited = {s1}

        while queue:
            s, swaps = queue.popleft()

            i = 0
            while s[i] == s2[i]:
                i += 1

            for j in range(i + 1, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    chars = list(s)
                    chars[i], chars[j] = chars[j], chars[i]
                    new_s = ''.join(chars)

                    if new_s == s2:
                        return swaps + 1

                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append((new_s, swaps + 1))

        return 0
 