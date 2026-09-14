class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        den = 1

        i = 0

        while i < len(expression):
            sign = 1

            if expression[i] == '+':
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1

            # Read numerator
            n = 0
            while i < len(expression) and expression[i].isdigit():
                n = n * 10 + int(expression[i])
                i += 1

            i += 1  # skip '/'

            # Read denominator
            d = 0
            while i < len(expression) and expression[i].isdigit():
                d = d * 10 + int(expression[i])
                i += 1

            n *= sign

            # Add fractions
            num = num * d + n * den
            den = den * d

            # Simplify
            import math
            g = math.gcd(abs(num), den)
            num //= g
            den //= g

        return str(num) + "/" + str(den)