class Solution:
    def removeInvalidParentheses(self, s):
        result = set()

        # Count minimum removals needed
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        def backtrack(index, left, right, balance, path):
            if index == len(s):
                if left == 0 and right == 0 and balance == 0:
                    result.add("".join(path))
                return

            ch = s[index]

            if ch == '(':
                # Remove '('
                if left > 0:
                    backtrack(index + 1, left - 1, right, balance, path)

                # Keep '('
                path.append(ch)
                backtrack(index + 1, left, right, balance + 1, path)
                path.pop()

            elif ch == ')':
                # Remove ')'
                if right > 0:
                    backtrack(index + 1, left, right - 1, balance, path)

                # Keep ')' only if it won't make balance negative
                if balance > 0:
                    path.append(ch)
                    backtrack(index + 1, left, right, balance - 1, path)
                    path.pop()

            else:
    
                path.append(ch)
                backtrack(index + 1, left, right, balance, path)
                path.pop()

        backtrack(0, left_remove, right_remove, 0, [])
        return list(result)
        