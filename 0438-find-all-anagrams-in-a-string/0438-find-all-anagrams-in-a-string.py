class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        window = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        result = []
        left = 0
        window_size = len(p)

        for right in range(len(s)):
 
            window[ord(s[right]) - ord('a')] += 1

         
            if right - left + 1 > window_size:
                window[ord(s[left]) - ord('a')] -= 1
                left += 1

          
            if window == p_count:
                result.append(left)

        return result
        