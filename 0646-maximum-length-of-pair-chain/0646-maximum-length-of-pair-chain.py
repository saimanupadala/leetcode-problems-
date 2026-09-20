class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])
        
        count = 0
        end = float('-inf')
        
        for left, right in pairs:
            if left > end:
                count += 1
                end = right
        
        return count  