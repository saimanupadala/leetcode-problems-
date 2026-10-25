class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0

        # Find the decoded string length
        for ch in s:
            if ch.isdigit():
                length *= int(ch)
            else:
                length += 1

        # Work backwards to find the kth character
        for ch in reversed(s):
            k %= length

            if k == 0 and ch.isalpha():
                return ch

            if ch.isdigit():
                length //= int(ch)
            else:
                length -= 1