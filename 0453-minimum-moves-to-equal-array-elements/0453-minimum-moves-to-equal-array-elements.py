class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum = min(nums)

        moves = sum(nums) - minimum * len(nums)

        return moves