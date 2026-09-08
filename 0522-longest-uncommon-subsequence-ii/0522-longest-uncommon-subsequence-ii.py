class Solution:
    def findLUSlength(self, strs):
        strs.sort(key=len, reverse=True)

        for i in range(len(strs)):
            uncommon = True

            for j in range(len(strs)):
                if i != j and self.isSubsequence(strs[i], strs[j]):
                    uncommon = False
                    break

            if uncommon:
                return len(strs[i])

        return -1

    def isSubsequence(self, a, b):
        i = 0

        for ch in b:
            if i < len(a) and a[i] == ch:
                i += 1

        return i == len(a)