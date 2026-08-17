class Solution:
    def diffWaysToCompute(self, expression):
        def solve(expr):
            results = []
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i + 1:])
                    for a in left:
                        for b in right:
                            if expr[i] == "+":
                                results.append(a + b)
                            elif expr[i] == "-":
                                results.append(a - b)
                            else:
                                results.append(a * b)
            if not results:
                results.append(int(expr))
            return results
        return solve(expression)
        