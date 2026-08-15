class Solution:
    def calculate(self, s):
        stack = []
        result = 0
        number = 0
        sign = 1

        i = 0

        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                number = 0

                while i < len(s) and s[i].isdigit():
                    number = number * 10 + int(s[i])
                    i += 1

                result += sign * number
                continue

            elif ch == '+':
                sign = 1

            elif ch == '-':
                sign = -1

            elif ch == '(':
                # Save current result and sign
                stack.append(result)
                stack.append(sign)

                # Start a new expression
                result = 0
                sign = 1

            elif ch == ')':
                # Complete the expression inside parentheses
                result = stack.pop() * result + stack.pop()

            i += 1

        return result
        