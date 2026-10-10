
class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [0] * n
        prev = -n

        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev

        prev = 2 * n

        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)

        return answer
