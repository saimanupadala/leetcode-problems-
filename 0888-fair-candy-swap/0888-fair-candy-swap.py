
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)

        diff = (sumA - sumB) // 2

        bobSet = set(bobSizes)

        for a in aliceSizes:
            b = a - diff

            if b in bobSet:
                return [a, b]
  