
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        last = [-1] * 26
        prev = [-1] * 26
        ans = 0

        for i, ch in enumerate(s):
            c = ord(ch) - ord('A')

            ans += (i - last[c]) * (last[c] - prev[c])

            prev[c] = last[c]
            last[c] = i

        for c in range(26):
            ans += (n - last[c]) * (last[c] - prev[c])

        return ans
