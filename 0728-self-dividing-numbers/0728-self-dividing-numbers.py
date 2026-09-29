class Solution:
    def selfDividingNumbers(self, left, right):
        ans = []

        for num in range(left, right + 1):
            n = num
            valid = True

            while n > 0:
                digit = n % 10

                if digit == 0 or num % digit != 0:
                    valid = False
                    break

                n //= 10

            if valid:
                ans.append(num)

        return ans