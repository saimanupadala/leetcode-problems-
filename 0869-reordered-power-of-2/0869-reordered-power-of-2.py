
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(str(n))

        for i in range(31):
            power = 1 << i
            if sorted(str(power)) == digits:
                return True

        return False
