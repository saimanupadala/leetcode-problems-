class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

       
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        
        for ch in count:
            if count[ch] < k:
              
                parts = s.split(ch)

             
                return max(
                    self.longestSubstring(part, k)
                    for part in parts
                )

    
        return len(s)
        