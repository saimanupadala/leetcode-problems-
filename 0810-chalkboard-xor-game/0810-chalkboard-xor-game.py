class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        # Calculate total XOR sum of all elements
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        # Alice wins if initial XOR sum is 0 OR total length is even
        return xor_sum == 0 or len(nums) % 2 == 0