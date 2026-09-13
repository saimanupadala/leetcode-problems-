class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        unique_types = len(set(candyType))
        
        return min(unique_types, n // 2)