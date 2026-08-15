class Solution:
    def shortestPalindrome(self, s):
        if not s:
            return ""

        # Create pattern: s + "#" + reverse(s)
        rev = s[::-1]
        pattern = s + "#" + rev

        # KMP prefix table
        lps = [0] * len(pattern)

        for i in range(1, len(pattern)):
            j = lps[i - 1]

            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]

            if pattern[i] == pattern[j]:
                j += 1

            lps[i] = j

        # Length of longest palindromic prefix
        palindrome_len = lps[-1]

        # Remaining suffix
        remaining = s[palindrome_len:]

        # Add reversed suffix to the front
        return remaining[::-1] + s
        