class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)

        def check(a, b, index):
            while index < n:
                total = a + b
                s = str(total)

                if not num.startswith(s, index):
                    return False

                index += len(s)
                a, b = b, total

            return True

        # Choose the first number
        for i in range(1, n):
            # Leading zero is not allowed
            if num[0] == '0' and i > 1:
                break

            a = int(num[:i])

            # Choose the second number
            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break

                b = int(num[i:j])

                # Need at least three numbers
                if check(a, b, j):
                    return True

        return False
        