class Solution:
    def partition(self, s):
        result = []
        current = []
        def is_palindrome(string):
            return string == string[::-1]
        def backtrack(start):
            if start == len(s):
                result.append(current[:])
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    current.append(substring)
                    backtrack(end)
                    current.pop()
        backtrack(0)
        return result
        