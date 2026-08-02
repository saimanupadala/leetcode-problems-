class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            for length in range(1, 4):
                if start + length > len(s):
                    break
                part = s[start:start + length]
                if len(part) > 1 and part[0] == '0':
                    continue
                if int(part) <= 255:
                    backtrack(start + length, path + [part])
        backtrack(0, [])
        return res
        