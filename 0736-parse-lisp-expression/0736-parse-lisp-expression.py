class Solution:
    def evaluate(self, expression: str) -> int:

        def eval_expr(expr, scope):
            # Integer
            if expr[0] != '(':
                if expr.lstrip('-').isdigit():
                    return int(expr)

                # Variable
                for i in range(len(scope) - 1, -1, -1):
                    if expr in scope[i]:
                        return scope[i][expr]

            # Remove outer parentheses
            expr = expr[1:-1]

            # Split first word
            parts = []
            i = 0

            while i < len(expr):
                if expr[i] == ' ':
                    i += 1
                    continue

                start = i

                if expr[i] == '(':
                    count = 0
                    while i < len(expr):
                        if expr[i] == '(':
                            count += 1
                        elif expr[i] == ')':
                            count -= 1
                        i += 1

                        if count == 0:
                            break
                else:
                    while i < len(expr) and expr[i] != ' ':
                        i += 1

                parts.append(expr[start:i])

            command = parts[0]

            if command == "add":
                return eval_expr(parts[1], scope) + eval_expr(parts[2], scope)

            if command == "mult":
                return eval_expr(parts[1], scope) * eval_expr(parts[2], scope)

            # let expression
            new_scope = scope + [{}]

            # Assign variables sequentially
            for i in range(1, len(parts) - 1, 2):
                var = parts[i]
                value = eval_expr(parts[i + 1], new_scope)
                new_scope[-1][var] = value

            # Final expression
            return eval_expr(parts[-1], new_scope)

        return eval_expr(expression, [])