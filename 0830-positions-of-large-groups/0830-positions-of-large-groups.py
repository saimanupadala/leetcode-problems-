
class Solution:
    def largeGroupPositions(self, s: str):
        res = []
        start = 0

        for i in range(1, len(s) + 1):
            if i == len(s) or s[i] != s[start]:
                if i - start >= 3:
                    res.append([start, i - 1])
                start = i

        return res
