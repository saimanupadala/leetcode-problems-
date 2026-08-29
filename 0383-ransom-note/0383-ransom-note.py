class Solution:
    def canConstruct(self, ransomNote, magazine):
        count = [0] * 26

     
        for ch in magazine:
            count[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            index = ord(ch) - ord('a')

            if count[index] == 0:
                return False

            count[index] -= 1

        return True
        