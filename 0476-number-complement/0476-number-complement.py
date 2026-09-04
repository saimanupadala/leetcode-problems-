class Solution:
    def findComplement(self, num: int) -> int:
        # Create a mask having all 1s
        mask = 0
        temp = num

        while temp > 0:
            mask = (mask << 1) | 1
            temp >>= 1

        # Flip only the bits used by num
        return num ^ mask