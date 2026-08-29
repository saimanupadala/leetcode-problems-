class Solution:
    def findTheDifference(self, s, t):
        count = [0] * 26

     
        for ch in s:
            count[ord(ch) - ord('a')] += 1

     
        for ch in t:
            index = ord(ch) - ord('a')
            count[index] -= 1

          
            if count[index] < 0:
                return ch
        