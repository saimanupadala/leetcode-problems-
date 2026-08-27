class Solution:
    def getSum(self, a, b):
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
        if a <= MAX_INT:
            return a
        else:
            return ~(a ^ MASK)
        