class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        count = [0] * 26
        length = 0

        for i in range(len(s)):
            if i > 0 and (
                ord(s[i]) == ord(s[i - 1]) + 1
                or s[i - 1] == 'z' and s[i] == 'a'
            ):
                length += 1
            else:
                length = 1

            index = ord(s[i]) - ord('a')
            count[index] = max(count[index], length)

        return sum(count)