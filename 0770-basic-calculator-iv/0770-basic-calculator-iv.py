class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):

        values = dict(zip(evalvars, evalints))

        def add(A, B, sign=1):
            result = A.copy()

            for key, value in B.items():
                result[key] = result.get(key, 0) + sign * value

                if result[key] == 0:
                    del result[key]

            return result

        def multiply(A, B):
            result = {}

            for vars1, coef1 in A.items():
                for vars2, coef2 in B.items():

                    variables = tuple(sorted(vars1 + vars2))

                    result[variables] = (
                        result.get(variables, 0) + coef1 * coef2
                    )

            return {
                key: value
                for key, value in result.items()
                if value != 0
            }

        tokens = expression.replace("(", " ( ").replace(")", " ) ").split()

        def parse_expression(pos):
            poly, pos = parse_term(pos)

            while pos < len(tokens) and tokens[pos] != ")":

                op = tokens[pos]
                right, pos = parse_term(pos + 1)

                if op == "+":
                    poly = add(poly, right)
                else:
                    poly = add(poly, right, -1)

            return poly, pos

        def parse_term(pos):
            poly, pos = parse_factor(pos)

            while pos < len(tokens) and tokens[pos] == "*":
                right, pos = parse_factor(pos + 1)
                poly = multiply(poly, right)

            return poly, pos

        def parse_factor(pos):
            token = tokens[pos]

            if token == "(":
                poly, pos = parse_expression(pos + 1)
                return poly, pos + 1

            if token.isdigit():
                return {(): int(token)}, pos + 1

            if token in values:
                return {(): values[token]}, pos + 1

            return {(token,): 1}, pos + 1

        poly, _ = parse_expression(0)

        terms = list(poly.items())

        # Higher degree first
        # Then lexicographical order
        terms.sort(key=lambda x: (-len(x[0]), x[0]))

        answer = []

        for variables, coefficient in terms:

            # Important: ignore zero coefficient
            if coefficient == 0:
                continue

            if variables:
                answer.append(
                    str(coefficient) + "*" + "*".join(variables)
                )
            else:
                answer.append(str(coefficient))

        return answer