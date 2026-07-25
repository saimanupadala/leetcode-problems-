class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(curr, open_count, close_count):
            # If the current string is complete
            if len(curr) == 2 * n:
                result.append(curr)
                return

            # Add an opening parenthesis if possible
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Add a closing parenthesis if it keeps the string valid
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result