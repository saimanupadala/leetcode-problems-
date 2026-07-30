from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  
        result = []
        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            result.append(numbers.pop(index))
            k %= fact
        return "".join(result)
        