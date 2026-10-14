
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = "L" + dominoes + "R"
        result = []
        prev = 0

        for i in range(1, len(s)):
            if s[i] == '.':
                continue

            middle = i - prev - 1

            if prev > 0:
                result.append(s[prev])

            if s[prev] == s[i]:
                result.append(s[prev] * middle)
            elif s[prev] == 'R' and s[i] == 'L':
                result.append('R' * (middle // 2))
                if middle % 2:
                    result.append('.')
                result.append('L' * (middle // 2))
            else:
                result.append('.' * middle)

            prev = i

        return ''.join(result)
