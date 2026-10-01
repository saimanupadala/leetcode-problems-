class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        parts = []
        count = 0
        start = 0

        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1

            # Found one complete special substring
            if count == 0:
                inner = s[start + 1:i]
                parts.append("1" + self.makeLargestSpecial(inner) + "0")
                start = i + 1

        # Put larger special strings first
        parts.sort(reverse=True)

        return "".join(parts)