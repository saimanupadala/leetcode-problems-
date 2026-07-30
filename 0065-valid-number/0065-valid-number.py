class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        num = False
        dot = False
        exp = False
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = True
            elif ch in ['+', '-']:
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            elif ch == '.':
                if dot or exp:
                    return False
                dot = True
            elif ch in ['e', 'E']:
                if exp or not num:
                    return False
                exp = True
                num = False
            else:
                return False
        return num
        