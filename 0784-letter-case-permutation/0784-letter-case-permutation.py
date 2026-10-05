class Solution:
    def letterCasePermutation(self, s):
        result = []

        def backtrack(index, current):
            if index == len(s):
                result.append(current)
                return

            if s[index].isalpha():
                backtrack(index + 1, current + s[index].lower())
                backtrack(index + 1, current + s[index].upper())
            else:
                backtrack(index + 1, current + s[index])

        backtrack(0, "")
        return result