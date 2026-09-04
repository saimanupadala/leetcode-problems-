class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)

        # Maximum possible number of digits
        max_len = num.bit_length()

        for length in range(max_len, 1, -1):

            # Find k using binary search
            left = 2
            right = int(num ** (1 / (length - 1))) + 2

            while left <= right:
                k = (left + right) // 2

                total = 1
                power = 1

                for _ in range(1, length):
                    power *= k
                    total += power

                    if total > num:
                        break

                if total == num:
                    return str(k)

                if total < num:
                    left = k + 1
                else:
                    right = k - 1

        # If no longer representation exists,
        # n = 11 in base (n - 1)
        return str(num - 1)