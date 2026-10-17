class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = 0
        result = list(s)

        for i in range(len(s) - 1, -1, -1):
            total = (total + shifts[i]) % 26
            result[i] = chr((ord(s[i]) - ord('a') + total) % 26 + ord('a'))

        return ''.join(result)