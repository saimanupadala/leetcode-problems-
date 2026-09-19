class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(s):
            coeff = 0
            const = 0
            i = 0
            sign = 1

            while i < len(s):
                if s[i] == '+':
                    sign = 1
                    i += 1
                elif s[i] == '-':
                    sign = -1
                    i += 1

                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1

                if j < len(s) and s[j] == 'x':
                    if j == i:
                        num = 1
                    else:
                        num = int(s[i:j])
                    coeff += sign * num
                    i = j + 1
                else:
                    if j > i:
                        const += sign * int(s[i:j])
                    i = j

            return coeff, const

        left, right = equation.split('=')

        a, b = parse(left)
        c, d = parse(right)

   
        if a == c and b == d:
            return "Infinite solutions"

        if a == c:
            return "No solution"

        x = (d - b) // (a - c)

        return "x=" + str(x)