class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for ch in s1:
            count1[ord(ch) - ord('a')] += 1

        k = len(s1)

        for i in range(len(s2)):
            count2[ord(s2[i]) - ord('a')] += 1

            if i >= k:
                count2[ord(s2[i - k]) - ord('a')] -= 1

            if count1 == count2:
                return True

        return False   